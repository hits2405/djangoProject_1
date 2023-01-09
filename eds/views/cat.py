import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from eds.models import Category


def root(request):
    return JsonResponse({"status": "ok"})


class CatDV(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({"id": category.pk, "name": category.name}, safe=False)


class CatLV(ListView):
    model = Category
    queryset = Category.objects.order_by("name")

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by('name')
        return JsonResponse(data=[{"id": category.pk, "name": category.name} for category in self.object_list],
                            safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CatCV(CreateView):
    model = Category
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        cat_data = json.loads(request.body)
        new_cat = Category.objects.create(**cat_data)
        return JsonResponse({"id": new_cat.pk,
                             "name": new_cat.name
                             })


@method_decorator(csrf_exempt, name='dispatch')
class CatUV(UpdateView):
    model = Category
    fields = "__all__"

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        cat_data = json.loads(request.body)
        self.object.name = cat_data["name"]
        self.object.save()
        return JsonResponse({"id": self.object.pk,
                             "name": self.object.name
                             })


@method_decorator(csrf_exempt, name='dispatch')
class CatDeleteV(DeleteView):
    model = Category
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        cat = self.get_object()
        cat_pk = cat.pk
        super().delete(request, *args, **kwargs)
        return JsonResponse({"id": cat_pk})
