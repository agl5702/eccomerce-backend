from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField('Category Name', max_length=50)

    class Meta:

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return  self.name

class Customer(models.Model):

    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    phone = models.IntegerField('Phone number')
    email = models.EmailField('Email', max_length=254)
    password = models.CharField('Password', max_length=50)
    
    class Meta:
        """Meta definition for Customer."""

        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Product(models.Model):
    name = models.CharField('Product name', max_length=50)
    price = models.DecimalField('Price',default=0,decimal_places=2,max_digits=6)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=250,default='',blank=True,null=True)
    image = models.ImageField('Image product', upload_to='uploads/product/')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField('Sale price',default=0,decimal_places=2,max_digits=6)
    
    class Meta:

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
    
class Order(models.Model):
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100,default='',blank=False)
    phone=models.CharField(max_length=20,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)


    class Meta:

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order of {self.product.name}"


