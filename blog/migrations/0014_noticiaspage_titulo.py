# Generated by Django 3.2.11 on 2022-03-01 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20220301_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticiaspage',
            name='titulo',
            field=models.CharField(blank=True, max_length=250, verbose_name='Titulo'),
        ),
    ]