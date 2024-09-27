# Generated by Django 5.1.1 on 2024-09-15 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fblood', '0003_remove_donar_signup_info_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donar_donate_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=11)),
                ('blood', models.CharField(max_length=5)),
                ('date', models.CharField(max_length=15)),
                ('district', models.CharField(max_length=20)),
                ('police', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
