import json

from django.db.models import Count
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView
from rest_framework.generics import RetrieveAPIView, ListAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from users.models import User, Location
from users.serializers import UserDS, UserLS, UserCS, UserUS, LocationMS


class UserLV(ListAPIView):
    queryset = User.objects.filter().annotate(total_ad=Count('ad')).order_by('username')
    serializer_class = UserLS


class UserDV(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDS


class UserCV(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCS


class UserUV(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUS


class UserDeleteV(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDS


class LocationVS(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationMS


