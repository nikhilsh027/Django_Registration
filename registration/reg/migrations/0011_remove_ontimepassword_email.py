# Generated by Django 4.2 on 2024-12-19 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0010_remove_ontimepassword_otp_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ontimepassword',
            name='email',
        ),
    ]
