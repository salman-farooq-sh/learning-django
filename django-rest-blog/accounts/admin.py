from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "age", "is_staff"]
    search_fields = ("email",)
    ordering = ("email",)
    add_fieldsets = (
        (
            None,
            {"fields": ("email", 'age', "password1", "password2", "is_staff", "is_active")},
        ),
    )
    fieldsets = (
        (None, {"fields": ("email", 'age', "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
