from django.urls import path

from . import views

urlpatterns = [
    path("", views.View.as_view(), name='view'),
    path('<int:pk>/', views.Detail.as_view(), name='detail'),
]
