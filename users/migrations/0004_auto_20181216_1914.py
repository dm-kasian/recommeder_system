# Generated by Django 2.1.4 on 2018-12-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_facebooktokens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebooktokens',
            name='token',
            field=models.CharField(max_length=500),
        ),
    ]
