from django.urls import path

from app import views

urlpatterns = [
    path('', views.FileUpload.as_view(), name='index'),
    path('<int:pk>/', views.FileDetailView.as_view(), name='file-detail'),
]
