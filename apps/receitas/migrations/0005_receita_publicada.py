# Generated by Django 4.1.4 on 2022-12-19 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0004_receita_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]
