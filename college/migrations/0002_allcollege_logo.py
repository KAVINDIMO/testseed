# Generated by Django 3.1.3 on 2021-10-08 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcollege',
            name='logo',
            field=models.ImageField(default='images/tst2.jpg', upload_to='images'),
        ),
    ]
