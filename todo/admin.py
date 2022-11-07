from django.contrib import admin
from .models import Todo


class todoAdmin(admin.ModelAdmin):
    list = ('title','description','completed')

admin.site.register(Todo,todoAdmin)

# Register your models here.
