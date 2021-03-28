# Generated by Django 3.0.3 on 2021-03-28 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210328_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='image1',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image4',
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='portfolio/images/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
    ]
