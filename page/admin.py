from django.contrib import admin
from .models import Page, Carousel


# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'content', 'status', 'create_at']
    prepopulated_fields = {"slug": ('title',)}
    list_filter = ['status', 'create_at']
    # list_editable = ['status', 'title']


class CarouselAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'status', 'create_at']
    list_filter = ['status', 'create_at']


admin.site.register(Page, PageAdmin)
admin.site.register(Carousel, CarouselAdmin)