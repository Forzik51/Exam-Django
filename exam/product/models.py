
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=4096, blank=True)
    main_photo = models.ImageField(upload_to='%Y/%m/%d')
    photo1 = models.ImageField(upload_to='%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = 'id',
