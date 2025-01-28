from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=255,null=True, blank=True)
    customer_email = models.EmailField(max_length=255,null=True, blank=True)
    quantity = models.CharField(max_length=200,null=True, blank=True)
    price = models.CharField(max_length=10,null=True, blank=True)
    total_amount = models.CharField(max_length=10,null=True, blank=True)  
    phone_number = models.CharField(max_length=10, null=True, blank=True)  
    status = models.CharField(
        max_length=50, 
        choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Returned', 'Returned')], 
        default='Pending'
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    order_date = models.DateField()  
    PAYMENT_METHOD_CHOICES = [
        ('COD', 'Cash on Delivery'),
        ('CARD', 'Credit/Debit Card'),
        ('UPI', 'UPI'),
    ]
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHOD_CHOICES,
        default='COD', 
    )

    class Meta:
        db_table = 'tbl_order'
        ordering = ['-order_date']
