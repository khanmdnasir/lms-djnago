from django.contrib import admin
from .models import (user_profile)

# Register your models here.
@admin.register(user_profile)
class user_profile_admin(admin.ModelAdmin):
    list_display=['id','user','bio','profile_pic','user_type']