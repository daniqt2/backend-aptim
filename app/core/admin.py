from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models
# Register your models here.

class UserAdmin(BaseUserAdmin):
    order = ['id']
    list_display = ['email','name']
    fieldsets = (
        (None,{'fields': ('email', 'password')}),
        (_('Personal Info'),{'fields':('name','last')}),
        (_('Identification Info'), {'fields':('username','identif','club','groups')}),
        (
            _('Permissions'),
            {'fields' : ('is_active','is_staff','is_superuser', 'is_apmaster')}
        ),
        (_('Important dates'), {'fields':('last_login',)}),
        (_('Images'), {'fields':('image',)})
        # (_('Requests'), {'fields':('requests',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    
admin.site.register(models.CustomUser, UserAdmin)
admin.site.register(models.Club)
admin.site.register(models.ClubGroup)
admin.site.register(models.Channel)
admin.site.register(models.Topic)
admin.site.register(models.Thread)
admin.site.register(models.Comment)
admin.site.register(models.Event)