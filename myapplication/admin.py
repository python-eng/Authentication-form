from django.contrib import admin
from myapplication.models import Singup

# Register your models here.

@admin.register(Singup)
class SignUpAdmin(admin.ModelAdmin):
    list_display=['username','email','first_name','last_name','Address']