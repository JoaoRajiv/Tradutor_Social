# Generated by Django 2.2.5 on 2019-09-11 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publicacao', '0004_correction_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correction',
            name='corrector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Corretor', to=settings.AUTH_USER_MODEL, verbose_name='Corretor'),
        ),
        migrations.AlterField(
            model_name='correction',
            name='publication',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publicacao.Publication', verbose_name='Publicação'),
        ),
    ]
