from django.contrib import admin
from django.contrib.admin import ModelAdmin

from goods.models import Ads, Category


class AdsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'created_at', 'photo', 'price', 'view')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content')
    list_filter = ('category', 'price', 'created_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Ads, AdsAdmin)
admin.site.register(Category, CategoryAdmin)


# @admin.register(Ads)
# class AdsAdmin(ModelAdmin):
#     pass

