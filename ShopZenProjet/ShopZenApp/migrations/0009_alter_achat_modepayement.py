# Generated by Django 5.1.3 on 2025-02-24 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopZenApp', '0008_alter_achat_produit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achat',
            name='modePayement',
            field=models.CharField(choices=[('En spece', 'En spece'), ('tmoney', 'TMoney'), ('flooz', 'Flooz')], default='En spece', max_length=20),
        ),
    ]
