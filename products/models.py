from django.db import models

class Product(models.Model):
    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    product_name = models.CharField(blank=False, null=False,  max_length=50, default='', editable=True, verbose_name='Product name')
    product_brand = models.CharField(blank=False, null=False, max_length=40, default='', editable=True, verbose_name='Product brand')
    year_of_manufacture = models.IntegerField(blank=False, null=False, default=0, editable=True, verbose_name='Year of manufacture')
    color = models.CharField(blank=False, null=False, max_length=25, default='', editable=True, verbose_name='Color')
    description = models.TextField(blank=False, null=False, max_length=998, default='', editable=True, verbose_name='Description')
    prise = models.FloatField(blank=False, null=False, default=0, editable=True, verbose_name='Prise')

class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    category = models.CharField(blank=False, null=False, max_length=30, default='', editable=True, verbose_name='Category')
    description = models.TextField(blank=False, null=False, max_length=80, default='', editable=True, verbose_name='Description')

class ProductCategory(models.Model):
    class Meta:
        db_table = 'products_categories'
        verbose_name = 'Product category'
        verbose_name_plural = 'Products categories'

    product = models.ForeignKey(Product, blank=False, null=False, verbose_name='Good', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=False, null=False, verbose_name='Category', on_delete=models.CASCADE)
