from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, EmailActivation


class AccountAdmin(UserAdmin):
    list_display = ('email', 'date_joined', 'last_login', 'is_active')
    search_fields = ('email', 'date_joined', 'last_login',)
    readonly_fields = ("date_joined", 'last_login')
    
    # filter_horizontal = ()
    # list_filter = ()
    # fieldsets = ()
    
admin.site.register(User)

class EmailActivationAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = EmailActivation


admin.site.register(EmailActivation, EmailActivationAdmin)
