from django.db import models

# Create your models here.


SITUATION   = (
    ('Didentpay','لم يقم بالدفع'),
    ('Remaininstallment','باقي اقساط'),
    ('Done','خالص')
)


class Formstudent(models.Model):
    name                = models.CharField("إسم الطالب",max_length=100, blank=True)
    id_number           = models.CharField("الرقم القومي",max_length=14, blank=True)
    school_fees         = models.CharField("مصاريف المدرسة",max_length=255, blank=True)
    activity            = models.CharField("نشاط",max_length=3, blank=True)
    discount            = models.CharField("خصم",max_length=4, blank=True)
    net_expenses        = models.CharField("الصافي",max_length=8, blank=True)
    f_installment       = models.CharField("القسط الاول",max_length=5, blank=True)
    f_receipt_number    = models.CharField("إيصال القسط الاول",max_length=4, blank=True)
    s_installment       = models.CharField("القسط الثاني",max_length=5, blank=True)
    s_receipt_number    = models.CharField("إيصال القسط الثاني",max_length=4, blank=True)
    th_installment      = models.CharField("القسط الثالث",max_length=5, blank=True)
    th_receipt_number   = models.CharField("إيصال القسط الثالث",max_length=4, blank=True)
    remaining_amount    = models.CharField("الباقي",max_length=8, blank=True)
    situation           = models.CharField("حالة الطالب",max_length=50, null=True, choices=SITUATION, default='Didentpay')
    created_at          = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Formstudent'
        managed = True
        verbose_name = 'Registration'
        verbose_name_plural = 'Registrations'
   
    def __str__(self):
        return self.name

    # Capitalize (name)
    def clean(self):
        self.name  =self.name.capitalize()        # to write all text reformat capitalize

class Updatestudent(models.Model):
    name                = models.CharField(max_length=100, blank=True)

    net_expenses        = models.CharField(max_length=8, blank=True)
    f_installment       = models.CharField(max_length=5, blank=True)
    f_receipt_number    = models.CharField(max_length=4, blank=True)
    s_installment       = models.CharField(max_length=5, blank=True)
    s_receipt_number    = models.CharField(max_length=4, blank=True)
    th_installment      = models.CharField(max_length=5, blank=True)
    th_receipt_number   = models.CharField(max_length=4, blank=True)
    remaining_amount    = models.CharField(max_length=8, blank=True)

    created_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # Capitalize (name)
    def clean(self):
        self.name  =self.name.capitalize()        # to write all text reformat capitalize