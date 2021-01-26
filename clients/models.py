from django.db import models

class Client(models.Model):
    class Meta:
        db_table = 'clients'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    first_name = models.CharField(blank=False, null=False, max_length=60, default='', editable=True,verbose_name='First name')
    last_name = models.CharField(blank=False, null=False, max_length=80, default='', editable=True, verbose_name='Last name')
    email = models.EmailField(blank=False, null=False, max_length=60, default='', editable=True, verbose_name='Email')
    address = models.CharField(blank=False, null=False, max_length=50, default='', editable=True, verbose_name='Street address')
    city = models.CharField(blank=False, null=False, max_length=20, default='', editable=True, verbose_name='City')
    province = models.CharField(blank=False, null=False, max_length=20, default='', editable=True, verbose_name='Province')
    country = models.CharField(blank=False, null=False, max_length=40, default='', editable=True, verbose_name='Country')
    postal_code = models.CharField(blank=False, null=False, max_length=20, default='', editable=False, verbose_name='Postal / Zip code')


