from django import forms
from form.models import Formstudent, Updatestudent
from django.core.validators import RegexValidator # لعمل صلاحيات خاصة على الحقول 
from django.core.exceptions import ValidationError # مستخدم في داله عدم تكرار المدخلات



class FormstudentForm(forms.ModelForm):
    # validations
        
    # Student`s` name 
    name       = forms.CharField(
        label       ='اسم الطالب',max_length=50, 
        min_length  =9,
        validators  =[RegexValidator(r'^[\u0621-\u064Aa-zA-Z\d\-_\s]*$', 
        message     ="الاسم غير صحيح")],
        error_messages={'required':'يرجي ادخال اسم الطالب'}, 
        widget      =forms.TextInput(attrs={
            'placeholder':'اسم الطالب',
            'style': 'font-size: 18px; text-transform: capitalize'
            })
        )

    #  Age Number only
    id_number       = forms.CharField(
        label       ='الرقم القومي', max_length=14, 
        min_length  =1,
        validators  =[RegexValidator(r'^[0-9]*$', 
        message     ="الرقم القومي غير صحيح")],
        error_messages={'required':'يرجي ادخال الرقم القومي'}, 
        widget      =forms.TextInput(attrs={
            'placeholder':'الرقم القومي',
            'style': 'font-size: 18px'
            })
        )

    # school_fees number only
    school_fees     = forms.CharField(
        label       ='مصروفات مدرسية', max_length=8, 
        min_length  =8,
        required    =False,
        widget      =forms.TextInput(attrs={
            'placeholder':'مصروفات مدرسية',
            'default':'18416.59',
            'style': 'font-size: 18px;'
            })
        )

    # activity only
    activity     = forms.CharField(
        label       ='نشاط', max_length=3, 
        min_length  =3,
        )

    # DISCOUNT number only
    discount     = forms.CharField(
        label       ='خصم', max_length=4, 
        min_length  =4,
        required    =False,
        )
    
    # net_expenses number only
    net_expenses     = forms.CharField(
        label       ='صافي المبلغ', max_length=8, 
        min_length  =8,
        required    =False,
        widget      =forms.TextInput(attrs={
            'placeholder':'الصافي',
            'style': 'font-size: 18px;'
            })
        )

    # f_installment number only
    f_installment     = forms.CharField(
        label       ='القسط الاول', max_length=5, 
        min_length  =4,
        required    =False,
        )

    # f_receipt_number number only
    f_receipt_number     = forms.CharField(
        label       =' ايصال القسط الاول', max_length=4, 
        min_length  =4,
        required    =False,
        )

    # s_installment number only
    s_installment     = forms.CharField(
        label       ='القسط الثاني', max_length=5, 
        min_length  =4,
        required    =False,
        )

    # s_receipt_number number only
    s_receipt_number     = forms.CharField(
        label       =' ايصال القسط الثاني', max_length=4, 
        min_length  =4,
        required    =False,
        )

    # th_installment number only
    th_installment     = forms.CharField(
        label       ='القسط الثالث', max_length=5, 
        min_length  =4,
        required    =False,
        )

    # th_receipt_number number only
    th_receipt_number     = forms.CharField(
        label       =' ايصال القسط الثالث', max_length=4, 
        min_length  =4,
        required    =False,
        )

    # th_receipt_number number only
    remaining_amount     = forms.CharField(
        label       =' الباقي ', max_length=8, 
        min_length  =1,
        required    =False,
        widget      =forms.TextInput(attrs={
            'placeholder':'باقي المصاريف',
            'style': 'font-size: 18px;'
            })
        )
    
    class Meta:
            model       = Formstudent
            # fields      = '__all__'
            # fields      = ['firstname','lastname','age','email','message']
            exclude     = ['situation','created-at']
####################################        
# # All Fields Frome Models.py
#     code_number      
#     name             
#     id_number        
#     school_fees      
#     activity         
#     discount         
#     net_expenses     
#     f_installment    
#     f_receipt_number 
#     s_installment    
#     s_receipt_number 
#     th_installment   
#     th_receipt_number
#     remaining_amount 
####################################
# SUPER FUNCTION
    # دا بداية الدالة لكل الاوامر بالاسفل
    def __init__(self, *args, **kwargs):
        super(FormstudentForm, self).__init__(*args, **kwargs)
            # ============ CONTROL PANAL ( Optiona method to control) ============|
            # All Fields 'discount','net_expenses','f_installment','f_receipt_number','s_installment','s_receipt_number','th_installment','th_receipt_number','remaining_amount'
            # 1- input requiered # مطلوب الكتابة ولا يمكن الاستكمال بدونه
        # self.fields['discount'].required = True
    # 3- input ReadOnly # لجعل الحقل للقراءة فقط
        # self.fields['net_expenses'].widget.attrs.update({'readonly':'readonly'})
        # self.fields['remaining_amount'].widget.attrs.update({'readonly':'readonly'})

#############================ EDIT STUDENT TO PAY INSTALLMENT =========############
class Update_StudentForm(forms.ModelForm):
    name       = forms.CharField(label='اسم الطالب', max_length=50, min_length=9)
    net_expenses     = forms.CharField(label='صافي المبلغ', max_length=8, min_length=8, required=False,
        widget      =forms.TextInput(attrs={'placeholder':'الصافي','style': 'font-size: 18px;'}))

    # f_installment number only
    f_installment     = forms.CharField(label='القسط الاول', max_length=5, min_length=4, required=False)

    # f_receipt_number number only
    f_receipt_number     = forms.CharField(label='ايصال القسط الاول', max_length=4, min_length=4, required=False)

    # s_installment number only
    s_installment     = forms.CharField(label='القسط الثاني', max_length=5, min_length=4, required=False)

    # s_receipt_number number only
    s_receipt_number     = forms.CharField(label='ايصال القسط الثاني', max_length=4, min_length=4, required=False)

    # th_installment number only
    th_installment     = forms.CharField(label='القسط الثالث', max_length=5, min_length=4, required=False)

    # th_receipt_number number only
    th_receipt_number     = forms.CharField(label=' ايصال القسط الثالث', max_length=4, min_length  =4, required    =False,
        )

    # th_receipt_number number only
    remaining_amount     = forms.CharField(label=' الباقي ', max_length=8, min_length=1, required=False,
        widget      =forms.TextInput(attrs={'placeholder':'باقي المصاريف','style': 'font-size: 18px;'}))
    
    
    class Meta:
        model                   = Updatestudent
        exclude                 = ['situation','created-at']
        verbose_name            = 'Student Update'
        verbose_name_plural     = 'Student Updates'

# SUPER FUNCTION
    # دا بداية الدالة لكل الاوامر بالاسفل
    def __init__(self, *args, **kwargs):
        super(Update_StudentForm, self).__init__(*args, **kwargs)
            # ============ CONTROL PANAL ( Optiona method to control) ============|
        self.fields['net_expenses'].widget.attrs.update({'readonly':'readonly'})
        self.fields['remaining_amount'].widget.attrs.update({'readonly':'readonly'})    
        
        
    # dont register duplecate id_number
    def clean_id_number(self):
        id_number = self.cleaned_data.get('id_number')
        for obj in Formstudent.objects.all():
            if obj.id_number == id_number:
                raise forms.ValidationError('هذا الرقم' + id_number + 'تم تسجيله من قبل')
        return id_number




