# Generated by Django 3.2.2 on 2021-05-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycinema', '0009_alter_news_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='short_description',
            field=models.CharField(max_length=100),
        ),
    ]