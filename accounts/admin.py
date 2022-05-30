from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# from .forms import CreationUserForm
from .models import User  # AccountInfo
#
#
# class AccountInfoInline(admin.StackedInline):
#     model = AccountInfo
#     can_delete = False
#     verbose_name_plural = 'AccountInfo'
#


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_admin', 'is_active')
    search_fields = ('email',)
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ('last_login',)
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    ordering = ('email',)


# # admin.site.register(AccountInfo)
admin.site.register(User, UserAdmin)

