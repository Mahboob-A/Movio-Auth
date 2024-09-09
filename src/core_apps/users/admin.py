from django.contrib import admin


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core_apps.users.models import CustomUser


class CustomUserAdmin(BaseUserAdmin):

    list_display = [
        "id",
        "username",
        "email",
        "is_staff",
        "created_at",
        "updated_at",
    ]
    list_filter = ["email"]
    fieldsets = [
        (
            "User Credentials",
            {"fields": ["email", "username"]},
        ),
        (
            "Personal Information",
            {"fields": ["first_name", "last_name"]},
        ),
        (
            "Permissions",
            {
                "fields": [
                    "is_staff",
                ]
            },
        ),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "password",
                    "password2",
                    "is_staff",
                ],
            },
        ),
    ]
    search_fields = ["email", "username"]
    ordering = ["email", "username"]
    filter_horizontal = []



admin.site.register(CustomUser, CustomUserAdmin)
