from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import UserChangeForm,UserCreationForm

@admin.register(User)
class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    list_display = ['username',
                    'email',
                    'is_staff',
                    'is_active',
                    'role',
                    'first_name',
                    'last_name'
    ]

    list_filter = ['email', 'is_staff', 'is_superuser','is_active', 'role']
    fieldsets = (
    (
        _("Login Credentials"),
        {
            "fields": (
                "username",
                "password",
                "email",
            )
        },
    ),
    (
        _("Personal Information"),
        {"fields": ("first_name", "middle_name", "last_name","id_no","role")},
    ),
    (
      _("Account Status"),
      {
            "fields": ("account_status",
                       "failed_login_attempts",
                       "last_failed_login",)
      },
    ),
    (
        _("Security"),
     {
         "fields": ("security_question", "security_answer")
     },
    ),
    (
        _("Permissions and Groups"),
        {
            "fields": ("is_active",
                       "is_staff",
                       "is_superuser",
                       "groups",
                       "user_permissions",
            )
        },
    ),
    (
        _("Important Dates"),
        {
            "fields": (
                "last_login",
                "date_joined",
            )
        },
    ),
    )
    search_fields = ['username', 'email','first_name', 'last_name']
    ordering = ['email']
