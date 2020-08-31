# Generated by Django 3.1 on 2020-08-28 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_maker', '0007_auto_20200828_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
    ]
