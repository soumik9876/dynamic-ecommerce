# Generated by Django 4.1.6 on 2024-02-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('country', models.CharField(max_length=40, verbose_name='Country')),
                ('state', models.CharField(blank=True, max_length=40, verbose_name='State')),
                ('city', models.CharField(max_length=40, verbose_name='City')),
                ('street_number', models.CharField(blank=True, max_length=40, verbose_name='Street Number')),
                ('street_name', models.CharField(blank=True, max_length=40, verbose_name='Street Name')),
                ('zip', models.CharField(blank=True, max_length=20, verbose_name='ZIP')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]