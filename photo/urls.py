# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:08:39 2023

@author: k_fujiyama
"""

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import my_view


app_name = 'photo'

urlpatterns = [
    path('my-view/', my_view, name='my_view'),

    
    path('',views.IndexView.as_view(), name='index'),
    path('post/', views.CreatePhotoView.as_view(), name='post'),
 
    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),
    
    path('photos/<int:category>',
         views.CategoryView.as_view(),
         name = 'photos_cat'
         ),
    
    path('user-list/<int:user>',
         views.UserView.as_view(),
         name = 'user_list'
         ),
    
    path('photo-detail/<int:pk>',
         views.DetailView.as_view(),
         name = 'photo_detail'
         ),
    
    path('mypage/',
         views.MypageView.as_view(), 
         name = 'mypage'
         ),
         
    path('photo/<int:pk>/delete',
         views.PhotoDeleteView.as_view(),
         name = 'photo_delete'
         ),
    
    path('photo/<int:pk>/delete',
         views.PhotoDeleteView.as_view(),
         name = 'photo_delete'
         ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)