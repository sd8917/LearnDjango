# Generated by Django 2.2.4 on 2019-11-02 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importapp', '0002_auto_20191102_0729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='rollno',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
