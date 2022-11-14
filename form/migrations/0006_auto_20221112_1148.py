# Generated by Django 3.2 on 2022-11-12 09:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_auto_20221112_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standardfees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('afees', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='formstudent',
            name='adminschool_fees',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formstudent',
            name='school_fees',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.standardfees'),
        ),
    ]