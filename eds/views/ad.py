from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from eds.permissions import IsAdOwnerOrStaff
from eds.serializers import *
from eds.models import Ad


def root(request):
    return JsonResponse({"status": "ok"})


class AdVS(ModelViewSet):
    queryset = Ad.objects.order_by('-price')
    default_serializer = AdS
    serializer_classes = {
        "List": AdLS,
        "retrieve": AdDetailS
    }
    default_permission = [AllowAny()]
    permissions = {
        "retrieve": [IsAuthenticated()],
        "partial_update": [IsAuthenticated(), IsAdOwnerOrStaff()],
        "update": [IsAuthenticated(), IsAdOwnerOrStaff()],
        "delete": [IsAuthenticated(), IsAdOwnerOrStaff()]
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        categories = request.GET.getlist('cat')
        if categories:
            self.queryset = self.queryset.filter(category_id__in=categories)
        text = request.GET.get('text')
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)
        location = request.GET.get('location')
        if location:
            self.queryset = self.queryset.filter(author__locations__name__icontains=location)
        price_from = request.GET.get('price_from')
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)
        price_to = request.GET.get('price_to')
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)
        return super().list(request, *args, **kwargs)


class AdDV(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailS


class AdCV(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCS


@method_decorator(csrf_exempt, name='dispatch')
class AdUpIm(UpdateView):
    model = Ad
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES('image')
        self.object.save()
        return JsonResponse({"id": self.object.pk,
                             "name": self.object.name,
                             "image": self.object.image.url
                             })


class AdUV(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUS


class AdDeleteV(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDeleteS
