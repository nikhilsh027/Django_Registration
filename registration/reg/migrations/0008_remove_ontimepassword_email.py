# Generated by Django 4.2 on 2024-12-19 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0007_remove_ontimepassword_stored_otp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ontimepassword',
            name='email',
        ),
    ]