from django.contrib import admin
from form.models import Formstudent
from form.forms import FormstudentForm
from django.utils.html import format_html 
from import_export.admin import ImportExportModelAdmin


# Register your models here.
admin.site.site_header = 'LYS Al-Manar Account system v22.1.0 Admin'

class FormstudentAdmin(ImportExportModelAdmin):  # ImportExportModelAdmin بديله عن   admin.ModelAdmin 
    # radio_fields    = {"smoker": admin.HORIZONTAL} # to convert in admin panel to horizontal
    # form            = FormstudentForm
    exclude         = ['status'] # لإظهار الحالة والتحكم فيها
    readonly_fields = ['name','school_fees','id_number','activity','discount','net_expenses','f_installment','f_receipt_number','s_installment','s_receipt_number','th_installment','th_receipt_number','remaining_amount']# لجعل الحقول للقراءة فقط  
    list_display    = ['name','id_number','created_at','situation','_']
    search_fields   = ['name','id_number','situation',]
    list_filter     = ['situation','name']
    list_per_page   = 10
    

    #  Function to Hide F-name and L-name (when clicking over the candidiate -Rows)
    # def get_fields(self, request, obj = None):
    #     fields  =  super().get_fields(request, obj)
    #     if obj:
    #         fields.remove('firstname')
    #         fields.remove('lastname')
    #     return fields

    # Function to change the Icon

    def _(self, obj):
        if obj.situation == 'Done':
            return True
        elif obj.situation == 'Remaininstallment':
            return None
        else:
            return False
    _.boolean = True

    # Function to color text

    def status(self, obj):
        if obj.situation == 'Done':
            color = '#28a745' # green Color
        elif obj.situation == 'Remaininstallment':
            color = '#fea95e' # orange Color
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.situation)) # تستخدم مع اضافة  format_html
    status.allow_tages = True


admin.site.register(Formstudent,FormstudentAdmin)

# =================================================
