# Generated by Django 2.1.4 on 2018-12-16 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0007_material_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='image',
            field=models.ImageField(max_length=500, upload_to=''),
        ),
    ]
