# Generated by Django 3.2 on 2024-04-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybei', '0003_auto_20240407_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersettings',
            name='last_study_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
