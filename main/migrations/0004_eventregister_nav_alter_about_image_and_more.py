# Generated by Django 4.2.3 on 2023-08-02 20:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_number_numberofachievements'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First Name ', max_length=100)),
                ('last_name', models.CharField(help_text='First Name ', max_length=100)),
                ('PhoneNumber', models.CharField(blank=True, help_text='enter phone number', max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must contain 10 digits', regex='^\\d{10}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(help_text='Image Poster for news ', upload_to='static/images')),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='Image',
            field=models.ImageField(default=0, help_text='insert about image ', upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='events',
            name='Image',
            field=models.ImageField(default='default_image.jpg', help_text='Image Poster for news ', upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='existingprojects',
            name='Image',
            field=models.ImageField(help_text='project poster image', upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='news',
            name='Image',
            field=models.ImageField(help_text='Image Poster for news ', upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='poster',
            name='image',
            field=models.ImageField(help_text='Image Poster for news ', upload_to='static/images'),
        ),
    ]
