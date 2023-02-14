from django.urls import path

from . import views

urlpatterns = [ 
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('veg',views.veg,name='veg'),
    path('fruit',views.fruit,name='fruit'),
    path('personalcare',views.personalcare,name='personalcare'),
    path('snack',views.snack,name='snack'),
    path('householditem',views.householditem,name='householditem'),
    path('admin',views.admin,name='admin'),
    path('post_new', views.post_new, name='post_new'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('myacct',views.myacct,name='myacct'),
    path('checkout',views.checkout,name='checkout'),
    path('contact',views.contact,name='contact'),
    ]
    
   
