# Generated by Django 3.1.3 on 2021-08-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_auto_20210821_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='addquestiont',
            name='canswer',
            field=models.IntegerField(default=1),
        ),
    ]
