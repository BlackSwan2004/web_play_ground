from django.contrib import admin
from .models import Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','orden')
    list_filter = ('title', 'orden')

admin.site.register(Page, PageAdmin)