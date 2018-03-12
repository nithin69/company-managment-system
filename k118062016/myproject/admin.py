# vim: set fileencoding=utf-8 :
from django.contrib import admin
from import_export import resources
from myproject.models import *
from myproject.forms import *
from myproject.views import *
from myproject import models, forms
from django import forms
from dal import autocomplete
from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin
from django.contrib.admin import DateFieldListFilter
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

class EmpResource(resources.ModelResource):

    designation =  fields.Field(column_name='designation', attribute='designation', widget=ForeignKeyWidget(PomeManageMasters, 'name'))
    
    class Meta:
        model = PomeEmloyees

class LocationInchargeResource(ModelResource):

    class Meta:
        model = PomeLocationIncharge

class LoansResource(resources.ModelResource):

    pome_employee_id =  fields.Field(column_name='pome_employee_id', attribute='pome_employee_id', widget=ForeignKeyWidget(PomeEmloyees, 'employeno'))

    class Meta:
        model = PomeEmpLoansTransactions


class WashingResource(resources.ModelResource):

    washing_emp =  fields.Field(column_name='washing_emp', attribute='washing_emp', widget=ForeignKeyWidget(PomeEmloyees, 'employeno'))


    class Meta:
        model = PomeWashings



class FineResource(resources.ModelResource):

    emp_id =  fields.Field(column_name='emp_id', attribute='emp_id', widget=ForeignKeyWidget(PomeEmloyees, 'employeno'))
    pot =  fields.Field(column_name='pot', attribute='pot', widget=ForeignKeyWidget(PomeEmloyees, 'employeno'))

    class Meta:
        model = PomeFineDeductions


class PayrollResource(ModelResource):

    class Meta:
        model = PomeAllowanceMaster


class AttendanceResource(resources.ModelResource):

    employee_id =  fields.Field(column_name='employee_id', attribute='employee_id', widget=ForeignKeyWidget(PomeEmloyees, 'employeno'))

    designation =  fields.Field(column_name='designation', attribute='designation', widget=ForeignKeyWidget(PomeManageMasters, 'name'))

    work_order = fields.Field(column_name='work_order', attribute='work_order', widget=ForeignKeyWidget(PomeManageClientsLocations, 'loc_name'))

    class Meta:
        model = PomeEmployeeAttendence


class ClientAttendanceResource(ModelResource):

    class Meta:
        model = PomeClientAttendance



class PomeEmloyeesAdmin(ImportExportModelAdmin):

    list_display = (
        'employeno',
	'joining_date',
	#'dateofjoining',
	
	'firstname',
        #'middlename',
        'lastname',
        #'database_table',
        #'database_table_id',
        #'parentid',
        #'status',
        #'username',
        #'password',
        #'type_id',
        'department',
        #'client_location',
        'location',
        #'first_location',
        'designation',
        #'reporting_auth',
        #'reference_by',
        #'photo',
        
        'shortname',
        
        #'gender',
        #'home_address1',
        #'home_address2',
        #'policestation',
        #'district',
        #'city',
        #'country',
        #'state',
        #'zipcode',
        #'panno',
        #'aadhar',
        #'esic',
        #'epf',
        #'work_phone',
        #'work_phoneext',
        #'home_phone',
        #'mobile',
        #'fax',
        #'work_email',
        #'home_email',
        #'dob',
        #'birthplace',
        #'sin_ssn',
        #'note',
        #'father_name',
        #'father_age',
        #'mother_name',
        #'mother_age',
        #'husband_wife',
        #'husband_wife_age',
        #'issue',
        #'brother',
        #'brother_no',
        #'sister_no',
        #'sister',
        #'years',
        #'school_college',
        #'exam_passed',
        #'subjects',
        #'division',
        
        #'dateofleaving',
        #'parent_occupation',
        #'details_employe',
        #'identification_mark',
        #'arrested_details',
        #'requiring_certificate',
        #'verification_period',
        #'staying_place',
        #'eminent_persons',
        #'eminent_persons2',
        #'added_on',
        #'separation_date',
        #'reason',
        #'separation_status',
        'issue_items',
	'police_verification',
        #'date_time',
        #'alert_status',
        #'sep_date_time',
        #'sept_alert',
        #'reference_paid_status',
        #'separation_net_pay',
        #'separation_paid_amount',
        #'issue_items_count',
        #'pol_ver_time',
        #'pol_ver_remarks',
        #'chest_expanded',
        #'chest_unexpanded',
        #'height',
        #'weight',
        #'caste',
        #'religian',
        #'bike',
        #'dlicence',
        #'dtype',
        #'licence',
        #'prosecuted',
        #'service_code',
        #'service_rank',
        #'service_name',
        #'pre_village',
        #'pre_post',
        #'pre_dist',
        #'pre_policestation',
        #'pre_state',
        #'pre_pincode',
        #'perm_village',
        #'perm_post',
        #'perm_dist',
        #'perm_policestation',
        #'perm_state',
        #'perm_pincode',
        #'coming',
        #'cutting',
        #'approve_bonus',
        #'proof_type',
        #'ot_allowed',
        #'sendsms',
        #'notfield',
        #'emp_sign',
        #'secondlot',
    )
    exclude = ('parentid','database_table', 'database_table_id','years', 'separation_status','employeno','alert_status','secondlot',)
    list_filter = ('joining_date', 'department', 'designation', )
    search_fields = ('firstname','lastname', 'employeno','location',)
    resource_class = EmpResource

class PomeManageClientsLocationsAdmin(admin.ModelAdmin):
  
    form = ManageClientsLocationsForm

    list_display = (
        'loc_name',
        'cid',
        'name',
        
        'address',
        #'parentid',
        #'username',
        #'password',
        'entry_date',
        'from_date',
        'to_date',
        'authorised_person',
        #'panno',
        #'tanno',
        #'auth_designation',
        #'guard_deployement',
        #'email',
        #'telephone',
        #'mobile',
        #'city',
        #'state',
        #'zipcode',
        #'status',
        #'added_on',
        #'login_type',
        #'created',
    )
    exclude = ('parentid','name',)
    list_filter = (
       
        'cid',
    )
    search_fields = ('name','loc_name','cid__client_name')


class PomeTrainerAdmin(admin.ModelAdmin):

    list_display = (
       'trainer_name',
        #'parentid',
        
        'phone',
        'location',
        #'status',
        #'added_on',
    )
    exclude = ('parentid', 'status', 'added_on',)
    #list_filter = ('added_on',)
    search_fields = ('trainer_name',)


class PomeBiodataAdmin(admin.ModelAdmin):
    form = PomeBiodataForm
    list_display = (
       'shortname',
        #'parentid',
        'status',
        #'name',
        #'middle_name',
        #'last_name',
        
        #'gender',
	'trainee_id',
        #'mother_name',
        #'father_name',
        #'brother_name',
        #'sister_name',
        #'fage',
        #'mage',
        #'photo',
        #'chest_expanded',
        #'chest_unexpanded',
        #'height',
        #'weight',
        #'identification_mark',
        #'pre_village',
        #'pre_post',
        #'pre_dist',
        #'pre_policestation',
        #'pre_state',
        #'pre_pincode',
        #'perm_village',
        #'perm_post',
        #'perm_dist',
        #'perm_policestation',
        #'perm_state',
        #'perm_pincode',
        #'dob',
        #'telephone',
        #'caste',
        #'religian',
        'mobile',
        #'bike',
        #'dlicence',
        #'dtype',
        #'licence',
        #'service_code',
        #'service_rank',
        #'service_name',
        #'brother_no',
        #'sister_no',
        #'wife_name',
        #'wife_age',
        #'issue',
        #'year',
        #'school_college',
        'exam_passed',
        #'subjects',
        #'division',
        #'prosecuted',
        #'other_name1',
        #'other_name2',
        #'other_village1',
        #'other_village2',
        #'other_post1',
        #'other_post2',
        #'other_ps1',
        #'other_ps2',
        #'other_dist1',
        #'other_dist2',
        #'other_prof1',
        #'other_prof2',
        #'other_long1',
        #'other_long2',
        #'added_on',
        'post_applied',
        #'interview_with',
        #'remarks',
        #'trainer_name',
        #'location',
        #'training_session',
        'date_time',
	'image',
        #'reference_by',
        #'emp_sign',
        #'email',
    )
    exclude = ('parentid', 'interview_with','emp_sign','trainer_name', 'trainee_id','training_session','location','email',)
    list_filter = ('shortname','status',)
    search_fields = ('shortname','name', 'trainee_id',)

class PomeMastersAdmin(admin.ModelAdmin):

    list_display = (
       'master_name',
        #'parentid',
        
        'master_desc',
        #'status',
        'added_on',
    )
    exclude = ('parentid','status',)
    #list_filter = ('added_on',)
    search_fields = ('master_name',)


class PomeManageMastersAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        #'parentid',
        'master_id',
        'dept_id',
        
        'description',
        #'status',
        'added_on',
    )
    exclude = ('parentid','status',)
    #list_filter = ('added_on',)
    #search_fields = ('name',)
    search_fields = ('master_id','dept_id',)

class PomeTrainingSessionAdmin(admin.ModelAdmin):

    list_display = (
       'session_name',
        #'parentid',
        'status',
        
        'trainer_name',
        'place',
        'session_straingth',
        'total_days',
        'training_dates',
        'added_on',
        'perday_price',
    )
    exclude = ('parentid',)
    list_filter = ('trainer_name', 'added_on')
    search_fields = ('session_name',)


