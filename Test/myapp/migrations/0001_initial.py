# Generated by Django 3.2.25 on 2024-07-20 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Up_UsersDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('store_image', models.CharField(blank=True, max_length=100, null=True)),
                ('official_email', models.CharField(max_length=100, unique=True)),
                ('primary_contact_number', models.CharField(blank=True, max_length=25, null=True)),
                ('password', models.CharField(max_length=255)),
                ('profile_image', models.CharField(blank=True, max_length=255, null=True)),
                ('web_auth_token', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]