# Generated by Django 5.1.3 on 2025-02-19 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopZenApp', '0005_alter_produit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achat',
            name='modePayement',
            field=models.CharField(choices=[('carte_credit', 'Carte de crédit'), ('tmoney', 'TMoney'), ('flooz', 'Flooz')], default='carte_credit', max_length=255),
        ),
    ]
