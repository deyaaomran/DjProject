# Generated by Django 5.2.4 on 2025-07-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.png', upload_to='photos/%y/%m/%d'),
            preserve_default=False,
        ),
    ]
