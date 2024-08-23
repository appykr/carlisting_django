from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email_id','car_title','user_city',)
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'car_title','email_id',)
    list_per_page = 25
admin.site.register(Contact, ContactAdmin)