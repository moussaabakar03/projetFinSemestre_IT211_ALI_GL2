# Generated by Django 5.1.3 on 2025-02-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopZenApp', '0004_alter_categorie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='produits'),
        ),
    ]
