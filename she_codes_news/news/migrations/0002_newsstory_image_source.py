# Generated by Django 3.0.8 on 2020-08-22 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='image_source',
            field=models.CharField(default='https://picsum.photos/600', max_length=200),
        ),
    ]