from django.urls import path

from eds.views import root

from eds.views import CatDV, CatLCV

urlpatterns = [
    path('', CatLCV.as_view()),
    path('<int:pk>/', CatDV.as_view())
]
