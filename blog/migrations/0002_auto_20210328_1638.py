# Generated by Django 3.0.3 on 2021-03-28 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image1',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='image2',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='image3',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='image4',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
    ]