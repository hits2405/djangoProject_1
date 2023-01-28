from django.urls import path

from users.views import *

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', UserLV.as_view()),
    path('<int:pk>/', UserDV.as_view()),
    path('create/', UserCV.as_view()),
    path('<int:pk>/update/', UserUV.as_view()),
    path('<int:pk>/delete/', UserDeleteV.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

router = routers.SimpleRouter()
router.register('location', LocationVS)

urlpatterns += router.urls
