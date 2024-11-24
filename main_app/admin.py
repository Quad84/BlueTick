from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Apps)
class MyAppsAdmin(admin.ModelAdmin):
    list_display = ('name', 'show')
    ordering = ('-show',)
    list_filter = ('show',)
    list_editable = ['show']
    fieldsets = [
        ('صفحه اصلی', {'fields': ['name', 'icon', 'slug' , 'show']}),
        ('صفحه جزئیات', {'fields': ['title', 'description', 'URL_website', 'URL_download', 'image']}),
    ]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    def has_add_permission(self, request):
        # بررسی تعداد آبجکت‌ها
        if Service.objects.count() >= 4:
            # اگر تعداد بیشتر از ۴ بود، مجوز افزودن آبجکت جدید را رد می‌کنیم
            return False
        return True

@admin.register(Message)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone' ,'service' , 'created')
    list_filter = ('service',)
    readonly_fields = ('full_name', 'phone' , 'service', 'created' )

@admin.register(BlueTick_info)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('phone', 'telegram')

    def has_add_permission(self, request):
        if BlueTick_info.objects.count() >= 1:
            return False
        return True

@admin.register(ads_banner)
class ServiceAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if ads_banner.objects.count() >= 3:
            return False
        return True