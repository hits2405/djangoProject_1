from django.urls import path

from eds.views.ad import AdLCV, AdDV

urlpatterns = [
    path('', AdLCV.as_view()),
    path('<int:pk>/', AdDV.as_view())
]
