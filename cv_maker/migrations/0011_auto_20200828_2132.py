# Generated by Django 3.1 on 2020-08-28 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv_maker', '0010_auto_20200828_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='details',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='email',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='name',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='phone',
        ),
    ]