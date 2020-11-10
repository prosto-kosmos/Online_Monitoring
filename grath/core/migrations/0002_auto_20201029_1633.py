# Generated by Django 2.0 on 2020-10-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='capacity_control',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='close',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='open_pos_control',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='short_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]