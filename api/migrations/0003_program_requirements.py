# Generated by Django 3.0.4 on 2020-04-25 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_program'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='requirements',
            field=models.CharField(default='', max_length=2048),
            preserve_default=False,
        ),
    ]
