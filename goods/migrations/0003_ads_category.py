# Generated by Django 3.2.7 on 2021-09-12 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_ads_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='goods.category'),
        ),
    ]