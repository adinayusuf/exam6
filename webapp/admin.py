from django.contrib import admin

# Register your models here.
from webapp.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'create_time']
    list_filter = ['status']
    search_fields = ['status']
    fields = ['name', 'status', 'email', 'text']
    readonly_fields = ['create_time']


admin.site.register(GuestBook, GuestBookAdmin)
