# Generated by Django 3.1 on 2020-08-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_maker', '0013_auto_20200829_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='category',
            field=models.CharField(default='', max_length=255),
        ),
    ]