# Generated by Django 3.2 on 2022-11-10 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formstudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_number', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=14)),
                ('school_fees', models.CharField(max_length=8)),
                ('activity', models.CharField(max_length=3)),
                ('discount', models.CharField(max_length=4)),
                ('net_expenses', models.CharField(max_length=8)),
                ('f_installment', models.CharField(max_length=5)),
                ('f_receipt_number', models.CharField(max_length=4)),
                ('s_installment', models.CharField(max_length=5)),
                ('s_receipt_number', models.CharField(max_length=4)),
                ('th_installment', models.CharField(max_length=5)),
                ('th_receipt_number', models.CharField(max_length=4)),
                ('remaining_amount', models.CharField(max_length=8)),
                ('situation', models.CharField(choices=[('Didentpay', 'لم يقم بالدفع'), ('Remaininstallment', 'باقي اقساط'), ('Done', 'خالص')], default='Didentpay', max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
