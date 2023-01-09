from django.urls import path

from eds.views.cat import root, CatUV, CatDeleteV, CatLV, CatCV, CatDV


urlpatterns = {
    path('', CatLV.as_view()),
    path('<int:pk>/', CatDV.as_view()),
    path('create/', CatCV.as_view()),
    path('<int:pk>/update/', CatUV.as_view()),
    path('<int:pk>/delete/', CatDeleteV.as_view()),
}
