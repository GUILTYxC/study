# Generated by Django 3.2 on 2024-04-07 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybei', '0004_usersettings_last_study_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersettings',
            old_name='last_study_date',
            new_name='last_new_word_fetch_date',
        ),
    ]
