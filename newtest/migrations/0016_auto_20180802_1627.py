# Generated by Django 2.0.5 on 2018-08-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newtest', '0015_auto_20180802_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='clientid',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
