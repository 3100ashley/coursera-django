# Generated by Django 4.2.6 on 2023-11-01 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_drinkscategory_rename_drink_name_drinks_drink_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('guest_count', models.IntegerField()),
                ('reservation_time', models.DateField(auto_now=True)),
                ('comments', models.CharField(max_length=200)),
            ],
        ),
    ]
