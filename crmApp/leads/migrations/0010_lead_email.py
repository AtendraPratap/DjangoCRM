# Generated by Django 4.2 on 2023-06-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0009_lead_date_added_lead_description_lead_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]