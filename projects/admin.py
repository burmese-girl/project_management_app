from django.contrib import admin
from .models import *

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_per_page = 20
    ordering = ['-id']
    search_fields = []
    readonly_fields = []
    list_display = [f.name for f in Task._meta.fields if not f.name == "id"]


admin.site.register(Task,TaskAdmin)