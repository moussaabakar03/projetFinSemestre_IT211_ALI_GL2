# Generated by Django 5.1.3 on 2025-02-20 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopZenApp', '0007_alter_achat_modepayement_alter_achat_produit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achat',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achats', to='ShopZenApp.produit'),
        ),
    ]
