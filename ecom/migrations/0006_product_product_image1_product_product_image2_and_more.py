# Generated by Django 5.0 on 2023-12-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_feedback_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image1',
            field=models.ImageField(blank=True, null=True, upload_to='product_image/'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image2',
            field=models.ImageField(blank=True, null=True, upload_to='product_image/'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='salom'),
        ),
    ]
