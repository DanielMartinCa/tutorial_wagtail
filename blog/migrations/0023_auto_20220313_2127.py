# Generated by Django 3.2.11 on 2022-03-13 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_contactpage_formfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='noticiaspage',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='viajespage',
            name='categories',
        ),
    ]
