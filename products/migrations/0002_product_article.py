# Generated by Django 3.0.5 on 2020-11-18 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='article',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True),
        ),
    ]
