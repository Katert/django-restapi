# Generated by Django 3.1.4 on 2020-12-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testDb', '0003_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='salary_scale',
            field=models.IntegerField(),
        ),
    ]