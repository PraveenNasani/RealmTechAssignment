from django.db import models


class Vendor(models.Model):
    shop_name = models.CharField(max_length=200)

    def __str__(self):
        return self.shop_name

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    vendor = models.ForeignKey(Vendor, related_name='category', on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name


class Items(models.Model):
    item_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name