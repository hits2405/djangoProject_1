from django.urls import path

from users.views import *


urlpatterns = [
    path('', UserLV.as_view()),
    path('<int:pk>/', UserDV.as_view()),
    path('create/', UserCV.as_view()),
    path('<int:pk>/update/', UserUpV.as_view()),
    path('<int:pk>/delete/', UserDeleteV.as_view()),
]