from django.contrib import admin
from .models import HelloModel
# Register your models here.
@admin.register(HelloModel)
class HelloModelAdmin(admin.ModelAdmin):
    pass