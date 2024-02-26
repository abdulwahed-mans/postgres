from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brand = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/', blank=True)
    is_active = models.BooleanField(default=True)
    slogan = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True)
    barcode = models.CharField(max_length=255, blank=True)  

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/products/{self.slug}/"
    
    def get_image(self):
        if self.image:
            return self.image.url
        return '/static/assets/images/default.jpg'
    
    def get_price(self):
        return "{:.2f}".format(self.price)
    
    def get_stock(self):
        return self.stock
    
    