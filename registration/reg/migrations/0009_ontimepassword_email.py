# Generated by Django 4.2 on 2024-12-19 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0008_remove_ontimepassword_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='ontimepassword',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]