class PomeManageItemsAdmin(admin.ModelAdmin):
    form = ManageitemsForm
    list_display = (
        #'parentid',
	'item_name',
        'item_code',
        'itemtype',
        'category',
        'measurement',
        'threshold_limit',
        'unit_price',
        'charge_price',
        'threshold_to1',
        'days1',
        'threshold_to2',
        'days2',
        'threshold_to3',
        'days3',
        #'status',
        #'added_on',
        #'timestamp',
        #'initiated_by',
        #'stockitem',
    )
    exclude = ('parentid', 'status', 'added_on','item_code', 'timestamp', 'initiated_by', 'stockitem')
    list_filter = ('item_name', )
    search_fields = ('item_name','item_code',)


class PomeManageClientsAdmin(admin.ModelAdmin):
    form = ManageClientsForm
    list_display = (
        'client_name',
        #'parentid',
        #'login_type',
        #'profile_pic',
        #'clientid',
        
        #'client_code_num',
        'client_code',
        #'username',
        #'password',
        #'propreitor',
        #'entry_date',
        #'from_date',
        #'to_date',
        'authorised_person',
        #'auth_designation',
        #'authorised_email',
        #'authorised_phone',
        #'authorised_mobile',
        #'panno',
        #'tanno',
        #'service_tax',
        #'country',
        #'designation',
        #'site_incharge',
        #'guard_deployement',
        #'rate',
        #'client_location',
        #'email',
        'telephone',
        'mobile',
        #'address',
        #'city',
        #'district',
        #'state',
        #'zipcode',
        #'status',
        #'added_on',
        #'stax',
        #'created',
    )
    exclude = ('parentid','profile_pic', 'login_type', 'clientid','client_code_num','client_code', 'created','added_on','auth_designation', 'status','authorised_phone','authorised_mobile', 'site_incharge', 'client_location', 'stax')
    list_filter = (
        'client_name',
    )
    search_fields = ('client_name',)


class PomeAcknowledgementAdmin(admin.ModelAdmin):
    form = PomeAcknowledgeForm
    list_display = (
        u'id',
        #'parentid',
        'emp_id',
        'designation',
        #'emp_id',
        #'emp_name',
        #'emp_code',
        'join_date',
        'receive_date',
        'receive_time',
        #'amount',
        'training_cost',
        'address',
        #'status',
        'document',
        'recept_no',
        'recept_date',
        #'ack_reference_no',
        #'added_on',
    )
    exclude = ('parentid','emp_name', 'emp_code', 'status', 'added_on', 'ack_reference_no','designation',)
    list_filter = ('emp_id',)
    search_fields = ('name','emp_id',)


class PomeAcknowledgementDocumentsAdmin(admin.ModelAdmin):

    list_display = (u'id',
	#'parentid',
	#'ackn_id',
	'upload_documents'
     )
    exclude = ('parentid',)


class PomeCutSalaryAdmin(admin.ModelAdmin):
    form = PomeCutSalaryForm
    list_display = (u'id',
	#'parentid',
	#'ackn_id',
	'employee'
     )
    exclude = ('parentid',)
    search_fields = ('employee',)


class PomeActionsAdmin(admin.ModelAdmin):

    list_display = (u'id', 'name', 'code')
    exclude = ('parentid',)
    search_fields = ('name',)


class PomeAdvancesTypesAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        #'status',
        'loan_type',
        'description',
        #'added_on',
    )
    exclude = ('parentid','status', 'added_on',)
    list_filter = ('added_on',)
    search_fields = ('loan_type',)


class PomeOjtAdmin(admin.ModelAdmin):
    form = OjtForm
    list_display = (
        'ojt_employees',
	'hours', 
	'date',
 	'reason',
    )	

class PomeAllowanceMasterAdmin(ImportExportMixin, admin.ModelAdmin):
    form = StafftypeForm
    list_display = (
        u'id',
        #'parentid',
        'date',
        'employee_id',
        'designation',
        'gross_salary',
        'basic_salary',
        'bonus_val',
        #'loyality_bonus_val',
        #'loyality_bonus_period',
        'bonus_unit',
        'hra_val',
        'hra_unit',
        'others_val',
        'others_unit',
        #'washing_val',
        #'washing_unit',
        'epf_val',
        'epf_unit',
        'epf_emp_val',
        'epf_emp_unit',
        'conveyance_val',
        'conveyance_unit',
        'esi_val',
        'esi_unit',
        'esi_emp_val',
        'esi_emp_unit',
        'percent_basic',
        'value_hra',
        'value_conveyance',
        #'value_washing',
        'value_bonus',
        'value_others',
        'perday_wage',
        'otallowed',
        'ptax_val',
        'ptax_unit',
        'tds_val',
        'tds_unit',
        #'status',
        #'added_on',
    )
    exclude = ('parentid','status', 'added_on', 'designation',  'washing_val','washing_unit','value_washing',)
    list_filter = ('employee_id', 'designation',)
    resource_class = PayrollResource
    search_fields = ('employee_id__employeno',)

class PomeAnnualbonusAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'from_month',
        'to_month',
        'month_eligible',
        'limit_months',
        'percentage',
    )
    exclude = ('parentid',)


class PomeUploadAdmin(admin.ModelAdmin):
    raw_id_fields = ("employee",)
    list_display = (
        u'id',
        'employee',
        'type',
        'upload',
            )


class PomeBillingTaxAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'service_tax',
        'edu_cess',
        'high_edu_cess',
        'swacch_bharat',
        'krish_kalyan',
        'date',
        #'status',
        #'added_on',
    )
    exclude = ('parentid','status', 'added_on', )
    #list_filter = ('date', 'added_on')


class PomeCalendarAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'title',
        'description',
        'start',
        'end',
        'allday',
        'color',
        'url',
        'category',
        'repeat_type',
        'user_id',
        'repeat_id',
    )
    exclude = ('parentid',)
    list_filter = ('start', 'end', 'allday')


class PomeClientBillingAdmin(admin.ModelAdmin):
    form = ClientbillingForm
    list_display = (
        u'id',
        #'parentid',
        #'added_on',
        'client_name',
        'work_order_no',
        'designation',
        'hour',
        #'location',
        'noofpersons',
        'rate',
        #'clientrate',
        #'k1rate',
        'date',
        'todate',
        #'billingperiod',
        'authorised',
        #'status',
        #'supervisor',
        #'alert_status',
        #'date_time',
        #'createdby',
        #'updatedby',
        #'updatetime',
    )
    exclude = ('parentid', 'added_on','updatetime','updatedby', 'location',  'createdby','date_time','alert_status','status','clientrate', 'k1rate', 'supervisor',)
    list_filter = ('client_name', 'work_order_no',)
    search_fields = ('client_name__client_name',)
    


class PomeClientAttendanceAdmin(ImportExportMixin, admin.ModelAdmin):
    form = CleintAttendanceForm
    list_display = (
        u'id',
        #'parentid',
        #'client_id',
        'work_order',
        'employee_id',
        'month',
        'year',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten',
        'eleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eightteen',
        'nineteen',
        'twenty',
        'twentyone',
        'twentytwo',
        'twentythree',
        'twentyfour',
        'twentyfive',
        'twentysix',
        'twentyseven',
        'twentyeight',
        'twentynine',
        'thirty',
        'thirtyone',
        'total_hours',
        #'sessionid',
        #'datetime',
    )
    exclude = ('parentid', 'sessionid', )
    list_filter = ('month','year', 'work_order',)
    resource_class = ClientAttendanceResource
    search_fields = ('work_order','employee_id', )

class PomeClientBranchesAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'client_id',
        'status',
        'branch_name',
        'branch_addr',
        'branch_tele',
        'name',
        'mobile',
        'email',
        'date',
    )
    exclude = ('parentid',)
    list_filter = ('client_id', 'date')
    search_fields = ('name','client_id',)


class PomeClientInvoiceAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'client_id',
        'work_order_no',
        #'parentid',
        #'from_date',
        #'to_date',
        'invoice_date',
        'invoice_no',
        #'invnumber',
        'sub_total',
        #'others',
        'final_total',
        #'stax',
        #'edu_cess',
        #'high_edu_cess',
        #'swacch_bharat',
        #'krish_kalyan',
        'total_amount',
        #'datetime',
        #'sub_total_authorised',
        #'sub_total_additional',
        #'status',
        #'prtstatus',
    )
    exclude = ('parentid','status',)
    list_filter = ('client_id', 'work_order_no', 'invoice_no',)
    search_fields = ('client_id','work_order_no', )

class PomeClientInvoiceTransactionsAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'pome_client_invoice_id',
        'client_id',
        'work_order_no',
        'status_auth',
        'no_of_employees',
        'designation',
        'hours',
        'rate',
        'price',
        'no_of_employees_want',
        'no_of_hours_want',
        'no_of_rate_want',
        'from_date',
        'to_date',
    )
    exclude = ('parentid',)
    list_filter = (
        'pome_client_invoice_id',
        'client_id',
        'work_order_no',
        'designation',
        'from_date',
        'to_date',
    )
    search_fields = ('client_id','work_order_no',)


class PomeClientPatrollingAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'clientid',
        'patrollingno',
        'employeeid',
        'remarks',
    )
    exclude = ('parentid',)
    list_filter = ('clientid', 'employeeid')
    search_fields = ('patrollingno','employeeid',)


class PomeClientPaymentTransactionsAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'invoice_id',
        'date',
        'payment',
        'cqno',
        'cqdate',
        'bank',
        'branch',
        'amount',
        'tds',
        'otherded',
        'reason',
        'work_order_no',
    )
    exclude = ('parentid',)
    list_filter = ('invoice_id', 'date', 'cqdate', 'work_order_no')
    search_fields = ('invoice_id','work_order_no')

class PomeConsultanciesAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'consultancy_name',
        'consultancy_address',
        'consultancy_phoneno',
        'consultancy_emailid',
        'contactperson_name',
        'contactperson_phoneno',
        'contactperson_emailid',
        #'status',
    )
    exclude = ('parentid','status',)
    search_fields = ('consultancy_name',)

