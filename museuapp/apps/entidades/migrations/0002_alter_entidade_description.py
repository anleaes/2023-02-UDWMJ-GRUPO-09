# Generated by Django 4.1 on 2023-12-05 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidade',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Descricao'),
        ),
    ]
