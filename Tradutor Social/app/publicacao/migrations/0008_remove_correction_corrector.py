# Generated by Django 2.2.5 on 2019-09-11 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicacao', '0007_auto_20190911_0419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='correction',
            name='corrector',
        ),
    ]