class PomeCustomerFeedbackAdmin(admin.ModelAdmin):
    
    list_display = (
        u'id',
        #'parentid',
        #'status',
        'customer_id',
        #'customer_name',
        #'customer_address',
        #'city',
        #'state',
        #'incharge_perform',
        #'guard_perform',
        #'dressup_rate',
        #'record_communicate',
        #'head_office_staff',
        #'daily_report',
        #'night_patrolling',
        'service_quality',
        'lodged_compt',
        'complaint',
        'improvement',
        #'remarks',
        'date',
        'work_order_no',
	'customer_feedback',
    )
    exclude = ('parentid','customer_name','customer_address', 'city', 'state', )
    list_filter = ('service_quality', 'lodged_compt', 'date')
    search_fields = ('customer_id','work_order_no',)

class PomeDefaultAccessAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'permission_id',
        'menu_id',
        'sub_menu_id',
        'added_on',
    )
    exclude = ('parentid',)
    list_filter = ('added_on',)


class PomeDefaultAdvancesAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'name',
        'amount',
        'description',
        'installment_no',
        #'datetime',
        'first_slot',
        'second_slot',
        #'first_slot_installment',
        #'second_slot_installment',
    )
    exclude = ('parentid','first_slot_installment','second_slot_installment','datetime', )
    #list_filter = ('datetime',)
    search_fields = ('name',)


class PomeDisciplineComplianceAdmin(admin.ModelAdmin):
    form = PomeDisciplineForm
    list_display = (
        u'id',
        #'parentid',
        #'group_id',
        'initiated_by',
        #'send_date',
        #'send_time',
        'subject',
        'description',
        'send_to',
        'priority',
	'penality_amount',
        #'alert_status',
        #'date_time',
    )
    exclude = ('parentid','group_id','alert_status','date_time',)
    #list_filter = ('initiated_by', 'send_date', 'date_time')
    search_fields = ('initiated_by',)

class PomeDonationAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        #'status',
        'donation_date',
        'donation_to',
        'address',
        'mobile',
        'email',
        #'payment_method',
        #'cheque_no',
        #'cheque_date',
        #'bank_name',
        #'branch_name',
        'amount',
        'description',
    )
    exclude = ('parentid','status', )
    list_filter = ('donation_date',)
    search_fields = ('donation_to','donation_date')


class PomeEmpAdvancesAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'status',
        'emp_id',
        'name',
        'code',
        'designation',
        'month',
        'opening_balance',
        'issued_adv1',
        'issued_adv2',
        'deduct_adv1',
        'deduct_adv2',
        'closing_balance',
    )
    exclude = ('parentid',)
    #list_filter = ('emp_id',)
    search_fields = ('name',)


class PomeEmpLoansAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        #'status',
        #'type',
        'apply_date',
        'start_date',
        #'end_date',
        'loan_type',
        'emp_id',
        'designation',
        'loan_amount',
        #'reason',
        #'int_apli',
        #'interest',
        #'amount_with_interest',
        'instalment_no',
        'instalment_amount',
        'approval',
        'approved_by',
        'approved_on',
        #'default_advance_id',
        #'training_cost_type',
    )
    exclude = ('parentid',)
    list_filter = ('apply_date', 'start_date', 'end_date', 'approved_on')
    search_fields = ('emp_id',)

class PomeEmpLoansTransactionsAdmin(ImportExportModelAdmin):

    list_display = (
        u'id',
        'pome_employee_id',
        'pome_emp_loans_id',
        'type',
        'date',
        'instalment_amount',
        'status',
        #'approve_status',
        #'view_status',
    )
    exclude = ('parentid',)
    list_filter = ('date',)
    search_fields = ('pome_employee_id__employeno',)
    resource_class = LoansResource

class PomeSeparationsAdmin(admin.ModelAdmin):
    raw_id_fields = ("employees_id",)
    list_display = (
        u'id',
        'separation_date',
        'employees_id',
        'designation',
        'joining_date',
        'vintage',
        'separation_type',
        'reason',
    )
    search_fields = ('employees_id',)

class PomeStaffTypeAdmin(admin.ModelAdmin):
    form = StafftypeForm
    list_display = (
        u'id',
        'employee_id',
        'emp_type',
    )
    search_fields = ('employee_id',)



class PomeEmployeeAttendenceAdmin(ImportExportModelAdmin):
    form = PomeAttendenceForm
    raw_id_fields = ("work_order",)
    list_display = (
        u'id',
        'employee_id',
        'designation',
        'pome_leaves_absents_id',
        'applied_for',
        'date',
        'month_year',
        'status',
        'work_order',
        'actual_hours',
        'hours',
        'minutes',
        'remarks',
        'locations_id',
        'datetime',
        'entered',
    )
    exclude = ('parentid',)
    list_filter = ('employee_id', 'work_order', 'date')
    resource_class = AttendanceResource
    search_fields = ('employee_id__employeno','work_order__loc_name',)


class PomeEmployeeCtcAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'status',
        'ctc_name',
        'ctc_amount',
        'date',
    )
    exclude = ('parentid',)
    list_filter = ('date',)


class PomeEmployeeExpenditureAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'acc_type',
        'status',
        'account_id',
        'auth_person',
        'emp_name',
        'designation',
        'expenditure_name',
        'purpose',
        'expenditure_amount',
        'expenditure_date',
        'upload',
        'reference_no',
        'approver',
        'approved_by',
    )
    exclude = ('parentid',)
    list_filter = ('emp_name', 'designation', 'expenditure_date')


class PomeEmployeeMovementAdmin(admin.ModelAdmin):
    form = PomeEmployeeMovementForm
    raw_id_fields = ("order_by","gmo",)
    list_display = (
        u'id',
        #'parentid',
        #'client_id',
        #'hours',
        'work_order',
        #'auto_work_order_no',
        #'order_number',
        'emp_name',
        'designation',
        #'order_by',
        #'order_designation',
        #'order_date',
        #'order_time',
        'from_date',
        'to_date',
        #'from_time',
        #'to_time',
        #'reason',
        'emp_status',
        'job_status',
        #'gmo',
        #'exc_site',
        #'old_site',
        #'allowance',
        #'reach_update',
        #'alert_status',
        #'remarks',
        #'reporting_date',
        #'reporting_time',
        #'status',
    )
    exclude = ('parentid', 'designation', 'exc_site','old_site', 'alert_status', 'status', 'reach_update', 'order_designation','allowance', 'auto_work_order_no')
    list_filter = (
        'client_id',
        'work_order',
        'emp_name',
        'designation',
        'reporting_date',
    )
    search_fields = ('emp_name__employeno','work_order__loc_name',)


class PomeEmployeePostingAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'status',
        'emp_id',
        'emp_name',
        'emp_code',
        'designation',
        'moveto_client',
        'client_branch',
        'location',
        'order_by',
        'order_date',
        'from_date',
        'to_date',
        'reason',
        'emp_status',
        'added_on',
    )
    exclude = ('parentid',)
    list_filter = (
        'emp_id',
        'designation',
        'order_date',
        'from_date',
        'to_date',
        'added_on',
    )
    search_fields = ('emp_id','designation',)


class PomeEmployeeSeparationsAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'pome_employees_id',
        'separation_net_pay',
        'total_earnings',
        #'epf_esi',
        #'adp',
        #'ldp',
        #'other_deductions',
        #'sub_total',
        #'mess',
        #'total_amount',
        #'message',
        #'training_cost',
        #'others_recovery',
        #'acknowledge',
        #'separation_paid_amount',
        #'payment_type',
        #'cqno',
        #'cqdate',
        #'bank',
        #'branch',
        #'online_type',
        #'reference_number',
        #'datetime',
    )
    exclude = ('parentid',)
    list_filter = ( 'pome_employees_id', 'datetime')
    search_fields = ('pome_employees_id',)

class PomeEmployeeSettlementAdmin(admin.ModelAdmin):
    form = EmployeesettlementForm
    list_display = (
        u'id',
        #'parentid',
        #'status',
        'emp_id',
        #'emp_name',
        #'emp_code',
        'designation',
        'settlement_amt',
        'paid_amount',
        'balance_amount',
        'settlement_status',
        #'added_on',
    )
    exclude = ('parentid','emp_name', 'emp_code', )
    #list_filter = ('emp_id', 'designation', 'added_on')
    search_fields = ('emp_id',)

class PomeEodManagementAdmin(admin.ModelAdmin):
    form = EODManagementForm
    list_display = (
        u'id',
        #'parentid',
        'eod_subject',
        'eod_data',
        'eod_by',
        #'status',
        'sended_on',
    )
    exclude = ('parentid','status',)
    list_filter = ('eod_by', 'sended_on')
    search_fields = ('eod_by',)

class PomeEodForwardAdmin(admin.ModelAdmin):

    list_display = (u'id',
	#'parentid',
	'eod_id',
	'remarks',
	'forward_to')
    exclude = ('parentid',)
    list_filter = ('eod_id', 'forward_to')
    search_fields = ('eod_id',)

class PomeExcessAttendanceAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'employee_id',
        'work_order',
        'day_balance',
        'rota_entry',
        'entered',
        'date',
        'date_entered',
    )
    exclude = ('parentid',)
    list_filter = ('employee_id', 'work_order', 'date', 'date_entered')
    search_fields = ('employee_id','work_order',)

class PomeExcessLocAttendanceAdmin(admin.ModelAdmin):
    raw_id_fields = ("employee_id","work_order", "entered",)
    list_display = (
        u'id',
        'employee_id',
        'work_order',
        'day_balance',
        'rota_entry',
        'entered',
        'date',
        'date_entered',
    )
    exclude = ('parentid',)
    list_filter = ('employee_id', 'work_order', 'date', 'date_entered')
    search_fields = ('employee_id','work_order',)

