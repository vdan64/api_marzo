from django.contrib import admin

# Register your models here.
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'important')
    search_fields = ('title', 'body')
    list_filter = ('title', 'body', 'important', 'created_at', 'completed')
    list_per_page = 10
    ordering = ('important',)



admin.site.register(Task, TaskAdmin)