from django.contrib import admin
from . models import Car, Feature
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" style="width: 50px; border-radius: 50px;"/>'.format(object.car_photo.url))
    thumbnail.short_description = 'Photo'

    list_display = ('id','thumbnail','car_title','year', 'created_date','is_featured')
    list_display_links = ('id','thumbnail','car_title')
    search_fields = ('car_title','year', 'model')
    list_editable = ('is_featured',)
    list_filter = ('fuel_type',)

admin.site.register(Car, CarAdmin)
admin.site.register(Feature)