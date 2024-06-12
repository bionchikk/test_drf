from django.contrib import admin
from .models import User, Task


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone', 'is_employee', 'is_client')
    search_fields = ('username', 'email', 'phone')
    list_filter = ('is_employee', 'is_client')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'employee', 'status', 'created_at', 'updated_at', 'closed_at', 'report')
    search_fields = ('client__username', 'employee__username', 'status')
    list_filter = ('status', 'created_at', 'updated_at', 'closed_at')
