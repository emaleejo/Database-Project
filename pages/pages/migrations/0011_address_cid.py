# Generated by Django 2.2.5 on 2019-12-03 04:35

from django.db import migrations, models
import django.db.models.deletion as dd


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20191202_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='cid',
            field=models.ForeignKey(default=1, on_delete=dd.CASCADE,
                                    to='pages.ContactDetail'),
        ),
    ]
