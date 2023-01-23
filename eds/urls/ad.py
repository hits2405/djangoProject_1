from django.urls import path

from eds.views.ad import *

urlpatterns = [
    path('', AdLCV.as_view()),
    path('<int:pk>/', AdDV.as_view()),
    path('create/', AdCV.as_view()),
    path('<int:pk>/upload_image/', AdUpIm.as_view()),
    path('<int:pk>/update/', AdUV.as_view()),
    path('<int:pk>/delete/', AdDeleteV.as_view()),
]
