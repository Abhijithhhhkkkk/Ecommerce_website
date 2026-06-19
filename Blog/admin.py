from django.contrib import admin
from .models import Homepage,logo,details,order_details

# Register your models here.
admin.site.register(Homepage)
admin.site.register(logo)
admin.site.register(details)
#to create table view
class order_admin(admin.ModelAdmin):
    list_display=('product','buyer')
    search_fields = ('buyer__email', 'product__title')
admin.site.register(order_details,order_admin)