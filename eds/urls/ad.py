from django.urls import path

from eds.views.ad import *

from rest_framework import routers

urlpatterns = [
    # path('ad/', AdVS.as_view({'get': 'list'})),
    path('ad/<int:pk>/', AdDV.as_view()),
    path('ad/create/', AdCV.as_view()),
    path('ad/<int:pk>/upload_image/', AdUpIm.as_view()),
    path('ad/<int:pk>/update/', AdUV.as_view()),
    path('ad/<int:pk>/delete/', AdDeleteV.as_view()),
]

router = routers.SimpleRouter()
router.register('ad', AdVS)

urlpatterns += router.urls
