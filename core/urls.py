from django.urls import path,include
from . import views

app_name = 'core'

urlpatterns = [
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('', views.index)
]