# Generated by Django 3.2 on 2022-11-12 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_auto_20221112_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Updatestudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('net_expenses', models.CharField(max_length=8)),
                ('f_installment', models.CharField(max_length=5)),
                ('f_receipt_number', models.CharField(max_length=4)),
                ('s_installment', models.CharField(max_length=5)),
                ('s_receipt_number', models.CharField(max_length=4)),
                ('th_installment', models.CharField(max_length=5)),
                ('th_receipt_number', models.CharField(max_length=4)),
                ('remaining_amount', models.CharField(max_length=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]