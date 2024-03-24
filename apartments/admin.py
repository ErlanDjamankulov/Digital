from django.contrib import admin

from .models import Category,Status,Clients,Flats,Manager

admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Clients)
admin.site.register(Flats)
admin.site.register(Manager)