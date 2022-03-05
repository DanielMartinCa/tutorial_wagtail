# Generated by Django 3.2.11 on 2022-03-02 08:45

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0015_viajespage_coordenadas'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViajePageTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='blog.viajespage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_viajepagetag_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ViajesTagIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]