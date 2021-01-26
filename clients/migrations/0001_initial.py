# Generated by Django 3.1.5 on 2021-01-19 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=60, verbose_name='First name')),
                ('last_name', models.CharField(default='', max_length=80, verbose_name='Last name')),
                ('email', models.EmailField(default='', max_length=60, verbose_name='Email')),
                ('address', models.CharField(default='', max_length=50, verbose_name='Street address')),
                ('city', models.CharField(default='', max_length=20, verbose_name='City')),
                ('province', models.CharField(default='', max_length=20, verbose_name='Province')),
                ('country', models.CharField(default='', max_length=40, verbose_name='Country')),
                ('postal_code', models.CharField(default='', editable=False, max_length=20, verbose_name='Postal / Zip code')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'db_table': 'clients',
            },
        ),
    ]