# Generated by Django 2.2.5 on 2019-12-03 04:44

from django.db import migrations, models
import django.db.models.deletion as dd


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_address_cid'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplierrep',
            name='works_for',
            field=models.ForeignKey(default=1, on_delete=dd.CASCADE,
                                    to='pages.Supplier'),
        ),
    ]
