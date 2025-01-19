from django.contrib import admin
from .models import CustomUser, Blog
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
  list_display = ("username", "email", "first_name", "last_name")

class BlogAdmin(admin.ModelAdmin):
  list_display = ("title", "is_draft", "category", "created_at")

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Blog, BlogAdmin)