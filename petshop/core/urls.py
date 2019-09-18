from django.urls import path
from petshop.core.views import home
app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
]