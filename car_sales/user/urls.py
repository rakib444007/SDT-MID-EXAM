from django.urls import path,include
from django.contrib import admin
from .import views

urlpatterns = [
    path('signup/',views.signup , name='signup'),
    path('login/',views.UserLoginView.as_view() , name='user_login'),
    path('logout/',views.user_logout , name='user_logout'),
    path('profile/',views.ProfileView.as_view() , name='profile'),
    path('profile/edit/pass_change',views.pass_change, name='pass_change'),
    path('profile/edit',views.edit_profile , name='edit_profile'),
     path('buy-car/<int:id>/',views.CarBuyUser,name='buy_car'),
]