class PomeFinalReportAdmin(admin.ModelAdmin):
    form = PomeFinalreportForm
    list_display = (
        u'id',
        #'parentid',
        'biodata_id',
        'attire',
        'punctuality',
        'behaviour',
        'tabacco',
        'command',
        'drill',
        'recom',
        'remarks',
        'added_on',
    )
    exclude = ('parentid',)
    list_filter = ('biodata_id',)
    search_fields = ('biodata_id',)

class PomeFineAdmin(admin.ModelAdmin):

    list_display = (u'id',
    	'name',
	'link',
	'amount')
    exclude = ('parentid',)
    search_fields = ('name',)


class PomeFineDeductionsAdmin(ImportExportModelAdmin):
    form = FineForm
    list_display = (
        u'id',
        #'parentid',
        'apply_date',
        'month',
        'year',
        'emp_id',
        'amount',
        'selc_fine_ids',
        #'others',
        #'pot',
        #'datetime',
    )
    exclude = ('parentid',)
    list_filter = ('apply_date', 'emp_id', 'selc_fine_ids', 'datetime')
    search_fields = ('emp_id',)
    resource_class = FineResource



class PomeGalleryAdmin(admin.ModelAdmin):

    list_display = (u'id',
    	#'parentid',
	#'gallery_type',
	'image',
	#'added_on'
    )
    exclude = ('parentid','gallery_type', 'added_on',)
    #list_filter = ('added_on',)


class PomeGatepassAdmin(admin.ModelAdmin):
   
    form = PomeGatepassForm
    #raw_id_fields = ("issuedby", "emp_name")
    list_display = (
        'gatepass_no',
        #'parentid',
        #'gatepass_type',
        'out_date',
        'out_time',
        'in_date',
        'in_time',
        'gateno',
        'purpose',
        'emp_name',
        #'emp_code',
        
        #'gpnumber',
        #'approver',
        'issuedby',
        #'stock_to',
        #'srno',
        #'particulars',
        #'quantity',
        #'inventoryno',
        #'location',
        'designation',
        #'department',
        #'splinstruction',
        #'update_remarks',
        #'status',
        #'date_time',
        #'first_emp',
        #'cancel_remarks',
    )
    
    exclude = ('parentid','gatepass_type','designation', 'gpnumber','srno','particulars', 'quantity','gatepass_no', 'inventoryno', 'location', 'department', 'update_remarks', 'status', 'date_time', 'first_emp', 'cancel_remarks', 'stock_to', 'emp_code', 'approver', )
    list_filter = ('out_date', 'in_date')
    search_fields = ('gatepass_no',)

class PomeGraderateSettingAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'grade_name',
        'rate',
        'date',
        'status',
        'added_on',
    )
    exclude = ('parentid',)
    list_filter = ('date', 'added_on')
    

class PomeGuardPlacementAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'client_name',
        'location',
        'designation',
        'emp_id',
        'employe_name',
        'status',
        'post_from',
        'post_to',
        'added_on',
    )
    exclude = ('parentid',)
    list_filter = (
        'client_name',
        'designation',
        'emp_id',
        'post_from',
        'post_to',
        'added_on',
    )
    
    search_fields = ('employee_name','client_name')

class PomeHolidaysAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'name',
        'date',
        'remarks',
        'holiday',
        #'status',
    )
    exclude = ('parentid','status',)
    #list_filter = ('date',)
    #search_fields = ('name',)


class PomeIncentiveAdmin(admin.ModelAdmin):
    form = PomeIncentiveForm
    list_display = (
        u'id',
        #'parentid',
        'designation',
        'amount',
        'date',
        #'status',
        #'added_on',
        'purpose',
        'totamount',
        #'generated_id',
    )
    exclude = ('parentid','status', 'added_on', 'generated_id',)
    list_filter = ('designation',)


class PomeIncentiveLocAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'location',
        'amount',
        'purpose',
        'totamount',
        'date',
        'status',
        'added_on',
        'generated_id',
    )
    exclude = ('parentid','status', 'generated_id','added_on',)
    list_filter = ('date',)


class PomeInnermenusAdmin(admin.ModelAdmin):

    list_display = (u'id', 'submenu_id', 'name', 'link', 'is_active')
    exclude = ('parentid',)
    search_fields = ('name',)


class PomeManageStoresAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'store_name',
        'address',
        'contact_no',
        'name',
        'designation',
        'mobile',
        'email',
        #'status',
        #'added_on',
    )
    exclude = ('parentid', 'status', 'added_on',)
    list_filter = ('store_name',)
    search_fields = ('store_name',)


class PomeVendorWorkshopAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'login_type',
        #'profile_pic',
        #'parentid',
        'type',
        'company_vendor_name',
        #'username',
        #'password',
        'vendor_code',
        #'registration_no',
        'company_type',
        #'agreement_date',
        #'purpose',
        #'regd_office_addr',
        'city',
        'district',
        'state',
        'country',
        #'pin_code',
        #'company_email',
        #'company_telephone',
        #'fax',
        #'amc_period',
        #'tin_tan',
        #'service_tax',
        'bank_details',
        'bank',
        'ac_no',
        'ifsc_no',
        'branch',
        #'bank_type',
        #'name',
        #'pan_no',
        #'designation',
        #'email',
        #'contact_no',
        #'mobile',
        #'status',
        #'added_on',
    )
    exclude = ('parentid','profile_pic','login_type', 'purpose', 'status','added_on',)
    list_filter = ('company_vendor_name',)
    search_fields = ('name',)


class PomeInvoicePaymentDeleteAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'invoice_id',
        'date',
        'payment',
        'cqno',
        'cqdate',
        'bank',
        'branch',
        'amount',
        'tds',
        'otherded',
        'reason',
        'entered',
        'datetime',
    )
    exclude = ('parentid',)
    list_filter = ('invoice_id', 'date', 'cqdate', 'datetime')
    search_fields = ('invoice_id',)

class PomeInwardInvoiceAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'status',
        'date',
        'invoice_no',
        'vendor_id',
        'total_amount',
        'paid_amount',
        'datetime',
    )
    exclude = ('parentid',)
    list_filter = ('date', 'invoice_no', 'vendor_id', 'datetime')
    search_fields = ('invoice_no',)

class PomeInwardAdmin(admin.ModelAdmin):
    form = PomeInwardForm
    raw_id_fields = ("invoice_no",)
    list_display = (
        u'id',
        #'pome_inward_invoice_id',
        #'status',
        #'pome_purchase_requisition_id',
        #'pome_inward_id',
        #'parentid',
        #'date',
        #'to',
        'invoice_no',
        'vendor_id',
        #'store_id',
        'items',
        'ordered',
        'received',
        #'price',
        #'total_amount',
        #'paid_amount',
        'exceed',
        'remarks',
        'courier_type',
        #'courier_name',
        #'pod_number',
        #'driver_number_plate',
        #'driver_name',
        #'driver_contact',
        #'per_name',
        #'per_contact',
        'received_by',
        #'datetime',
        #'inward_type',
        #'alert_status',
    )
    exclude = ('parentid','pome_inward_invoice_id','pome_inward_id', 'pome_purchase_requisition_id','date_time', 'inward_type', 'alert_status', 'exceed', )
    list_filter = (
        'date',
        'to',
        'courier_type',)
    search_fields = ('invoice_no',)


class PomeInwardDocumentsAdmin(admin.ModelAdmin):

    list_display = (u'id',
	#'parentid',
	'inward_id',
	'upload_documents'
    )
    exclude = ('parentid',)
    list_filter = ('inward_id',)


class PomeInwardOutwardCourierAdmin(admin.ModelAdmin):

    list_display = (
        'guid',
        #'parentid',
        'type',
        'date',
        'from_field',
        'to',
        'courier_type',
        'courier_name',
        'pod_number',
        'received_by',
        'dateandtime_delivery',
        'courier_particulars',
        'remarks',
        'date_added',
    )
    exclude = ('parentid',)
    list_filter = ('date', 'dateandtime_delivery', 'date_added')


class PomeInwardOutwardFixedAssetsAdmin(admin.ModelAdmin):

    list_display = (
        'guid',
        #'parentid',
        'type',
        'fixed_date',
        'fixed_visitor_name',
        'fixed_from',
        'fixed_contact',
        'fixed_email',
        'fixed_whom',
        'fixed_purpose',
        'fixed_issued_entry_pass',
        'fixed_issued_ppe',
        'date_added',
    )
    exclude = ('parentid',)
    list_filter = ('fixed_date', 'date_added')


class PomeInwardOutwardMaterialAdmin(admin.ModelAdmin):

    list_display = (
        'guid',
        #'parentid',
        'type',
        'receipts_date',
        'receipts_invoice_number',
        'receipts_received_from',
        'receipts_quantity',
        'receipts_cumulative',
        'receipts_remarks',
        'issues_date',
        'issues_requisition_no',
        'issues_issued_to',
        'issues_quantity',
        'issues_cumulative',
        'issues_remarks',
        'net_balance',
        'date_added',
    )
    exclude = ('parentid',)
    list_filter = ('receipts_date', 'issues_date', 'date_added')


class PomeIssuanceAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'emp_name',
        'emp_username',
        'emp_code',
        'join_date',
        'department',
        'location',
        'supervisor',
        'issuance_date',
        'items',
        'quantity',
        'value',
        'remarks',
        'status',
        'added_on',
    )
    exclude = ('parentid',)
    list_filter = ('emp_name', 'department', 'items', 'added_on')
    search_fields = ('emp_name',)

