# Generated by Django 3.1.1 on 2021-06-05 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_auto_20210605_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='vendor.vendor'),
        ),
    ]