from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('search', search, name = 'search-query'),
    path('items/<int:ids>', items, name = 'items'),
    path('details/<int:ids>', details, name = 'details'),
]