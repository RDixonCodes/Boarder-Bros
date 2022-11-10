from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/register', views.registration_page),
    path('user/register', views.user_register),
    path('user/login', views.login),
    path('success', views.success),
    path('add/items', views.add),
    path('items/list', views.view_items),
    path('logout', views.logout)
    # path('new/user', views.new_user),
    # path('create/user', views.create_user),
]