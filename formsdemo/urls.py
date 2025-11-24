from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('add-phone-field/', views.add_phone_field, name='add_phone'),  
]