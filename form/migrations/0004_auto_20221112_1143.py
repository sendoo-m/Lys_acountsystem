# Generated by Django 3.2 on 2022-11-12 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20221112_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formstudent',
            name='school_fees',
        ),
        migrations.DeleteModel(
            name='Standardfees',
        ),
    ]
