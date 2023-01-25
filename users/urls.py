from django.urls import path

from users.views import *

from rest_framework import routers

urlpatterns = [
    path('user/', UserLV.as_view()),
    path('user/<int:pk>/', UserDV.as_view()),
    path('user/create/', UserCV.as_view()),
    path('user/<int:pk>/update/', UserUV.as_view()),
    path('user/<int:pk>/delete/', UserDeleteV.as_view()),
]

router = routers.SimpleRouter()
router.register('location', LocationVS)

urlpatterns += router.urls
