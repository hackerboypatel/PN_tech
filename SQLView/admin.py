from django.contrib import admin
from .models import Restaurant
# Register your models here.


class ResturantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'lat_long', 'items', 'full_details')


admin.site.register(Restaurant, ResturantAdmin)