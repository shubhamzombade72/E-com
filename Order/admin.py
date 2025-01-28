from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name','customer_email', 'phone_number', 'order_date', 'status','quantity','price', 'total_amount', 'payment_method')  
    list_filter = ('status', 'order_date', 'payment_method') 
    search_fields = ('id', 'customer_name', 'customer_email', 'phone_number')  

admin.site.register(Order, OrderAdmin)
