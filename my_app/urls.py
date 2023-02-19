from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('sunglasses/', views.SunglassesCreate, name='sunglasses'),
    path('sunglasses/<int:pk>/delete', views.SunglassesDelete.as_view(),name='delete'),
    path('sunglasses/<int:pk>/update', views.SunglassesUpdate.as_view(),name='update'),
    path('sunglasses/<int:pk>/detail', views.SunglassesDetail.as_view(),name='sunglasses_detail'),
]