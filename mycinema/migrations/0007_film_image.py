# Generated by Django 3.2.2 on 2021-06-04 18:36

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('mycinema', '0006_auto_20210604_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='film/film_default.png', force_format=None, keep_meta=True, quality=90, size=[256, 256], upload_to='film/'),
        ),
    ]