class PomeItemDesignationwiseAdmin(admin.ModelAdmin):
    form = PomeDesignationIncentiveForm
    list_display = (
        u'id',
        #'parentid',
        'designation_id',
        'items_id',
        'second',
        #'added_on',
    )
    exclude = ('parentid',)
    list_filter = ('designation_id',)
    search_fields = ('items_id',)


class PomeItemRequisitionAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'type',
        #'parentid',
        'issuance_type',
        'pome_emloyees_id',
        #'discount',
        #'discountval',
        #'emp_name',
        #'emp_code',
        'department',
        'designation',
        #'location',
        #'supervisor',
        'request_date',
        'items',
        'unit_price',
        'quantity',
        #'value',
        'remarks',
        #'reason',
        'approver',
        'approve_date',
        'store_id',
        #'status',
        #'stores_status',
        #'returned',
        #'remaining',
        #'designationwise',
        #'penality_amount',
        #'returned_date',
        #'timestamp',
    )
    exclude = ('parentid', 'discount','discountval','emp_name','emp_code','location','status','stores_status','timestamp',)
    list_filter = ('type', 'issuance_type')
    search_fields = ('pome_emloyees_id',)

class PomeK1DetailsAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'st_no',
        'pan_no',
        'epf_no',
        'esi_no',
        'cin_no',
        'company_name',
        'address',
        'phone',
        'fax',
        'email',
        'invioce_no',
        'service_tax',
        'edu_cess',
        'high_edu_cess',
        'condition1',
        'condition2',
        'condition3',
        'condition4',
        'condition5',
    )
    exclude = ('parentid',)

class PomeLeaveManagementAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'leave_name',
        'leave_code',
        'payment',
        'noofleaves',
        'emp_apply',
        'emp_beyond',
        'leavetype',
        'percentage',
        'stop_period',
        #'status',
    )
    exclude = ('parentid','status',)
    search_fields = ('leave_name',)

class PomeLeavePeriodAdmin(admin.ModelAdmin):
    form = LeaveperiodForm
    list_display = (
        u'id',
        #'parentid',
        'from_date',
        'to_date',
        #'status',
        #'timestamp',
    )
    exclude = ('parentid','status', 'timestamp',)
    #list_filter = ('from_date', 'to_date', 'timestamp')


class PomeLeavesAbsentsAdmin(admin.ModelAdmin):
    form = PomeLeavesForm
    list_display = (
        u'id',
        #'parentid',
        'status',
        'name',
        'date',
        #'father_name',
        'designation',
        'applied_for',
        'applied_month',
        'from_date',
        'to_date',
        'reason_for',
        #'send_to',
        #'contact_at',
        #'contact_po',
        #'contact_dist',
        #'contact_phone',
        #'date_time',
    )
    exclude = ('parentid', 'father_name', 'send_to', 'date_time')
    list_filter = (
        
        'designation',
        'status',
        'name',
    )
    search_fields = ('name',)


class PomeLoanTypesAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        #'status',
        'loan_type',
        'description',
        #'added_on',
        #'type',
    )
    exclude = ('parentid','status', 'added_on', 'type',)
    #list_filter = ('added_on',)
    search_fields = ('loan_tyoe',)

class PomeLoansAdvancesAdmin(admin.ModelAdmin):
    form = LoanadvanceForm
    list_display = (
        u'id',
        #'parentid',
        #'status',
        'designation',
        'loan_limit',
        #'added_on',
    )
    exclude = ('parentid','status', 'added_on', )
    #list_filter = ('designation', 'added_on')


class PomeLoansCalculationAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'emp_id',
        'loan_id',
        'loan_type',
        'loan_amount',
        'inst_month',
        'inst_no',
        'inst_paid',
        'inst_amount',
        'balance',
        'added_on',
    )
    exclude = ('parentid',)
    list_filter = ('emp_id', 'added_on')
    search_fields = ('emp_id',)

class PomeLocDesgMasterAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'date',
        'designation',
        'basic',
        'hra',
        'conveyance',
        'others',
        'epf',
        'esi',
        'perday_wage',
        'status',
        'added_on',
    )
    exclude = ('parentid',)
    list_filter = ('date', 'designation', 'added_on')
    

class PomeLocationIncentiveAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'location',
        #'amount',
        #'date',
        #'status',
        #'added_on',
    )
    exclude = ('parentid','amount', 'date', 'status', 'added_on',)
    #list_filter = ('added_on',)


class PomeLocationInchargeAdmin(ImportExportMixin, admin.ModelAdmin):
    form = LocationinchargeForm
    list_display = (
        u'id',
        #'parentid',
        'client_id',
        'work_order',
        'employee_id',
        #'status',
        #'datetime',
    )
    exclude = ('parentid','status','datetime', )
    list_filter = ('employee_id','work_order',)
    resource_class = LocationInchargeResource
    search_fields = ('client_id__client_name','employee_id__employeno',)

class PomeLocationInchargeSalariesAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'emp_id',
        'month',
        'year',
        'total_amount',
        'thousands',
        'fivehundreds',
        'hundreds',
        'fifties',
        'twenties',
        'tens',
        'fives',
        'twos',
        'ones',
        'generated_id',
        'datetime',
    )
    exclude = ('parentid',)
    list_filter = ('emp_id', 'datetime')
    search_fields = ('emp_id',)

class PomeLocationsalarySettingsAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'designation',
        'clientid',
        'work_order',
        'amount',
        'status',
        'datetime',
    )
    exclude = ('parentid',)
    list_filter = ('clientid', 'work_order', 'datetime')
    search_fields = ('work_order',)

class PomeLocdesgAdmin(admin.ModelAdmin):

    list_display = (u'id', 'designation', 'desg_id', 'status')
    exclude = ('parentid',)


class PomeLocpayIncentiveAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'work_order',
        'designation',
        'perday',
        'date',
        'status',
        'added_on',
        'generated_id',
    )
    exclude = ('parentid',)
    list_filter = ('work_order', 'designation', 'date', 'added_on')
    search_fields = ('work_order',)

class PomeLoginDetailsAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'name',
        'send_to',
        'subject',
        'messages',
        'added_on',
    )
    exclude = ('parentid',)
    list_filter = ('added_on',)
    search_fields = ('name',)


class PomeLoginsAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'username',
        'password',
        'type',
        'pome_emloyees_id',
        'datetime',
    )
    exclude = ('parentid',)
    list_filter = ('datetime',)

class PomeLoyalityBonousAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'loyality_bonous',
        'loyality_period',
        'description',
        'date',
    )
    exclude = ('parentid',)
    #list_filter = ('date',)


class PomeManageDepartmentsAdmin(admin.ModelAdmin):

    list_display = (u'id', 'name', 'datetime')
    exclude = ('parentid',)
    list_filter = ('datetime',)
    search_fields = ('name',)


class PomeManageQuotationAdmin(admin.ModelAdmin):
    form = QuotationForm
    list_display = (
        u'id',
        #'parentid',
        #'status',
        'client',
        #'branch',
        #'subject',
        'designation',
        'work_order_no',
        'authorised',
        'additional',
        'date',
    )
    exclude = ('parentid', 'status', 'branch')
    list_filter = ('date','client',)
    search_fields = ('client__client_name',)


class PomeMenusAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'name',
        'link',
        'icon',
        'is_active',
        'sub_menu',
        'actions_id',
        'inner_menu',
        'sub_menu_id',
        'menu_id',
        'employee',
    )
    exclude = ('parentid',)
    search_fields = ('name',)
    

class PomeMobilePatrollingAdmin(admin.ModelAdmin):
    form = PatrollingForm
    list_display = (
        u'id',
        #'parentid',
        #'status',
        'patrolling_person',
        'date',
        'clientid',
        'employeeid',
        #'mobile',
        #'time1',
        #'time2',
        #'time3',
        #'time4',
        #'time5',
        #'time6',
        #'time7',
        #'call_1',
        #'call_2',
        #'call_3',
        #'call_4',
        #'call_5',
        #'call_6',
        #'call_7',
	'mobile_patrolling',
    )
    exclude = ('parentid','status', 'mobile')
    list_filter = ('date', 'clientid', 'employeeid')
    search_fields = ('employeeid',)

class PomeMoneytransferPettycashAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'status',
        'date',
        'petty_account',
        'amount',
        'approver',
        'approved_by',
        'approved_on',
    )
    exclude = ('parentid',)
    list_filter = ('date', 'approved_on')


class PomeNoticeboardAdmin(admin.ModelAdmin):
    form = NoticeBoardForm
    list_display = (
        u'id',
        #'parentid',
        'date',
        'subject',
        'message',
        'post_to',
        #'post_count',
        'priority',
        'from_date',
        'to_date',
        'notice_type',
        #'alert_status',
        'date_time',
        'send_by',
        #'status',
    )
    exclude = ('parentid','status', 'alert_status',)
    list_filter = ('date', 'from_date', 'to_date', 'date_time')
    search_fields = ('post_to',)

class PomeNotificationsAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'notification',
        'type',
        'status',
        'added_on',
    )
    exclude = ('parentid',)
    list_filter = ('added_on',)


class PomeOtherBenefitsAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'status',
        'benefit_name',
        'amount',
        'added_on',
    )
    exclude = ('parentid',)
    list_filter = ('added_on',)


class PomeOutwardAdmin(admin.ModelAdmin):
	
    form = PomeOutwardForm
    list_display = (
        u'id',
        #'parentid',
        #'status',
        'date',
        #'time',
        'gatepass_no',
        'invoice_no',
        'stock_to',
        'type',
        #'courier_name',
        #'pod_number',
        #'number_plate',
        #'driver_name',
        #'driver_contact',
        #'per_name',
        'approver',
        'ref_nonref',
        'items',
        'quantity',
        'value',
        'reason',
        'remarks',
        #'approve',
        #'date_time',
        #'alert_status',
    )
    exclude = ('parentid','status','gatepass_no', 'approve','date_time','alert_status',)
    list_filter = ('date', 'ref_nonref')
    search_fields = ('gatepass_no',)


class PomeOvertimeAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'pome_emloyees_id',
        'designation',
        'total_hours_ot',
        'total_hours',
        'absent_count',
        'month',
        'year',
        'total_days',
        'leave_count',
        'overtime_hours',
        #'own_ot',
        #'inctot',
        'tots',
        'work_order',
        #'generated_id',
    )
    exclude = ('parentid','own_ot', 'inctot', 'generated_id', )
    list_filter = ('pome_emloyees_id','designation','month', 'year', )
    search_fields = ('pome_emloyees_id',)

class PomeOvertimeGeneratedAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'month',
        'year',
        'page',
        'page_limit',
        'page_current_limit',
    )
    exclude = ('parentid',)

class PomeOvertimePaymentAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'ot_id',
        'employee_id',
        'date',
        'payment',
        'cqno',
        'cqdate',
        'bank',
        'branch',
        'amount',
        'voucherno',
        'status',
    )
    exclude = ('parentid',)
    list_filter = ('date', 'cqdate')
    search_fields = ('employee_id',)


class PomePatrollingAdmin(admin.ModelAdmin):
    form = PomePatrollingForm
    list_display = (
        u'id',
        #'parentid',
        'status',
        'patrolling_officer',
        'patrolling_officer2',
        'patrolling_time',
        'name',
        'code',
        #'dress_up',
        #'wear_belt',
        #'wear_tie',
        #'wear_shoes',
        #'b_polish',
        #'cap_batch',
        #'wear_cap',
        #'wear_whistle',
        #'wear_saving',
        #'wear_haircut',
        #'sleeping',
        #'post_out',
        #'wear_icard',
        #'wear_socks',
        #'dozzing',
        #'tabaco',
        'date',
        'loc_assign',
        'single_patrolling',
	'deduction_amount',	 
    )
    exclude = ('parentid','status', 'code')
    list_filter = ('date',)
    search_fields = ('name',)


class PomePattycashAccountsAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'status',
        'account_name',
        'description',
        'auth_person',
        'added_on',
    )
    exclude = ('parentid',)
    list_filter = ('added_on',)


class PomePaymentAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'client_name',
        'branch_name',
        'payment_date',
        'work_order',
        'amount',
        'payment_type',
        'payment_status',
        'status',
        #'added_on',
    )
    exclude = ('parentid',)
    list_filter = ('client_name', 'payment_date', 'added_on')
    search_fields = ('client_name',)


class PomePaymentCollectionAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'company_id',
        'type',
        'company_name',
        'date',
        'work_order',
        'amount',
        'payment_type',
        'payment_status',
        #'cqno',
        #'cqdate',
        #'bank',
        #'branch',
        #'status',
        #'added_on',
    )
    exclude = ('parentid','status', 'added_on', )
    list_filter = ('company_id', 'date',)
    search_fields = ('company_name',)

class PomePaymentReceiptInchargeAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'prepared_by',
        'achead',
        'paidby',
        'receivedby',
        'salary',
        'incentive',
        'barekrent',
        'others',
        'subtotal',
        'advance',
        'balance',
        'month',
        'year',
        #'thousands',
        #'fivehundreds',
        #'hundreds',
        #'fifties',
        #'twenties',
        #'tens',
        #'fives',
        #'twos',
        #'ones',
        #'datetime',
        'siteincharge',
        #'status',
        #'remarks',
        'final_amount',
    )
    exclude = ('parentid','thousands', 'fivehundreds', 'hundreds', 'fifties', 'twenties','tens', 'fives', 'twos', 'ones', 'datetime', 'remarks')
    list_filter = ('status','siteincharge', )
    search_fields = ('prepared_by',)

class PomePaymentsTransfersAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'database_table',
        'database_table_id',
        'vendor_id',
        'paid_amount',
        'invoice_number',
        'payment_type',
        'cqno',
        'cqdate',
        'bank',
        'branch',
        'online_type',
        'reference_number',
        'datetime',
    )
    exclude = ('parentid',)
    list_filter = ('vendor_id', 'cqdate', 'datetime')
    search_fields = ('vendor_id',)

class PomePayscaleSettingAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'status',
        'designation',
        'below_salary',
        'full_salary',
        'date',
    )
    exclude = ('parentid',)
    list_filter = ('designation', 'date')


class PomePoliceVerificationFormAdmin(admin.ModelAdmin):

    list_display = (
        #'guid',
        #'parentid',
        'full_name',
        #'father_name',
        #'present_address',
        #'permanent_address',
        #'residence_no',
        #'office_no',
        'mobile_no',
        #'date_of_birth',
        #'place_of_birth',
        #'family_father',
        #'family_mother',
        #'family_husband',
        #'family_brother',
        #'family_sister',
        #'parent_occupation',
        'fullname_of_the_employer',
        #'identification_mark',
        #'arrested',
        #'purpose_for_requiring',
        #'period_of_verification',
        #'place_of_stay',
        #'locality_verification',
        #'date_added',
    )
    exclude = ('parentid',)
    list_filter = ('date_of_birth',)
    search_fields = ('full_name',)

class PomePurchaseOrderAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'store_id',
        'item_name',
        'vendor',
        'item_price',
        'quantity',
        'refno',
        'status',
        'date',
        'delivery_date',
        'delivery_mode',
        'payment_mode',
        'credit_days',
        'payment_type',
        'discount',
        'initiated_by',
        'approved_by',
        'added_on',
    )
    exclude = ('parentid', 'status', 'added_on')
    list_filter = (
        'store_id',
        'item_name',
        'vendor',
        'date',
        'delivery_date',
        'initiated_by',
        'added_on',
    )
    search_fields = ('item_name','store_id',)

class PomePurchaseRequisitionAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        #'status',
        #'added_on',
        'store_id',
        'vendor',
        #'orderno',
        #'orderno_value',
        'initiated_by',
        'items',
        'price',
        'quantity',
        'value',
        'remarks',
        'approved_by',
        'approved_on',
        #'info1',
        #'day1',
        #'info2',
        #'day2',
        #'info3',
        #'day3',
        #'timestamp',
        #'clarify',
        #'answer',
    )
    exclude = ('parentid' ,'orderno','status', 'orderno_value', 'approved_by', 'approved_on','info1','day1', 'info2','day2', 'info3','day3', 'timestamp',)
    list_filter = ('added_on', 'store_id','vendor','items',)
    search_fields = ('vendor','store_id',)


class PomeReferenceIncentiveAdmin(admin.ModelAdmin):

    list_display = (u'id',
    	#'parentid',
	#'status',
	'date',
	'amount')
    #list_filter = ('date',)
    exclude = ('parentid','status',)


class PomeReferencePaymentAdmin(admin.ModelAdmin):
    form = ReferencepaymentForm
    list_display = (
        u'id',
        #'parentid',
        'reference_id',
        'emp_id',
        'amount',
        #'status',
        #'month_year',
        'date',
    )
    exclude = ('parentid', 'month_year')
    list_filter = ('reference_id', 'emp_id', 'date')
    search_fields = ('reference_id',)

class PomeReturnStockAdmin(admin.ModelAdmin):

    list_display = (
        'pid',
        'type',
        #'parentid',
        'employee_id',
        'item_id',
        'designation_id',
        'pome_item_requisition_id',
        'returned_stock',
        'remarks_stock',
        'reason_stock',
        'reusable',
        'penality_charges',
        'penality_amount_stock',
        'returned_date_stock',
        'siteincharge',
        'status_add',
        'datetime',
    )
    exclude = ('parentid',)
    list_filter = ('returned_date_stock', 'datetime')
    search_fields = ('employee_id',)

class PomeReturnStockVendorAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'vendor_id',
        'item_id',
        'quantity',
        'unit_price',
        'price',
        'remarks',
        'mode',
        'courier_no',
        'return_date',
        'reference_no',
        'approved_by',
        'datetime',
        'courier_name',
        'pod_number',
        'number_plate',
        'driver_name',
        'driver_contact',
        'per_name',
        'return_time',
        #'gatepass_no',
        #'in_date',
        #'in_time',
        'remarks_gp',
    )
    exclude = ('parentid','gatepass_no', 'in_date', 'in_time',)
    list_filter = (
        'vendor_id',
        'item_id',
        'return_date',
        'datetime',
        'in_date',
    )
    search_fields = ('item_id','vendor_id',)


class PomeSalAssignmentAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'client_name',
        'work_order_no',
        'month',
        'year',
        'supervisor',
        'salary',
        'payment_salary',
        'balance_salary',
        'incentive',
        'payment_incentive',
        'balance_incentive',
        'house_rent',
        'payment_house_rent',
        'balance_house_rent',
        'voucher',
        'payment_ottotal',
        'balance_ottotal',
        'others',
        'payment_others',
        'balance_others',
        'totamount',
        'payment_totamount',
        'balance_totamount',
        #'datetime',
    )
    exclude = ('parentid',)
    list_filter = ('client_name', 'work_order_no', 'datetime')
    search_fields = ('client_name','work_order_no')

class PomeSalAssignmentEmpsAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'psa_id',
        'pome_emloyees_id',
        'net_pay',
        'hra',
        'ot_got',
        'paid_mess',
        'cash_return',
        'incentive_ind',
        'net_pay_total',
        'hra_total',
        'ot_got_total',
        'incentive_ind_total',
        'paid_mess_total',
    )
    exclude = ('parentid',)
    search_fields = ('pome_emloyees_id',)

class PomeSalariesAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'pome_emloyees_id',
        'designation',
        'supervisor',
        'month_year',
        'month',
        'year',
        'work_days',
        'paid_leaves',
        'total_days',
        'total_hours',
        'basic',
        'cal_basic',
        'hra',
        'washing',
        'other',
        'bonus',
        'annual_bonus',
        'loyality_bonus',
        'total_allowances',
        'epf',
        'esi',
        'fines',
        'advances',
        'loans',
        'other_deductions',
        'total_deductions',
        'net_pay',
        'payment_status',
        'datetime',
        #'generated_id',
        #'work_order',
        #'conveyance',
        #'pt',
        #'tds',
    )
    exclude = ('parentid',)
    list_filter = ('month', 'year', 'pome_emloyees_id',)
    search_fields = ('pome_emloyees_id',)

class PomeSalariesGeneratedAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'designation',
        'from_date',
        'from_month',
        'from_year',
        'to_date',
        'to_month',
        'to_year',
        'from_final_date',
        'to_final_date',
        'from_year_month',
        'to_year_month',
        'status',
        'month',
        'year',
        'page',
        'page_limit',
        'page_current_limit',
        'otnot',
        'otallow',
    )
    exclude = ('parentid',)
    list_filter = ('from_date', 'from_final_date', 'to_final_date')


class PomeSalaryDisbursementAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'status',
        'salary_type',
        'client_id',
        'payment_to',
        'emp_id',
        'emp_name',
        'emp_code',
        'designation',
        'salary_month',
        'salary',
        'incentive',
        'voucher',
        'house_rent',
        'loan_amount',
        'absent_amount',
        'overtime_amount',
        'final_amount',
        'paid_amount',
        'balance_amount',
    )
    exclude = ('parentid',)
    list_filter = ('client_id', 'emp_id', 'designation')


class PomeSalaryFixedAdmin(admin.ModelAdmin):

    list_display = (u'id',
	#'parentid',
	'status',
	'designation',
	'amount')
    exclude = ('parentid',)
    list_filter = ('designation',)


class PomeSalaryPaymentTransactionsAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'salary_id',
        'pome_emloyees_id',
        'voucherno',
        'date',
        'payment',
        'cqno',
        'cqdate',
        'bank',
        'branch',
        'amount',
    )
    exclude = ('parentid',)
    list_filter = ('date', 'cqdate')
    search_fields = ('pome_emloyees_id',)

class PomeScaleDifferenceAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'scale_difference',
        'effective_date',
        'added_on',
    )
    exclude = ('parentid',)
    list_filter = ('effective_date', 'added_on')


class PomeSendsmsAdmin(admin.ModelAdmin):
    raw_id_fields = ("send_to",)
    list_display = (
        u'id',
        #'parentid',
        'send_to',
        'message',
        #'sms_no',
        #'number',
        'date',
        #'time',
    )
    exclude = ('parentid','sms_no', 'time',)
    list_filter = ('date',)
    search_fields = ('sms_no',)


class PomeShiftsAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'shift_name',
        'from_time',
        'to_time',
        'status',
        'added_on',
    )
    exclude = ('parentid',)
    list_filter = ('added_on',)

class PomeStipendDisbursementAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'status',
        'trainee_id',
        'session_id',
        'payment_amt',
        'paid_amount',
        'payment_status',
        'payment_method',
        'cheque_no',
        'cheque_date',
        'bank_name',
        'branch_name',
        'added_on',
    )
    exclude = ('parentid',)
    list_filter = ('trainee_id', 'session_id', 'added_on')
    search_fields = ('trainee_id',)

class PomeStipendTraineeAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'status',
        'session_id',
        'trainer_name',
        'location',
        'training_days',
        'perday_price',
    )
    exclude = ('parentid',)
    list_filter = ('session_id', 'trainer_name')
    search_fields = ('trainer_name',)

class PomeStockUpdateAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'item',
        'name',
        'invoiceno',
        'invoice_date',
        'quantity',
    )
    exclude = ('parentid',)
    list_filter = ('invoice_date',)
    search_fields = ('name',)


class PomeStocksAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'vendor_id',
        'store_id',
        'items',
        'quantity',
        'date_added',
    )
    exclude = ('parentid',)
    list_filter = ('date_added',)
    search_fields = ('vendor_id','store_id')

class PomeStocksTransactionsAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        'pome_stocks_id',
        'store_id',
        'vendor_id',
        'employee_id',
        'quantity',
        'pome_item_requisition_id',
        'pome_return_stock_id',
        'datetime',
        'status_add',
        'vendor_status',
    )
    exclude = ('parentid','datetime')
    list_filter = ('datetime',)
    search_fields = ('pome_stocks_id','store_id',)

class PomeSubmenusAdmin(admin.ModelAdmin):



    list_display = (
        u'id',
        #'parentid',
        'menu_id',
        'name',
        'link',
        'is_active',
        'inner_menu',
    )
    exclude = ('parentid',)
    search_fields = ('name',)


class PomeSuperAdminAdmin(admin.ModelAdmin):

    list_display = ('super_admin_id', 'username', 'password', 'email')
    exclude = ('parentid',)


class PomeSupporticketAdmin(admin.ModelAdmin):
    form = SupportticketForm
    list_display = (
        u'id',
        #'parentid',
        'name',
        'subject',
        'mail_from',
        'message',
        'status',
        'sended_on',
        #'empid',
        'update_message',
        'update_status',
    )
    #list_filter = ('sended_on',)
    exclude = ('parentid','update_message','empid', 'update_status')
    search_fields = ('name',)


class PomeTaskManagementAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'task',
        'task_summery',
        'assign_to',
        'assigned_by',
        'status',
        'assigned_on',
        'assigned_time',
        'time_duration',
        'start_time',
        'end_time',
        #'time_taken',
        #'start_date',
        #'starttime',
        #'date_time',
        'priority',
        #'taskremarks',
    )
    exclude = ('parentid','time_taken', 'start_date', 'starttime', 'date_time', 'task_remarks')
    #	list_filter = ('assign_to', 'assigned_on', 'start_date', 'date_time')


class PomeTraineeAttendenceAdmin(admin.ModelAdmin):
    form = PomeTraineeAttendenceForm
    list_display = (
        u'id',
        #'parentid',
        'trainee_id',
        #'name',
        #'code',
        'date',
	'hours',
	'work_order',
        #'status',
    )
    exclude = ('parentid','name', 'code', )
    list_filter = ('trainee_id',)
    search_fields = ('trainee_id',)

class PomeUploadWorkorderAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'status',
        'client_name',
        'branch',
        'order_name',
        'order_no',
        'order_date',
        'order_price',
        'order_upload',
    )
    exclude = ('parentid',)
    list_filter = ('client_name', 'order_date')
    search_fields = ('client_name',)

class PomeUserAccessAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'user_id',
        'permission_id',
        'menu_id',
        'sub_menu_id',
        'added_on',
    )
    exclude = ('parentid','added_on',)
    list_filter = ('added_on',)


class PomeUserPermissionAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'status',
        'permission_name',
        'description',
        'added_on',
    )
    exclude = ('parentid','status',)
    list_filter = ('added_on',)


class PomeUsersLogAdmin(admin.ModelAdmin):

    list_display = (
        u'id',
        #'parentid',
        'login_type',
        'login_id',
        'login_time',
        'logout_time',
        'loggedip',
    )
    exclude = ('parentid','loggedip',)
    list_filter = ('login_time', 'logout_time')


class PomeVisitorAdmin(admin.ModelAdmin):
    form = PomeVisitorForm
    list_display = (
        'id',
        #'parentid',
        'visitor_name',
        'from_company',
        'from_address',
        'contact_number',
        'emailid',
        'staff_guid',
        'purpose',
        'date',
        'time',
        'avaliability',
        #'alternate_person',
        #'date_added',
        #'alert_status',
        #'visit_date_time',
        #'update_person',
        'remarks',
        #'out_time',
    )
    exclude = ('parentid','date_added', 'alert_status', 'update_person', 'visit_date_time','alternate_person','out_time')
    list_filter = ('date', 'staff_guid', 'visitor_name')
    search_fields = ('visitor_name',)
 

class PomeWashingsAdmin(ImportExportModelAdmin):
    form = WashingForm
    list_display = (
        u'id',
	'washing_emp',
        'amount',
        #'end_amount',
        #'limit_amount',
        #'limit_amount_months',
        #'limit_months',
        'date',
    )
    resource_class = WashingResource

    #exclude = ('parentid',)
   # list_filter = ('datetime',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.PomeEmloyees, PomeEmloyeesAdmin)
_register(models.PomeManageClientsLocations, PomeManageClientsLocationsAdmin)
_register(models.PomeTrainer, PomeTrainerAdmin)
_register(models.PomeBiodata, PomeBiodataAdmin)
_register(models.PomeMasters, PomeMastersAdmin)
_register(models.PomeManageMasters, PomeManageMastersAdmin)
_register(models.PomeTrainingSession, PomeTrainingSessionAdmin)
_register(models.PomeManageItems, PomeManageItemsAdmin)
_register(models.PomeManageClients, PomeManageClientsAdmin)
_register(models.PomeAcknowledgement, PomeAcknowledgementAdmin)
_register(
    models.PomeAcknowledgementDocuments,
    PomeAcknowledgementDocumentsAdmin)
_register(models.PomeActions, PomeActionsAdmin)
_register(models.PomeAdvancesTypes, PomeAdvancesTypesAdmin)
_register(models.PomeAllowanceMaster, PomeAllowanceMasterAdmin)
_register(models.PomeAnnualbonus, PomeAnnualbonusAdmin)
_register(models.PomeBillingTax, PomeBillingTaxAdmin)
_register(models.PomeCalendar, PomeCalendarAdmin)
_register(models.PomeClientBilling, PomeClientBillingAdmin)
_register(models.PomeClientAttendance, PomeClientAttendanceAdmin)
_register(models.PomeClientBranches, PomeClientBranchesAdmin)
_register(models.PomeClientInvoice, PomeClientInvoiceAdmin)
_register(
    models.PomeClientInvoiceTransactions,
    PomeClientInvoiceTransactionsAdmin)
