from django.contrib import admin

# Register your models here.
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display =('id','username')
    list_display_links =('id','username')
    
admin.site.register(CustomUser,CustomUserAdmin)