# Generated by Django 4.1.1 on 2022-10-29 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='contractNo',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
