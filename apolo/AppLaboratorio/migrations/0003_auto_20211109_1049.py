# Generated by Django 3.2.9 on 2021-11-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLaboratorio', '0002_energia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energia',
            name='f80',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='energia',
            name='p80',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='energia',
            name='wi',
            field=models.FloatField(),
        ),
    ]