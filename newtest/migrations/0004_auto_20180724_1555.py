# Generated by Django 2.0.5 on 2018-07-24 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newtest', '0003_auto_20180712_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passid', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='clientid',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
