from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Manager, BasicUser, Donation


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "email", "phone", "full_name"]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("phone", "full_name")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Manager)
admin.site.register(BasicUser)
admin.site.register(Donation)
