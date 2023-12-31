from django.contrib import admin
from django.urls import path
from Rojgar import views
from .views import *
from .views import item_detail
from .views import get_user_profile



from django.urls import path , include
from Rojgar import views

urlpatterns = [
     path('login/',views.login_page , name='login'),
     path('signup/',views.singup_page , name='signup'),
     path('home/',views.home_page , name='home'),
     path('logout/',views.logout_page , name='logout'),
     path('request/',views.request , name='request'),
     path('formadded',views.formadded , name='formadded'),
     path('admin/',views.admin_redirect , name='admin_redirect'),
     path('admin/',views.admin_redirect , name='admin_redirect'),
     path('home/',views.home_page , name='home_page'),
     path('work/',views.work , name='work'),
     path('item/<int:item_id>/', item_detail, name='item_detail'),
     path('be_worker/',views.be_worker, name='be_worker'),
     # path('',views.home_redirect , name='home_redirect'),
     path('get_user_profile/', get_user_profile, name='get_user_profile'),
    path('request_detail_accepted/<int:request_id>/', request_detail_accepted, name='request_detail_accepted'),
    path('request_detail_waiting/<int:request_id>/', request_detail_waiting, name='request_detail_waiting'),
    path('mark_work_done/<int:request_id>/', views.mark_work_done, name='mark_work_done'),
    path('payment/',views.payment , name='payment'),
    path('profile/',views.profile , name='profile'),
    path('',views.home , name='home'),
]


     
 
