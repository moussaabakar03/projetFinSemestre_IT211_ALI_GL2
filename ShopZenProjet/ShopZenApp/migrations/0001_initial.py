# Generated by Django 5.1.3 on 2025-02-14 21:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='categories')),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prixTotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dateFacture', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PanierClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomClient', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Achat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('prixUnitaire', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dateAchat', models.DateTimeField(auto_now_add=True)),
                ('modePayement', models.CharField(max_length=255)),
                ('prixTotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('panierDuClient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShopZenApp.panierclient')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='produits')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantite', models.IntegerField()),
                ('dateAjoutProduit', models.DateTimeField(auto_now_add=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShopZenApp.categorie')),
            ],
        ),
        migrations.AddField(
            model_name='panierclient',
            name='achats',
            field=models.ManyToManyField(through='ShopZenApp.Achat', to='ShopZenApp.produit'),
        ),
        migrations.AddField(
            model_name='achat',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShopZenApp.produit'),
        ),
    ]
