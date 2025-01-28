from django.contrib import admin

# Register your models here.
from E_com_app.models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display=('discription','stock','price','pname','c_img')
admin.site.register(Product,ProductAdmin)
