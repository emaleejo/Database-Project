# Generated by Django 2.2.5 on 2019-12-03 00:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion as dd


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0004_auto_20191202_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='sampleFiels',
        ),
        migrations.AddField(
            model_name='review',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=dd.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
