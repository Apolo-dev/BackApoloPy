# Generated by Django 3.2.9 on 2021-11-19 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLaboratorio', '0006_auto_20211118_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='labgiratorio',
            name='fechaActual',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]