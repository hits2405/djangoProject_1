from django.urls import path

from eds.views.cat import root

from eds.views.cat import CatDV, CatLV

urlpatterns = [
    path('', CatLV.as_view()),
    path('<int:pk>/', CatDV.as_view())
]
