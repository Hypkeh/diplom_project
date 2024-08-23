from django.urls import path
from django.contrib.auth import views
from . import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='main_page'),
    
    path('search/', views.search, name='search_form'),


    path('announcments/', views.AnnouncmentList.as_view(), name='announcment_list'),
    path('create/', views.AnnouncmentCreate.as_view(), name='announcment_create'),
    path('update/<int:pk>', views.AnnouncmentUpdate.as_view(), name='announcment_update'),
    path('delete/<int:pk>/', views.AnnouncmentDelete.as_view(), name='announcment_delete'),
    path('<int:pk>/', views.AnnouncmentDetail.as_view(), name='announcment_detail'),
]