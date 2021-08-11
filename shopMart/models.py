from django.db import models

# Create your models here.
class Categrory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return  self.name

class Product(models.Model):
    product_Name            =   models.CharField(max_length=100)
    price                   =   models.IntegerField()
    category                =   models.ForeignKey(Categrory,on_delete=models.CASCADE)
    color                   =   models.ForeignKey(Color,on_delete=models.CASCADE)
    short_decription        =   models.CharField(max_length=600)
    decription              =   models.TextField()
    main_Image              =   models.FileField(blank=True)
    is_available            =   models.BooleanField(default=True)
    is_active               =   models.BooleanField(default=True)
    created                 =   models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.product_Name
    
    def get_images(self):
        return ProductImage.objects.filter(product=self)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="myApp/images")
 
    def __str__(self):
        return self.product_Name
