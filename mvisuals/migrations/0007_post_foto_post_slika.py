# Generated by Django 5.0.6 on 2024-06-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvisuals', '0006_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='foto',
            field=models.ImageField(default='/hw5_final/media/products/canon.jpg', upload_to='products'),
        ),
        migrations.AddField(
            model_name='post',
            name='slika',
            field=models.ImageField(default='/hw5_final/media/products/canon.jpg', upload_to='products'),
        ),
    ]