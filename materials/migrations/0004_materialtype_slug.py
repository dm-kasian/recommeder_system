# Generated by Django 2.1.3 on 2018-12-02 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0003_auto_20181202_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialtype',
            name='slug',
            field=models.SlugField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
