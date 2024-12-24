# Generated by Django 4.2 on 2024-12-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0011_remove_ontimepassword_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='ontimepassword',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='ontimepassword',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ontimepassword',
            name='ph_number',
            field=models.IntegerField(null=True),
        ),
    ]