_register(models.PomeClientPatrolling, PomeClientPatrollingAdmin)
_register(
    models.PomeClientPaymentTransactions,
    PomeClientPaymentTransactionsAdmin)
_register(models.PomeConsultancies, PomeConsultanciesAdmin)
_register(models.PomeCustomerFeedback, PomeCustomerFeedbackAdmin)
_register(models.PomeDefaultAccess, PomeDefaultAccessAdmin)
_register(models.PomeDefaultAdvances, PomeDefaultAdvancesAdmin)
_register(models.PomeDisciplineCompliance, PomeDisciplineComplianceAdmin)
_register(models.PomeDonation, PomeDonationAdmin)
_register(models.PomeEmpAdvances, PomeEmpAdvancesAdmin)
_register(models.PomeEmpLoans, PomeEmpLoansAdmin)
_register(models.PomeEmpLoansTransactions, PomeEmpLoansTransactionsAdmin)
_register(models.PomeEmployeeAttendence, PomeEmployeeAttendenceAdmin)
_register(models.PomeEmployeeCtc, PomeEmployeeCtcAdmin)
_register(models.PomeEmployeeExpenditure, PomeEmployeeExpenditureAdmin)
_register(models.PomeEmployeeMovement, PomeEmployeeMovementAdmin)
_register(models.PomeEmployeePosting, PomeEmployeePostingAdmin)
_register(models.PomeEmployeeSeparations, PomeEmployeeSeparationsAdmin)
_register(models.PomeEmployeeSettlement, PomeEmployeeSettlementAdmin)
_register(models.PomeEodManagement, PomeEodManagementAdmin)
_register(models.PomeEodForward, PomeEodForwardAdmin)
_register(models.PomeExcessAttendance, PomeExcessAttendanceAdmin)
_register(models.PomeExcessLocAttendance, PomeExcessLocAttendanceAdmin)
_register(models.PomeFinalReport, PomeFinalReportAdmin)
_register(models.PomeFine, PomeFineAdmin)
_register(models.PomeFineDeductions, PomeFineDeductionsAdmin)
_register(models.PomeGallery, PomeGalleryAdmin)
_register(models.PomeGatepass, PomeGatepassAdmin)
_register(models.PomeGraderateSetting, PomeGraderateSettingAdmin)
_register(models.PomeGuardPlacement, PomeGuardPlacementAdmin)
_register(models.PomeHolidays, PomeHolidaysAdmin)
_register(models.PomeIncentive, PomeIncentiveAdmin)
_register(models.PomeIncentiveLoc, PomeIncentiveLocAdmin)
_register(models.PomeInnermenus, PomeInnermenusAdmin)
_register(models.PomeManageStores, PomeManageStoresAdmin)
_register(models.PomeVendorWorkshop, PomeVendorWorkshopAdmin)
_register(models.PomeInvoicePaymentDelete, PomeInvoicePaymentDeleteAdmin)
_register(models.PomeInwardInvoice, PomeInwardInvoiceAdmin)
_register(models.PomeInward, PomeInwardAdmin)
_register(models.PomeInwardDocuments, PomeInwardDocumentsAdmin)
_register(models.PomeInwardOutwardCourier, PomeInwardOutwardCourierAdmin)
_register(
    models.PomeInwardOutwardFixedAssets,
    PomeInwardOutwardFixedAssetsAdmin)
_register(models.PomeInwardOutwardMaterial, PomeInwardOutwardMaterialAdmin)
_register(models.PomeIssuance, PomeIssuanceAdmin)
_register(models.PomeItemDesignationwise, PomeItemDesignationwiseAdmin)
_register(models.PomeItemRequisition, PomeItemRequisitionAdmin)
_register(models.PomeK1Details, PomeK1DetailsAdmin)
_register(models.PomeLeaveManagement, PomeLeaveManagementAdmin)
_register(models.PomeLeavePeriod, PomeLeavePeriodAdmin)
_register(models.PomeLeavesAbsents, PomeLeavesAbsentsAdmin)
_register(models.PomeLoanTypes, PomeLoanTypesAdmin)
_register(models.PomeLoansAdvances, PomeLoansAdvancesAdmin)
_register(models.PomeLoansCalculation, PomeLoansCalculationAdmin)
_register(models.PomeLocDesgMaster, PomeLocDesgMasterAdmin)
_register(models.PomeLocationIncentive, PomeLocationIncentiveAdmin)
_register(models.PomeLocationIncharge, PomeLocationInchargeAdmin)
_register(
    models.PomeLocationInchargeSalaries,
    PomeLocationInchargeSalariesAdmin)
_register(models.PomeLocationsalarySettings, PomeLocationsalarySettingsAdmin)
_register(models.PomeLocdesg, PomeLocdesgAdmin)
_register(models.PomeLocpayIncentive, PomeLocpayIncentiveAdmin)
_register(models.PomeLoginDetails, PomeLoginDetailsAdmin)
_register(models.PomeLogins, PomeLoginsAdmin)
_register(models.PomeLoyalityBonous, PomeLoyalityBonousAdmin)
_register(models.PomeManageDepartments, PomeManageDepartmentsAdmin)
_register(models.PomeManageQuotation, PomeManageQuotationAdmin)
_register(models.PomeMenus, PomeMenusAdmin)
_register(models.PomeMobilePatrolling, PomeMobilePatrollingAdmin)
_register(models.PomeMoneytransferPettycash, PomeMoneytransferPettycashAdmin)
_register(models.PomeNoticeboard, PomeNoticeboardAdmin)
_register(models.PomeNotifications, PomeNotificationsAdmin)
_register(models.PomeOtherBenefits, PomeOtherBenefitsAdmin)
_register(models.PomeOutward, PomeOutwardAdmin)
_register(models.PomeOvertime, PomeOvertimeAdmin)
_register(models.PomeCutSalary, PomeCutSalaryAdmin)
_register(models.PomeOvertimeGenerated, PomeOvertimeGeneratedAdmin)
_register(models.PomeOvertimePayment, PomeOvertimePaymentAdmin)
_register(models.PomePatrolling, PomePatrollingAdmin)
_register(models.PomePattycashAccounts, PomePattycashAccountsAdmin)
_register(models.PomePayment, PomePaymentAdmin)
_register(models.PomePaymentCollection, PomePaymentCollectionAdmin)
_register(models.PomePaymentReceiptIncharge, PomePaymentReceiptInchargeAdmin)
_register(models.PomePaymentsTransfers, PomePaymentsTransfersAdmin)
_register(models.PomePayscaleSetting, PomePayscaleSettingAdmin)
_register(models.PomePoliceVerificationForm, PomePoliceVerificationFormAdmin)
_register(models.PomePurchaseOrder, PomePurchaseOrderAdmin)
_register(models.PomePurchaseRequisition, PomePurchaseRequisitionAdmin)
_register(models.PomeReferenceIncentive, PomeReferenceIncentiveAdmin)
_register(models.PomeReferencePayment, PomeReferencePaymentAdmin)
_register(models.PomeReturnStock, PomeReturnStockAdmin)
_register(models.PomeReturnStockVendor, PomeReturnStockVendorAdmin)
_register(models.PomeSalAssignment, PomeSalAssignmentAdmin)
_register(models.PomeSalAssignmentEmps, PomeSalAssignmentEmpsAdmin)
_register(models.PomeSalaries, PomeSalariesAdmin)
_register(models.PomeSalariesGenerated, PomeSalariesGeneratedAdmin)
_register(models.PomeSalaryDisbursement, PomeSalaryDisbursementAdmin)
_register(models.PomeSalaryFixed, PomeSalaryFixedAdmin)
_register(
    models.PomeSalaryPaymentTransactions,
    PomeSalaryPaymentTransactionsAdmin)
_register(models.PomeScaleDifference, PomeScaleDifferenceAdmin)
_register(models.PomeSendsms, PomeSendsmsAdmin)
_register(models.PomeSeparations, PomeSeparationsAdmin)
_register(models.PomeStaffType, PomeStaffTypeAdmin)
_register(models.PomeUpload, PomeUploadAdmin)
_register(models.PomeShifts, PomeShiftsAdmin)
_register(models.PomeStipendDisbursement, PomeStipendDisbursementAdmin)
_register(models.PomeStipendTrainee, PomeStipendTraineeAdmin)
_register(models.PomeStockUpdate, PomeStockUpdateAdmin)
_register(models.PomeStocks, PomeStocksAdmin)
_register(models.PomeStocksTransactions, PomeStocksTransactionsAdmin)
_register(models.PomeSubmenus, PomeSubmenusAdmin)
_register(models.PomeSuperAdmin, PomeSuperAdminAdmin)
_register(models.PomeSupporticket, PomeSupporticketAdmin)
_register(models.PomeTaskManagement, PomeTaskManagementAdmin)
_register(models.PomeTraineeAttendence, PomeTraineeAttendenceAdmin)
_register(models.PomeUploadWorkorder, PomeUploadWorkorderAdmin)
_register(models.PomeUserAccess, PomeUserAccessAdmin)
_register(models.PomeUserPermission, PomeUserPermissionAdmin)
_register(models.PomeUsersLog, PomeUsersLogAdmin)
_register(models.PomeVisitor, PomeVisitorAdmin)
_register(models.PomeWashings, PomeWashingsAdmin)
_register(models.PomeOjtdeductions, PomeOjtAdmin)
