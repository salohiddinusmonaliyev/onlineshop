# Generated by Django 4.1.3 on 2022-11-08 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.FileField(null=True, upload_to='category/'),
        ),
    ]
