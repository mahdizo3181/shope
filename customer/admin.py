from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, OtpCode
from .forms import UserChangedForm, UserCreateForm
from django.contrib.auth.models import Group


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'code', 'created']


@admin.register(User)
class Admin(UserAdmin):
    form = UserChangedForm
    add_form = UserCreateForm
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone', 'is_superuser', 'is_staff',)
    fieldsets = ((None, {'fields': ('username', 'first_name', 'last_name', 'email', 'phone', 'password',)}),
                 ('Personal info', {'fields': ('is_active',)}),
                 ('Permissions', {'fields': ('is_superuser',)}),
                 ('Permissions groups', {'fields': ('is_staff',)})
                 )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2', 'groups',)
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups',)
