# Generated by Django 4.0.6 on 2022-07-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Title')),
                ('image', models.ImageField(upload_to='product')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('price', models.IntegerField()),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(blank=True, verbose_name='Description')),
            ],
        ),
        migrations.DeleteModel(
            name='Chopi',
        ),
    ]
