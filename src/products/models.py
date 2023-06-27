from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    title       = models.TextField()
    # blank for frontend/ui, null for database
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=50)
    summary     = models.TextField(blank=False, null=False)

    def get_absolute_url(self):
        # return f"/product/{self.id}/"
        return reverse(viewname="products:product-detail", kwargs={
                           "id" : self.id
                       }) # 'products' came from app_name in products.urls
