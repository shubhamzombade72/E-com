from django.db import models

# Create your models here.

class Product(models.Model):
    # c_img=models.FileField(upload_to="E_com_app/",max_length=255,null=True,blank=True)
    c_img = models.FileField(upload_to="E_com_app/", max_length=255, blank=True, null=True)
    pname=models.CharField(max_length=255)
    discription=models.CharField(max_length=255)
    price=models.CharField(max_length=255)
    stock=models.CharField( max_length=255)
    class Meta:
        db_table = 'tbl_product'



