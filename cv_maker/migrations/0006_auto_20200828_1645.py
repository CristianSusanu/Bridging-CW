# Generated by Django 3.1 on 2020-08-28 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv_maker', '0005_experience_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='detail',
            new_name='details',
        ),
    ]