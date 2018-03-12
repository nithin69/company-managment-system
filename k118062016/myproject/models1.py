# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.

from django.db import models
from k1emp.models import Employee 
from django.utils import timezone
from django.contrib import admin
    
class TrainingSession(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=25, choices=status_choices)
    session_name = models.CharField(max_length=255)
    trainer_name = models.ForeignKey(Employee)
    place = models.CharField(max_length=255)
    session_strength = models.CharField(max_length=255)
    total_days = models.CharField(max_length=255)
    training_dates = models.CharField(max_length=255)
    added_on = models.DateTimeField()
    perday_price = models.CharField(max_length=255)


class ManageItems(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    item_code = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    itemtype = models.CharField(max_length=50)
    category = models.CharField(max_length=255)
    measurement = models.CharField(max_length=255)
    threshold_limit = models.CharField(max_length=255)
    unit_price = models.CharField(max_length=255)
    charge_price = models.CharField(max_length=50)
    threshold_to1 = models.CharField(max_length=255)
    days1 = models.CharField(max_length=255)
    threshold_to2 = models.CharField(max_length=255)
    days2 = models.CharField(max_length=255)
    threshold_to3 = models.CharField(max_length=255)
    days3 = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    added_on = models.DateField()
    timestamp = models.DateTimeField()
    initiated_by = models.IntegerField()
    stockitem = models.IntegerField()




class ManageMasters(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    master_id = models.CharField(max_length=255)
    dept_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    added_on = models.DateTimeField()





class Acknowledgement(models.Model):
     # AutoField?
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.IntegerField()
    designation = models.CharField(max_length=255)
    emp_id = models.ForeignKey(Employee)
    emp_name = models.CharField(max_length=255)
    emp_code = models.CharField(max_length=255)
    join_date = models.CharField(max_length=255)
    receive_date = models.DateField()
    receive_time = models.TimeField()
    amount = models.IntegerField()
    training_cost = models.IntegerField()
    address = models.TextField()
    status = models.CharField(max_length=100, choices=status_choices)
    document = models.FileField(upload_to="documents")
    recept_no = models.CharField(max_length=255)
    recept_date = models.DateField()
    ack_reference_no = models.CharField(max_length=255)
    added_on = models.DateTimeField()



class AcknowledgementDocuments(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    ackn_id = models.CharField(max_length=255)
    upload_documents = models.FileField(upload_to="documents")



class Actions(models.Model):
     # AutoField?
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=250)



class AdvancesTypes(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.IntegerField()
    status = models.CharField(max_length=100, choices=status_choices)
    loan_type = models.CharField(max_length=255)
    description = models.TextField()
    added_on = models.DateField()



class AllowanceMaster(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.CharField(max_length=255)
    date = models.DateField()
    employee_id = models.ForeignKey(Employee)
    designation = models.ForeignKey(ManageMasters)
    gross_salary = models.IntegerField()
    basic_salary = models.IntegerField()
    bonus_val = models.CharField(max_length=255)
    loyality_bonus_val = models.CharField(max_length=52)
    loyality_bonus_period = models.IntegerField()
    bonus_unit = models.CharField(max_length=255)
    hra_val = models.CharField(max_length=255)
    hra_unit = models.CharField(max_length=255)
    others_val = models.CharField(max_length=255)
    others_unit = models.CharField(max_length=255)
    washing_val = models.CharField(max_length=255)
    washing_unit = models.CharField(max_length=255)
    epf_val = models.CharField(max_length=255)
    epf_unit = models.CharField(max_length=255)
    epf_emp_val = models.CharField(max_length=255)
    epf_emp_unit = models.CharField(max_length=255)
    conveyance_val = models.CharField(max_length=255)
    conveyance_unit = models.CharField(max_length=255)
    esi_val = models.CharField(max_length=255)
    esi_unit = models.CharField(max_length=255)
    esi_emp_val = models.CharField(max_length=255)
    esi_emp_unit = models.CharField(max_length=255)
    percent_basic = models.CharField(max_length=50)
    value_hra = models.CharField(max_length=50)
    value_conveyance = models.CharField(max_length=50)
    value_washing = models.CharField(max_length=50)
    value_bonus = models.CharField(max_length=50)
    value_others = models.CharField(max_length=50)
    perday_wage = models.CharField(max_length=50)
    otallowed = models.IntegerField()
    ptax_val = models.CharField(max_length=50)
    ptax_unit = models.CharField(max_length=50)
    tds_val = models.CharField(max_length=50)
    tds_unit = models.CharField(max_length=50)
    status = models.CharField(max_length=25, choices=status_choices)
    added_on = models.DateField()



class Annualbonus(models.Model):
     # AutoField?
    from_month = models.IntegerField()
    to_month = models.IntegerField()
    month_eligible = models.IntegerField()
    limit_months = models.IntegerField()
    percentage = models.FloatField()



class BillingTax(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.IntegerField()
    service_tax = models.CharField(max_length=255)
    edu_cess = models.CharField(max_length=255)
    high_edu_cess = models.CharField(max_length=255)
    swacch_bharat = models.CharField(max_length=10)
    krish_kalyan = models.CharField(max_length=10)
    date = models.DateField()
    status = models.CharField(max_length=25, choices=status_choices)
    added_on = models.DateField()



class Calendar(models.Model):
    yes = "Yes"
    no = "No"
    repeat_choices = ((yes, "Yes"), (no, "No"))
    every_day = "Every Day"
    every_week = "Every Week"
    every_month = "Every Month"
    repeat_on_choices = ((every_week, "Every Week"), (every_day,"Every Day"), (every_month, "Every Month"))
    
    title = models.CharField(max_length=160)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    allday = models.BooleanField()  # Field name made lowercase.
    color = models.CharField(max_length=7)
    url = models.CharField(max_length=255)
    category = models.CharField(max_length=200)
    repeat_type = models.CharField(max_length=20, choices=repeat_choices)
    user_id = models.IntegerField()
    repeat_id = models.CharField(max_length=20, choices=repeat_on_choices)



class ClientBilling(models.Model):
    authorised = "Authorised"
    unauthorised = "Unauthorised"
    authorised_choices = ((authorised, "Authorised"), (unauthorised, "Unauthorised"))
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.IntegerField()
    added_on = models.DateField()
    client_name = models.ForeignKey('ManageClients')
    work_order_no = models.CharField(max_length=250)
    designation = models.ForeignKey(ManageMasters)
    hour = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    noofpersons = models.IntegerField()
    rate = models.IntegerField()
    clientrate = models.IntegerField()
    k1rate = models.IntegerField()
    date = models.DateField()
    todate = models.DateField()
    billingperiod = models.IntegerField()
    authorised = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    supervisor = models.CharField(max_length=255)
    alert_status = models.CharField(max_length=20, choices=status_choices)
    date_time = models.DateTimeField()
    createdby = models.IntegerField()
    updatedby = models.ForeignKey(Employee)
    updatetime = models.DateTimeField()


class ClientAttendance(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    client_id = models.ForeignKey('ManageClients')
    work_order = models.ForeignKey(ClientBilling)
    employee_id = models.ForeignKey(Employee)
    month = models.IntegerField()
    year = models.IntegerField()
    one = models.IntegerField()
    two = models.IntegerField()
    three = models.IntegerField()
    four = models.IntegerField()
    five = models.IntegerField()
    six = models.IntegerField()
    seven = models.IntegerField()
    eight = models.IntegerField()
    nine = models.IntegerField()
    ten = models.IntegerField()
    eleven = models.IntegerField()
    twelve = models.IntegerField()
    thirteen = models.IntegerField()
    fourteen = models.IntegerField()
    fifteen = models.IntegerField()
    sixteen = models.IntegerField()
    seventeen = models.IntegerField()
    eightteen = models.IntegerField()
    nineteen = models.IntegerField()
    twenty = models.IntegerField()
    twentyone = models.IntegerField()
    twentytwo = models.IntegerField()
    twentythree = models.IntegerField()
    twentyfour = models.IntegerField()
    twentyfive = models.IntegerField()
    twentysix = models.IntegerField()
    twentyseven = models.IntegerField()
    twentyeight = models.IntegerField()
    twentynine = models.IntegerField()
    thirty = models.IntegerField()
    thirtyone = models.IntegerField()
    total_hours = models.IntegerField()
    sessionid = models.IntegerField()
    datetime = models.DateTimeField()





class ClientBranches(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255)
    client_id = models.ForeignKey('ManageClients')
    status = models.CharField(max_length=25, choices=status_choices)
    branch_name = models.CharField(max_length=255)
    branch_addr = models.CharField(max_length=255)
    branch_tele = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date = models.DateField()



class ClientInvoice(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    active = "Active"
    inactive = "Inactive"
    present_status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    client_id = models.ForeignKey('ManageClients')
    work_order_no = models.ForeignKey(ClientBilling)
    parentid = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()
    invoice_date = models.DateField()
    invoice_no = models.CharField(max_length=50)
    invnumber = models.IntegerField()
    sub_total = models.IntegerField()
    others = models.IntegerField()
    final_total = models.IntegerField()
    stax = models.IntegerField()
    edu_cess = models.IntegerField()
    high_edu_cess = models.IntegerField()
    swacch_bharat = models.IntegerField()
    krish_kalyan = models.IntegerField()
    total_amount = models.IntegerField()
    datetime = models.DateTimeField()
    sub_total_authorised = models.IntegerField()
    sub_total_additional = models.IntegerField()
    status = models.CharField(max_length=20, choices=status_choices)
    prtstatus = models.CharField(max_length=20, choices=status_choices)



class ClientInvoiceTransactions(models.Model):
    authorised = "Authorised"
    unauthorised = "Unauthorised"
    authorised_choices = ((authorised, "Authorised"), (unauthorised, "Unauthorised"))
    
    _client_invoice_id = models.ForeignKey(ClientInvoice)
    client_id = models.ForeignKey('ManageClients')
    work_order_no = models.ForeignKey(ClientBilling)
    status_auth = models.CharField(max_length=50, choices=authorised_choices)
    no_of_employees = models.IntegerField()
    designation = models.ForeignKey(ManageMasters)
    hours = models.IntegerField()
    rate = models.IntegerField()
    price = models.IntegerField()
    no_of_employees_want = models.IntegerField()
    no_of_hours_want = models.IntegerField()
    no_of_rate_want = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()



class ClientPatrolling(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    clientid = models.ForeignKey('ManageClients')
    patrollingno = models.CharField(max_length=50)
    employeeid = models.ForeignKey(Employee)
    remarks = models.TextField()



class ClientPaymentTransactions(models.Model):
    cash = "Cash"
    cheque = "Cheque"
    payment_choices = ((cash, "Cash"), (cheque, "Cheque"))
    
    invoice_id = models.ForeignKey(ClientInvoice)
    date = models.DateField()
    payment = models.CharField(max_length=50, choices=payment_choices)
    cqno = models.CharField(max_length=50)
    cqdate = models.DateField()
    bank = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    amount = models.IntegerField()
    tds = models.IntegerField()
    otherded = models.IntegerField()
    reason = models.TextField()
    work_order_no = models.ForeignKey(ClientBilling)



class Consultancies(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.IntegerField()
    consultancy_name = models.CharField(max_length=50)
    consultancy_address = models.CharField(max_length=250)
    consultancy_phoneno = models.IntegerField()
    consultancy_emailid = models.CharField(max_length=50)
    contactperson_name = models.CharField(max_length=50)
    contactperson_phoneno = models.CharField(max_length=20)
    contactperson_emailid = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=status_choices)



class CustomerFeedback(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"    
    incharge_choices = ((one, "1"), (two, "2"),(three, "3"), (four, "4"),(five, "5"))
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=status_choices)
    customer_id = models.ForeignKey('ManageClients')
    customer_name = models.CharField(max_length=255)
    customer_address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    incharge_perform = models.CharField(max_length=25, choices=incharge_choices)
    guard_perform = models.CharField(max_length=25, choices=incharge_choices)
    dressup_rate = models.CharField(max_length=25, choices=incharge_choices)
    record_communicate = models.CharField(max_length=25, choices=incharge_choices)
    head_office_staff = models.CharField(max_length=25, choices=incharge_choices)
    daily_report = models.CharField(max_length=25, choices=incharge_choices)
    night_patrolling = models.CharField(max_length=25, choices=incharge_choices)
    service_quality = models.BooleanField()
    lodged_compt = models.BooleanField()
    complaint = models.TextField()
    improvement = models.TextField()
    remarks = models.CharField(max_length=25, choices=incharge_choices)
    date = models.DateField()
    work_order_no = models.ForeignKey(ClientBilling)



class DefaultAccess(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    permission_id = models.CharField(max_length=255)
    menu_id = models.IntegerField()
    sub_menu_id = models.IntegerField()
    added_on = models.DateField()



class DefaultAdvances(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    name = models.CharField(max_length=250)
    amount = models.IntegerField()
    description = models.TextField()
    installment_no = models.IntegerField()
    datetime = models.DateTimeField()
    first_slot = models.IntegerField()
    second_slot = models.IntegerField()
    first_slot_installment = models.IntegerField()
    second_slot_installment = models.IntegerField()



class DisciplineCompliance(models.Model):
    normal = "Normal"
    priority = "Priority"
    serious = "Serious"
    priority_choices = ((normal, "Normal"), (priority, "Priority"), (serious,"Serious"))
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.IntegerField()
    group_id = models.IntegerField()
    initiated_by = models.ForeignKey(Employee)
    send_date = models.DateField()
    send_time = models.TimeField()
    subject = models.CharField(max_length=255)
    description = models.TextField()
    send_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=25, choices=priority_choices)
    alert_status = models.CharField(max_length=20, choices=status_choices)
    date_time = models.DateTimeField()



class Donation(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    cash = "Cash"
    cheque = "Cheque"
    payment_choices = ((cash, "Cash"), (cheque, "Cheque"))
    
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=25, choices=status_choices)
    donation_date = models.DateField()
    donation_to = models.CharField(max_length=255)
    address = models.TextField()
    mobile = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=25, choices=payment_choices)
    cheque_no = models.CharField(max_length=255)
    cheque_date = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    description = models.TextField()



class EmpAdvances(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=25, choices=status_choices)
    emp_id = models.ForeignKey(Employee)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    month = models.CharField(max_length=255)
    opening_balance = models.CharField(max_length=255)
    issued_adv1 = models.CharField(max_length=255)
    issued_adv2 = models.CharField(max_length=255)
    deduct_adv1 = models.CharField(max_length=255)
    deduct_adv2 = models.CharField(max_length=255)
    closing_balance = models.CharField(max_length=255)



class EmpLoans(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=status_choices)
    type = models.CharField(max_length=255)
    apply_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    loan_type = models.CharField(max_length=255)
    emp_id = models.ForeignKey(Employee)
    designation = models.ForeignKey(ManageMasters)
    loan_amount = models.CharField(max_length=255)
    reason = models.CharField(max_length=11)
    int_apli = models.CharField(max_length=255)
    interest = models.CharField(max_length=255)
    amount_with_interest = models.CharField(max_length=255)
    instalment_no = models.IntegerField()
    instalment_amount = models.CharField(max_length=255)
    approval = models.CharField(max_length=255)
    approved_by = models.CharField(max_length=255)
    approved_on = models.DateField()
    default_advance_id = models.IntegerField()
    training_cost_type = models.IntegerField()


class EmpLoansTransactions(models.Model):
    paid = "Paid"
    not_paid = "Not Paid"
    partly_paid = "Partly Paid"
    paid_choices = ((paid, "Paid"), (not_paid, "Not Paid"), (partly_paid,"Partly Paid"))
    yes = "Yes"
    no = "No"
    approve_choices = ((yes, "Yes"), (no, "No"))
    
    _employee_id = models.ForeignKey(Employee)
    _emp_loans_id = models.ForeignKey(EmpLoans)
    type = models.CharField(max_length=150)
    date = models.DateField()
    instalment_amount = models.IntegerField()
    status = models.CharField(max_length=25, choices=paid_choices)
    approve_status = models.IntegerField()
    view_status = models.IntegerField()


class EmployeeAttendence(models.Model):
    present = "Present"
    absent = "Absent"
    leave = "Leave"
    tour = "Tour"
    leave_choices = ((present, "Present"), (absent, "Absent"),(leave, "Leave"), (tour, "Tour"))
    
    employee_id = models.ForeignKey(Employee)
    designation = models.ForeignKey(ManageMasters)
    _leaves_absents_id = models.IntegerField()
    applied_for = models.IntegerField()
    date = models.DateField()
    month_year = models.DateField()
    status = models.CharField(max_length=50, choices=leave_choices)
    work_order = models.ForeignKey(ClientBilling)
    actual_hours = models.IntegerField()
    hours = models.IntegerField()
    minutes = models.IntegerField()
    remarks = models.TextField()
    locations_id = models.IntegerField()
    datetime = models.DateTimeField()
    entered = models.IntegerField()


class EmployeeCtc(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=25, choices=status_choices)
    ctc_name = models.CharField(max_length=255)
    ctc_amount = models.CharField(max_length=255)
    date = models.DateField()


class EmployeeExpenditure(models.Model):
    savings = "Savings"
    current = "Current"
    others = "Others"
    account_choices = ((savings, "Savings"), (current, "Current"), (others,"Others"))
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255)
    acc_type = models.CharField(max_length=25, choices=account_choices)
    status = models.CharField(max_length=25, choices=status_choices)
    account_id = models.CharField(max_length=255)
    auth_person = models.CharField(max_length=255)
    emp_name = models.ForeignKey(Employee)
    designation = models.ForeignKey(ManageMasters)
    expenditure_name = models.CharField(max_length=255)
    purpose = models.TextField()
    expenditure_amount = models.CharField(max_length=255)
    expenditure_date = models.DateField()
    upload = models.FileField(upload_to ="documents")
    reference_no = models.CharField(max_length=255)
    approver = models.CharField(max_length=255)
    approved_by = models.CharField(max_length=255)



class EmployeeMovement(models.Model):
    permanent = "Permanent"
    contract = "Contract"
    job_choices = ((permanent, "Permanent"), (contract, "Contract"))
    new = "New"
    old = "Old"
    emp_choices = ((new, "New"), (old, "Old"))
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    
    parentid = models.CharField(max_length=255)
    client_id = models.ForeignKey('ManageClients')
    hours = models.IntegerField()
    work_order = models.ForeignKey(ClientBilling)
    auto_work_order_no = models.CharField(max_length=50)
    order_number = models.IntegerField()
    emp_name = models.ForeignKey(Employee)
    designation = models.ForeignKey(ManageMasters)
    order_by = models.CharField(max_length=255)
    order_designation = models.CharField(max_length=250)
    order_date = models.DateField()
    order_time = models.TimeField()
    from_date = models.DateField()
    to_date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    reason = models.CharField(max_length=255)
    emp_status = models.CharField(max_length=25, choices=emp_choices)
    job_status = models.CharField(max_length=25, choices=job_choices)
    gmo = models.IntegerField()
    exc_site = models.IntegerField()
    old_site = models.IntegerField()
    allowance = models.CharField(max_length=20)
    reach_update = models.DateTimeField()
    alert_status = models.IntegerField()
    remarks = models.TextField()
    reporting_date = models.DateField()
    reporting_time = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=status_choices)



class EmployeePosting(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=25, choices=status_choices)
    emp_id = models.ForeignKey(Employee)
    emp_name = models.CharField(max_length=255)
    emp_code = models.CharField(max_length=255)
    designation = models.ForeignKey(ManageMasters)
    moveto_client = models.CharField(max_length=255)
    client_branch = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    order_by = models.CharField(max_length=255)
    order_date = models.DateField()
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.CharField(max_length=255)
    emp_status = models.CharField(max_length=255)
    added_on = models.DateTimeField()



class EmployeeSeparations(models.Model):
     # AutoField?
    _employees_id = models.ForeignKey(Employee)
    separation_net_pay = models.FloatField()
    total_earnings = models.FloatField()
    epf_esi = models.FloatField()
    adp = models.FloatField()
    ldp = models.FloatField()
    other_deductions = models.FloatField()
    sub_total = models.FloatField()
    mess = models.FloatField()
    total_amount = models.FloatField()
    message = models.FloatField()
    training_cost = models.FloatField()
    others_recovery = models.FloatField()
    acknowledge = models.FloatField()
    separation_paid_amount = models.FloatField()
    payment_type = models.CharField(max_length=50)
    cqno = models.CharField(max_length=50)
    cqdate = models.DateField()
    bank = models.CharField(max_length=150)
    branch = models.CharField(max_length=150)
    online_type = models.CharField(max_length=150)
    reference_number = models.CharField(max_length=150)
    datetime = models.DateTimeField()



class EmployeeSettlement(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=25, choices=status_choices)
    emp_id = models.ForeignKey(Employee)
    emp_name = models.CharField(max_length=255)
    emp_code = models.CharField(max_length=255)
    designation = models.ForeignKey(ManageMasters)
    settlement_amt = models.CharField(max_length=255)
    paid_amount = models.CharField(max_length=255)
    balance_amount = models.CharField(max_length=255)
    settlement_status = models.CharField(max_length=255)
    added_on = models.DateField()


class EodManagement(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255)
    eod_subject = models.TextField()
    eod_data = models.TextField()
    eod_by = models.ForeignKey(Employee)
    status = models.CharField(max_length=25, choices=status_choices)
    sended_on = models.DateTimeField()


class EodForward(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    eod_id = models.ForeignKey(EodManagement)
    remarks = models.CharField(max_length=255)
    forward_to = models.ForeignKey(Employee)





class ExcessAttendance(models.Model):
    employee_id = models.ForeignKey(Employee)
    work_order = models.ForeignKey(ClientBilling)
    day_balance = models.CharField(max_length=50, blank=True)
    rota_entry = models.CharField(max_length=50, blank=True)
    entered = models.CharField(max_length=50, blank=True)
    date = models.DateField()
    date_entered = models.DateField()



class ExcessLocAttendance(models.Model):
     # AutoField?
    employee_id = models.ForeignKey(Employee)
    work_order = models.ForeignKey(ClientBilling)
    day_balance = models.CharField(max_length=50)
    rota_entry = models.CharField(max_length=50)
    entered = models.CharField(max_length=50)
    date = models.DateField()
    date_entered = models.DateField()



class FinalReport(models.Model):
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"    
    final_choices = ((one, "1"), (two, "2"),(three, "3"), (four, "4"),(five, "5"))
    selected = "Selected"
    not_selected = "Not_Selected"    
    recom_choices = ((selected, "Selected"), (not_selected, "Not_Selectes"))
    
    parentid = models.CharField(max_length=255)
    biodata_id = models.ForeignKey(Employee)
    attire = models.CharField(max_length=25, choices=final_choices)
    punctuality = models.CharField(max_length=25, choices=final_choices)
    behaviour = models.CharField(max_length=25, choices=final_choices)
    tabacco = models.CharField(max_length=25, choices=final_choices)
    command = models.CharField(max_length=25, choices=final_choices)
    drill = models.CharField(max_length=25, choices=final_choices)
    recom = models.CharField(max_length=25, choices=recom_choices)
    remarks = models.CharField(max_length=255)
    added_on = models.DateField()



class Fine(models.Model):
     # AutoField?
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    amount = models.IntegerField()


class FineDeductions(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    apply_date = models.DateField()
    month = models.IntegerField()
    year = models.IntegerField()
    emp_id = models.ForeignKey(Employee)
    amount = models.IntegerField()
    selc_fine_ids = models.ForeignKey(Fine)
    others = models.IntegerField()
    pot = models.IntegerField()
    datetime = models.DateTimeField()



class Gallery(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    gallery_type = models.CharField(max_length=255)
    image = models.ImageField(upload_to="photos")
    added_on = models.DateField()



class Gatepass(models.Model):
    stock = "Stock"
    employees = "Employees"    
    gatepass_choices = ((stock, "Stock"), (employees, "Employees"))
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    gatepass_type = models.CharField(max_length=25, choices=gatepass_choices)
    outtime = models.DateTimeField()
    intime = models.DateTimeField()
    gateno = models.CharField(max_length=20)
    purpose = models.CharField(max_length=255)
    employee = models.ForeignKey('k1emp.Employee', related_name = "gatepass_emp")
    gatepass_no = models.CharField(max_length=255)
    approver = models.ForeignKey('k1emp.Employee', related_name = "gatepass_approver")
    issuedby = models.ForeignKey('k1emp.Employee', related_name = "gatepass_issuedby")
    stock_to = models.CharField(max_length=255)
    particulars = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    inventoryno = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    splinstruction = models.CharField(max_length=255)
    update_remarks = models.CharField(max_length=60)
    date_time = models.DateTimeField()
    cancel_remarks = models.CharField(max_length=255)

class GatepassAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Gatepass._meta.fields]



class GraderateSetting(models.Model):
    grade_a = "Grade A"
    grade_b = "Grade B"
    grade_c = "Grade C"
    grade_d = "Grade D"
    grade_choices = ((grade_a,"Grade A"),(grade_b,"Grade B"), (grade_c,"Grade C"),(grade_d,"Grade D"))
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255)
    grade_name = models.CharField(max_length=25, choices=grade_choices)
    rate = models.CharField(max_length=255)
    date = models.DateField()
    status = models.CharField(max_length=25, choices=status_choices)
    added_on = models.DateField()



class GuardPlacement(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.CharField(max_length=255)
    client_name = models.ForeignKey('ManageClients')
    location = models.CharField(max_length=255)
    designation = models.ForeignKey(ManageMasters)
    emp_id = models.ForeignKey(Employee)
    employe_name = models.CharField(max_length=255)
    status = models.CharField(max_length=25, choices=status_choices)
    post_from = models.DateField()
    post_to = models.DateField()
    added_on = models.DateTimeField()



class Holidays(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.IntegerField()
    name = models.CharField(max_length=50)
    date = models.DateField()
    remarks = models.CharField(max_length=255)
    holiday = models.CharField(max_length=20)
    status = models.CharField(max_length=25, choices=status_choices)



class Incentive(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255)
    designation = models.ForeignKey(ManageMasters)
    amount = models.CharField(max_length=255)
    date = models.DateField()
    status = models.CharField(max_length=255, choices=status_choices)
    added_on = models.DateField()
    purpose = models.CharField(max_length=255)
    totamount = models.IntegerField()
    generated_id = models.IntegerField()



class IncentiveLoc(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    totamount = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=25, choices=status_choices)
    added_on = models.DateField()
    generated_id = models.IntegerField()



class Innermenus(models.Model):
     # AutoField?
    submenu_id = models.IntegerField()
    name = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    is_active = models.IntegerField()



class ManageStores(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)
    address = models.TextField()
    contact_no = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    added_on = models.DateTimeField()



class VendorWorkshop(models.Model):
     # AutoField?
    login_type = models.CharField(max_length=50)
    profile_pic = models.CharField(max_length=255)
    parentid = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    company_vendor_name = models.CharField(max_length=255)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    vendor_code = models.CharField(max_length=50)
    registration_no = models.CharField(max_length=255)
    company_type = models.CharField(max_length=255)
    agreement_date = models.DateField()
    purpose = models.CharField(max_length=50)
    regd_office_addr = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pin_code = models.CharField(max_length=255)
    company_email = models.CharField(max_length=255)
    company_telephone = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    amc_period = models.CharField(max_length=50)
    tin_tan = models.CharField(max_length=255)
    service_tax = models.CharField(max_length=50)
    bank_details = models.TextField()
    bank = models.CharField(max_length=255)
    ac_no = models.CharField(max_length=255)
    ifsc_no = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    bank_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    pan_no = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    added_on = models.DateField()




class InvoicePaymentDelete(models.Model):
    cash = "Cash"
    cheque = "Cheque"
    payment_choices = ((cash, "Cash"), (cheque, "Cheque"))
    
    invoice_id = models.ForeignKey(ClientInvoice)
    date = models.DateField()
    payment = models.CharField(max_length=50, choices=payment_choices)
    cqno = models.CharField(max_length=50)
    cqdate = models.DateField()
    bank = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    amount = models.IntegerField()
    tds = models.IntegerField()
    otherded = models.IntegerField()
    reason = models.CharField(max_length=50)
    entered = models.IntegerField()
    datetime = models.DateTimeField()





class InwardInvoice(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.IntegerField()
    status = models.CharField(max_length=20, choices=status_choices)
    date = models.DateField()
    invoice_no = models.ForeignKey(ClientInvoice)
    vendor_id = models.ForeignKey(VendorWorkshop)
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    datetime = models.DateTimeField()



class Inward(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    courier = "Couries"
    transport = "Transport"
    person = "Person"
    courier_choices = ((courier, "Courier"), (transport, "Transport"), (person, "Person"))
    
    _inward_invoice_id = models.ForeignKey(InwardInvoice)
    status = models.CharField(max_length=20, choices=status_choices)
    _purchase_requisition_id = models.IntegerField()
    _inward_id = models.IntegerField()
    parentid = models.IntegerField()
    date = models.DateField()
    to = models.CharField(max_length=255)
    invoice_no = models.ForeignKey(ClientInvoice)
    vendor_id = models.ForeignKey(VendorWorkshop)
    store_id = models.ForeignKey(ManageStores)
    items = models.IntegerField()
    ordered = models.IntegerField()
    received = models.IntegerField()
    price = models.IntegerField()
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    exceed = models.IntegerField()
    remarks = models.TextField()
    courier_type = models.CharField(max_length=25, choices=courier_choices)
    courier_name = models.CharField(max_length=250)
    pod_number = models.CharField(max_length=250)
    driver_number_plate = models.CharField(max_length=250)
    driver_name = models.CharField(max_length=250)
    driver_contact = models.CharField(max_length=250)
    per_name = models.CharField(max_length=250)
    per_contact = models.CharField(max_length=250)
    received_by = models.CharField(max_length=250)
    datetime = models.DateTimeField()
    inward_type = models.CharField(max_length=50)
    alert_status = models.IntegerField()



class InwardDocuments(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    inward_id = models.ForeignKey(Inward)
    upload_documents = models.FileField(upload_to="documents")





class InwardOutwardCourier(models.Model):
    courier = "Couries"
    transport = "Transport"
    person = "Person"
    courier_choices = ((courier, "Courier"), (transport, "Transport"), (person, "Person"))
    
    guid = models.IntegerField(primary_key=True)
    parentid = models.IntegerField()
    type = models.CharField(max_length=25, choices=courier_choices)
    date = models.DateField()
    from_field = models.CharField(max_length=250)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=250)
    courier_type = models.CharField(max_length=250)
    courier_name = models.CharField(max_length=250)
    pod_number = models.CharField(max_length=250)
    received_by = models.CharField(max_length=250)
    dateandtime_delivery = models.DateTimeField()
    courier_particulars = models.TextField()
    remarks = models.TextField()
    date_added = models.DateField()



class InwardOutwardFixedAssets(models.Model):
    courier = "Couries"
    transport = "Transport"
    person = "Person"
    courier_choices = ((courier, "Courier"), (transport, "Transport"), (person, "Person"))
    
    guid = models.IntegerField(primary_key=True)
    parentid = models.IntegerField()
    type = models.CharField(max_length=25, choices=courier_choices)
    fixed_date = models.DateField()
    fixed_visitor_name = models.CharField(max_length=250)
    fixed_from = models.CharField(max_length=250)
    fixed_contact = models.CharField(max_length=250)
    fixed_email = models.CharField(max_length=250)
    fixed_whom = models.CharField(max_length=250)
    fixed_purpose = models.CharField(max_length=250)
    fixed_issued_entry_pass = models.CharField(max_length=250)
    fixed_issued_ppe = models.CharField(max_length=250)
    date_added = models.DateField()


class InwardOutwardMaterial(models.Model):
    courier = "Couries"
    transport = "Transport"
    person = "Person"
    courier_choices = ((courier, "Courier"), (transport, "Transport"), (person, "Person"))
    
    guid = models.IntegerField(primary_key=True)
    parentid = models.IntegerField()
    type = models.CharField(max_length=25, choices=courier_choices)
    receipts_date = models.DateField()
    receipts_invoice_number = models.CharField(max_length=250)
    receipts_received_from = models.CharField(max_length=250)
    receipts_quantity = models.CharField(max_length=250)
    receipts_cumulative = models.CharField(max_length=250)
    receipts_remarks = models.TextField()
    issues_date = models.DateField()
    issues_requisition_no = models.CharField(max_length=250)
    issues_issued_to = models.CharField(max_length=250)
    issues_quantity = models.CharField(max_length=250)
    issues_cumulative = models.CharField(max_length=250)
    issues_remarks = models.CharField(max_length=250)
    net_balance = models.CharField(max_length=250)
    date_added = models.DateField()


class Issuance(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    emp_name = models.ForeignKey(Employee)
    emp_username = models.CharField(max_length=255)
    emp_code = models.CharField(max_length=255)
    join_date = models.CharField(max_length=255)
    department = models.ForeignKey(ManageMasters)
    location = models.CharField(max_length=255)
    supervisor = models.CharField(max_length=255)
    issuance_date = models.CharField(max_length=255)
    items = models.ForeignKey(ManageItems)
    quantity = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    added_on = models.DateTimeField()



class ItemDesignationwise(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    designation_id = models.ForeignKey(ManageMasters)
    items_id = models.ForeignKey(ManageItems)
    second = models.IntegerField()
    added_on = models.DateTimeField()



class ItemRequisition(models.Model):
     # AutoField?
    type = models.CharField(max_length=50)
    parentid = models.CharField(max_length=255)
    issuance_type = models.CharField(max_length=255)
    _emloyees_id = models.ForeignKey(Employee)
    discount = models.CharField(max_length=255)
    discountval = models.CharField(max_length=255)
    emp_name = models.CharField(max_length=255)
    emp_code = models.CharField(max_length=255)
    department = models.ForeignKey(ManageMasters)
    designation = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    supervisor = models.CharField(max_length=255)
    request_date = models.CharField(max_length=255)
    items = models.ForeignKey(ManageItems)
    unit_price = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    approver = models.CharField(max_length=255)
    approve_date = models.DateField()
    store_id = models.IntegerField()
    status = models.CharField(max_length=255)
    stores_status = models.IntegerField()
    returned = models.IntegerField()
    remaining = models.IntegerField()
    designationwise = models.IntegerField()
    penality_amount = models.IntegerField()
    returned_date = models.DateField()
    timestamp = models.DateTimeField()


class K1Details(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    st_no = models.CharField(max_length=255)
    pan_no = models.CharField(max_length=255)
    epf_no = models.CharField(max_length=255)
    esi_no = models.CharField(max_length=255)
    cin_no = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    invioce_no = models.CharField(max_length=255)
    service_tax = models.CharField(max_length=255)
    edu_cess = models.CharField(max_length=255)
    high_edu_cess = models.CharField(max_length=255)
    condition1 = models.TextField()
    condition2 = models.TextField()
    condition3 = models.TextField()
    condition4 = models.TextField()
    condition5 = models.TextField()


class LeaveManagement(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    leave_name = models.CharField(max_length=255)
    leave_code = models.CharField(max_length=50)
    payment = models.CharField(max_length=50)
    noofleaves = models.IntegerField()
    emp_apply = models.CharField(max_length=50)
    emp_beyond = models.CharField(max_length=50)
    leavetype = models.CharField(max_length=50)
    percentage = models.IntegerField()
    stop_period = models.IntegerField()
    status = models.IntegerField()


class LeavePeriod(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()
    status = models.IntegerField()
    timestamp = models.DateTimeField()


class LeavesAbsents(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    date = models.DateField()
    father_name = models.CharField(max_length=255)
    designation = models.ForeignKey(ManageMasters)
    applied_for = models.CharField(max_length=255)
    applied_month = models.CharField(max_length=255)
    from_date = models.DateField()
    to_date = models.DateField()
    reason_for = models.TextField()
    send_to = models.CharField(max_length=255)
    contact_at = models.CharField(max_length=255)
    contact_po = models.CharField(max_length=255)
    contact_dist = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=255)
    date_time = models.DateTimeField()


class LoanTypes(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    loan_type = models.CharField(max_length=255)
    description = models.TextField()
    added_on = models.DateField()
    type = models.CharField(max_length=50)


class LoansAdvances(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    designation = models.ForeignKey(ManageMasters)
    loan_limit = models.CharField(max_length=255)
    added_on = models.DateField()


class LoansCalculation(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    emp_id = models.ForeignKey(Employee)
    loan_id = models.CharField(max_length=255)
    loan_type = models.CharField(max_length=255)
    loan_amount = models.CharField(max_length=255)
    inst_month = models.CharField(max_length=255)
    inst_no = models.CharField(max_length=255)
    inst_paid = models.CharField(max_length=255)
    inst_amount = models.CharField(max_length=255)
    balance = models.CharField(max_length=255)
    added_on = models.DateField()


class LocDesgMaster(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    date = models.DateField()
    designation = models.ForeignKey(ManageMasters)
    basic = models.CharField(max_length=50)
    hra = models.CharField(max_length=50)
    conveyance = models.CharField(max_length=50)
    others = models.CharField(max_length=50)
    epf = models.CharField(max_length=50)
    esi = models.CharField(max_length=50)
    perday_wage = models.CharField(max_length=50)
    status = models.CharField(max_length=255)
    added_on = models.DateField()



class LocationIncentive(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    added_on = models.DateField()



class LocationIncharge(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    client_id = models.ForeignKey('ManageClients')
    work_order = models.ForeignKey(ClientBilling)
    employee_id = models.ForeignKey(Employee)
    status = models.IntegerField()
    datetime = models.DateTimeField()


class LocationInchargeSalaries(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    emp_id = models.ForeignKey(Employee)
    month = models.IntegerField()
    year = models.IntegerField()
    total_amount = models.IntegerField()
    thousands = models.IntegerField()
    fivehundreds = models.IntegerField()
    hundreds = models.IntegerField()
    fifties = models.IntegerField()
    twenties = models.IntegerField()
    tens = models.IntegerField()
    fives = models.IntegerField()
    twos = models.IntegerField()
    ones = models.IntegerField()
    generated_id = models.IntegerField()
    datetime = models.DateTimeField()



class LocationsalarySettings(models.Model):
     # AutoField?
    designation = models.IntegerField()
    clientid = models.ForeignKey('ManageClients')
    work_order = models.ForeignKey(ClientBilling)
    amount = models.CharField(max_length=255)
    status = models.IntegerField()
    datetime = models.DateTimeField()


class Locdesg(models.Model):
     # AutoField?
    designation = models.CharField(max_length=255)
    desg_id = models.IntegerField()
    status = models.IntegerField()


class LocpayIncentive(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    work_order = models.ForeignKey(ClientBilling)
    designation = models.ForeignKey(ManageMasters)
    perday = models.CharField(max_length=255)
    date = models.DateField()
    status = models.IntegerField()
    added_on = models.DateTimeField()
    generated_id = models.IntegerField()



class LoginDetails(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    send_to = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    messages = models.TextField()
    added_on = models.DateField()


class Logins(models.Model):
     # AutoField?
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    _emloyees_id = models.ForeignKey(Employee)
    datetime = models.DateTimeField()


class LoyalityBonous(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    loyality_bonous = models.CharField(max_length=255)
    loyality_period = models.IntegerField()
    description = models.TextField()
    date = models.DateField()




class ManageClientsLocations(models.Model):
     # AutoField?
    cid = models.IntegerField()
    name = models.CharField(max_length=250)
    loc_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    parentid = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    entry_date = models.DateField()
    from_date = models.DateField()
    to_date = models.DateField()
    authorised_person = models.CharField(max_length=250)
    panno = models.CharField(max_length=20)
    tanno = models.CharField(max_length=20)
    auth_designation = models.CharField(max_length=20)
    guard_deployement = models.DateField()
    email = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)
    status = models.IntegerField()
    added_on = models.DateField()
    login_type = models.IntegerField()
    created = models.IntegerField()



class ManageDepartments(models.Model):
     # AutoField?
    name = models.CharField(max_length=250)
    datetime = models.DateTimeField()



class ManageQuotation(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    client = models.ForeignKey('ManageClients')
    branch = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    designation = models.ForeignKey(ManageMasters)
    work_order_no = models.ForeignKey(ClientBilling)
    authorised = models.CharField(max_length=255)
    additional = models.CharField(max_length=255)
    date = models.DateField()






class Masters(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    master_name = models.CharField(max_length=255)
    master_desc = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    added_on = models.DateTimeField()


class Menus(models.Model):
     # AutoField?
    name = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    icon = models.CharField(max_length=150)
    is_active = models.IntegerField()
    sub_menu = models.IntegerField()
    actions_id = models.IntegerField()
    inner_menu = models.IntegerField()
    sub_menu_id = models.IntegerField()
    menu_id = models.IntegerField()
    employee = models.IntegerField()



class MobilePatrolling(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    patrolling_person = models.CharField(max_length=255)
    date = models.DateField()
    clientid = models.ForeignKey('ManageClients')
    employeeid = models.ForeignKey(Employee)
    mobile = models.CharField(max_length=255)
    time1 = models.CharField(max_length=20)
    time2 = models.CharField(max_length=20)
    time3 = models.CharField(max_length=20)
    time4 = models.CharField(max_length=20)
    time5 = models.CharField(max_length=20)
    time6 = models.CharField(max_length=20)
    time7 = models.CharField(max_length=20)
    call_1 = models.CharField(max_length=255)
    call_2 = models.CharField(max_length=255)
    call_3 = models.CharField(max_length=255)
    call_4 = models.CharField(max_length=255)
    call_5 = models.CharField(max_length=255)
    call_6 = models.CharField(max_length=255)
    call_7 = models.CharField(max_length=255)



class MoneytransferPettycash(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    date = models.DateField()
    petty_account = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    approver = models.CharField(max_length=255)
    approved_by = models.CharField(max_length=255)
    approved_on = models.DateField()


class Noticeboard(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    date = models.DateField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    post_to = models.CharField(max_length=255)
    post_count = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    from_date = models.DateField()
    to_date = models.DateField()
    notice_type = models.CharField(max_length=255)
    alert_status = models.IntegerField()
    date_time = models.DateTimeField()
    send_by = models.IntegerField()
    status = models.IntegerField()



class Notifications(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    notification = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    added_on = models.DateTimeField()



class OtherBenefits(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    benefit_name = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    added_on = models.DateField()



class Outward(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    status = models.CharField(max_length=250)
    date = models.DateField()
    time = models.CharField(max_length=50)
    gatepass_no = models.CharField(max_length=50)
    invoice_no = models.CharField(max_length=250)
    stock_to = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    courier_name = models.CharField(max_length=250)
    pod_number = models.CharField(max_length=250)
    number_plate = models.CharField(max_length=250)
    driver_name = models.CharField(max_length=255)
    driver_contact = models.CharField(max_length=255)
    per_name = models.CharField(max_length=255)
    approver = models.CharField(max_length=255)
    ref_nonref = models.CharField(max_length=50)
    items = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    approve = models.IntegerField()
    date_time = models.DateTimeField()
    alert_status = models.IntegerField()



class Overtime(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    _emloyees_id = models.ForeignKey(Employee)
    designation = models.ForeignKey(ManageMasters)
    total_hours_ot = models.IntegerField()
    total_hours = models.IntegerField()
    absent_count = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    total_days = models.IntegerField()
    leave_count = models.IntegerField()
    overtime_hours = models.IntegerField()
    own_ot = models.IntegerField()
    inctot = models.IntegerField()
    tots = models.IntegerField()
    work_order = models.CharField(max_length=150)
    generated_id = models.IntegerField()



class OvertimeGenerated(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    page = models.IntegerField()
    page_limit = models.IntegerField()
    page_current_limit = models.IntegerField()



class OvertimePayment(models.Model):
     # AutoField?
    ot_id = models.IntegerField()
    employee_id = models.ForeignKey(Employee)
    date = models.DateField()
    payment = models.CharField(max_length=50)
    cqno = models.CharField(max_length=50)
    cqdate = models.DateField()
    bank = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    amount = models.IntegerField()
    voucherno = models.CharField(max_length=50)
    status = models.CharField(max_length=50)



class Patrolling(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    patrolling_officer = models.IntegerField()
    patrolling_officer2 = models.IntegerField()
    patrolling_time = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=255)
    dress_up = models.CharField(max_length=255)
    wear_belt = models.CharField(max_length=255)
    wear_tie = models.CharField(max_length=255)
    wear_shoes = models.CharField(max_length=255)
    b_polish = models.CharField(max_length=255)
    cap_batch = models.CharField(max_length=255)
    wear_cap = models.CharField(max_length=255)
    wear_whistle = models.CharField(max_length=255)
    wear_saving = models.CharField(max_length=255)
    wear_haircut = models.CharField(max_length=255)
    sleeping = models.CharField(max_length=255)
    post_out = models.CharField(max_length=255)
    wear_icard = models.CharField(max_length=255)
    wear_socks = models.CharField(max_length=255)
    dozzing = models.CharField(max_length=255)
    tabaco = models.CharField(max_length=255)
    date = models.DateField()
    loc_assign = models.CharField(max_length=50)



class PattycashAccounts(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    description = models.TextField()
    auth_person = models.CharField(max_length=255)
    added_on = models.DateField()



class Payment(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    client_name = models.ForeignKey('ManageClients')
    branch_name = models.CharField(max_length=255)
    payment_date = models.DateField()
    work_order = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    added_on = models.DateField()



class PaymentCollection(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    company_id = models.ForeignKey(K1Details)
    type = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    date = models.DateField()
    work_order = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    cqno = models.CharField(max_length=50)
    cqdate = models.CharField(max_length=50)
    bank = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    status = models.CharField(max_length=255)
    added_on = models.DateField()



class PaymentReceiptIncharge(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    prepared_by = models.IntegerField()
    achead = models.IntegerField()
    paidby = models.IntegerField()
    receivedby = models.IntegerField()
    salary = models.FloatField()
    incentive = models.FloatField()
    barekrent = models.FloatField()
    others = models.FloatField()
    subtotal = models.FloatField()
    advance = models.FloatField()
    balance = models.FloatField()
    month = models.IntegerField()
    year = models.IntegerField()
    thousands = models.IntegerField()
    fivehundreds = models.IntegerField()
    hundreds = models.IntegerField()
    fifties = models.IntegerField()
    twenties = models.IntegerField()
    tens = models.IntegerField()
    fives = models.IntegerField()
    twos = models.IntegerField()
    ones = models.IntegerField()
    datetime = models.DateTimeField()
    siteincharge = models.IntegerField()
    status = models.IntegerField()
    remarks = models.TextField()
    final_amount = models.IntegerField()



class PaymentsTransfers(models.Model):
     # AutoField?
    database_table = models.CharField(max_length=50)
    database_table_id = models.IntegerField()
    vendor_id = models.ForeignKey(VendorWorkshop)
    paid_amount = models.IntegerField()
    invoice_number = models.CharField(max_length=150)
    payment_type = models.CharField(max_length=50)
    cqno = models.CharField(max_length=50)
    cqdate = models.DateField()
    bank = models.CharField(max_length=250)
    branch = models.CharField(max_length=250)
    online_type = models.CharField(max_length=250)
    reference_number = models.CharField(max_length=250)
    datetime = models.DateTimeField()



class PayscaleSetting(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    designation = models.ForeignKey(ManageMasters)
    below_salary = models.CharField(max_length=255)
    full_salary = models.CharField(max_length=255)
    date = models.DateField()



class PoliceVerificationForm(models.Model):
    guid = models.IntegerField(primary_key=True)
    parentid = models.IntegerField()
    full_name = models.CharField(max_length=250)
    father_name = models.CharField(max_length=250)
    present_address = models.TextField()
    permanent_address = models.TextField()
    residence_no = models.CharField(max_length=250)
    office_no = models.CharField(max_length=250)
    mobile_no = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=250)
    family_father = models.CharField(max_length=250)
    family_mother = models.CharField(max_length=250)
    family_husband = models.CharField(max_length=250)
    family_brother = models.CharField(max_length=250)
    family_sister = models.CharField(max_length=250)
    parent_occupation = models.CharField(max_length=250)
    fullname_of_the_employer = models.CharField(max_length=250)
    identification_mark = models.TextField()
    arrested = models.CharField(max_length=250)
    purpose_for_requiring = models.TextField()
    period_of_verification = models.CharField(max_length=250)
    place_of_stay = models.CharField(max_length=250)
    locality_verification = models.CharField(max_length=250)
    date_added = models.IntegerField()



class PurchaseOrder(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    store_id = models.ForeignKey(ManageStores)
    item_name = models.ForeignKey(ManageItems)
    vendor = models.ForeignKey(VendorWorkshop)
    item_price = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    refno = models.CharField(max_length=255)
    status = models.IntegerField()
    date = models.DateField()
    delivery_date = models.DateField()
    delivery_mode = models.CharField(max_length=255)
    payment_mode = models.CharField(max_length=255)
    credit_days = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    discount = models.CharField(max_length=255)
    initiated_by = models.ForeignKey(Employee)
    approved_by = models.CharField(max_length=255)
    added_on = models.DateTimeField()



class PurchaseRequisition(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    added_on = models.DateField()
    store_id = models.ForeignKey(ManageStores)
    vendor = models.ForeignKey(VendorWorkshop)
    orderno = models.CharField(max_length=255)
    orderno_value = models.IntegerField()
    initiated_by = models.ForeignKey(Employee)
    items = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    approved_by = models.CharField(max_length=255)
    approved_on = models.CharField(max_length=255)
    info1 = models.IntegerField()
    day1 = models.IntegerField()
    info2 = models.IntegerField()
    day2 = models.IntegerField()
    info3 = models.IntegerField()
    day3 = models.IntegerField()
    timestamp = models.DateTimeField()
    clarify = models.TextField()
    answer = models.TextField()


class ReferenceIncentive(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    status = models.IntegerField()
    date = models.DateField()
    amount = models.CharField(max_length=255)



class ReferencePayment(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    reference_id = models.ForeignKey(PaymentsTransfers)
    emp_id = models.ForeignKey(Employee)
    amount = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    month_year = models.CharField(max_length=255)
    date = models.DateTimeField()



class ReturnStock(models.Model):
    pid = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=50)
    parentid = models.IntegerField()
    employee_id = models.ForeignKey(Employee)
    item_id = models.ForeignKey(PurchaseOrder)
    designation_id = models.ForeignKey(ManageMasters)
    _item_requisition_id = models.ForeignKey(PurchaseRequisition)
    returned_stock = models.IntegerField()
    remarks_stock = models.TextField()
    reason_stock = models.CharField(max_length=30)
    reusable = models.CharField(max_length=30)
    penality_charges = models.CharField(max_length=30)
    penality_amount_stock = models.IntegerField()
    returned_date_stock = models.DateField()
    siteincharge = models.IntegerField()
    status_add = models.IntegerField()
    datetime = models.DateTimeField()



class ReturnStockVendor(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    vendor_id = models.IntegerField()
    item_id = models.IntegerField()
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    price = models.IntegerField()
    remarks = models.TextField()
    mode = models.CharField(max_length=150)
    courier_no = models.CharField(max_length=150)
    return_date = models.DateField()
    reference_no = models.CharField(max_length=100)
    approved_by = models.CharField(max_length=150)
    datetime = models.DateTimeField()
    courier_name = models.CharField(max_length=50)
    pod_number = models.CharField(max_length=50)
    number_plate = models.CharField(max_length=50)
    driver_name = models.CharField(max_length=50)
    driver_contact = models.CharField(max_length=50)
    per_name = models.CharField(max_length=50)
    return_time = models.CharField(max_length=50)
    gatepass_no = models.CharField(max_length=50)
    in_date = models.DateField()
    in_time = models.CharField(max_length=50)
    remarks_gp = models.CharField(max_length=255)



class SalAssignment(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    client_name = models.ForeignKey('ManageClients')
    work_order_no = models.ForeignKey(ClientBilling)
    month = models.IntegerField()
    year = models.IntegerField()
    supervisor = models.IntegerField()
    salary = models.FloatField()
    payment_salary = models.FloatField()
    balance_salary = models.FloatField()
    incentive = models.FloatField()
    payment_incentive = models.FloatField()
    balance_incentive = models.FloatField()
    house_rent = models.FloatField()
    payment_house_rent = models.FloatField()
    balance_house_rent = models.FloatField()
    voucher = models.FloatField()
    payment_ottotal = models.FloatField()
    balance_ottotal = models.FloatField()
    others = models.FloatField()
    payment_others = models.FloatField()
    balance_others = models.FloatField()
    totamount = models.FloatField()
    payment_totamount = models.FloatField()
    balance_totamount = models.FloatField()
    datetime = models.DateTimeField()



class SalAssignmentEmps(models.Model):
     # AutoField?
    psa_id = models.ForeignKey(SalAssignment)
    _emloyees_id = models.ForeignKey(Employee)
    net_pay = models.FloatField()
    hra = models.FloatField()
    ot_got = models.FloatField()
    paid_mess = models.FloatField()
    cash_return = models.FloatField()
    incentive_ind = models.FloatField()
    net_pay_total = models.FloatField()
    hra_total = models.FloatField()
    ot_got_total = models.FloatField()
    incentive_ind_total = models.FloatField()
    paid_mess_total = models.FloatField()


class Salaries(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    _emloyees_id = models.ForeignKey(Employee)
    designation = models.ForeignKey(ManageMasters)
    supervisor = models.IntegerField()
    month_year = models.CharField(max_length=50)
    month = models.IntegerField()
    year = models.IntegerField()
    work_days = models.IntegerField()
    paid_leaves = models.IntegerField()
    total_days = models.IntegerField()
    total_hours = models.FloatField()
    basic = models.IntegerField()
    cal_basic = models.FloatField()
    hra = models.FloatField()
    washing = models.FloatField()
    other = models.FloatField()
    bonus = models.FloatField()
    annual_bonus = models.FloatField()
    loyality_bonus = models.FloatField()
    total_allowances = models.FloatField()
    epf = models.FloatField()
    esi = models.FloatField()
    fines = models.IntegerField()
    advances = models.FloatField()
    loans = models.FloatField()
    other_deductions = models.FloatField()
    total_deductions = models.FloatField()
    net_pay = models.FloatField()
    payment_status = models.CharField(max_length=50)
    datetime = models.DateTimeField()
    generated_id = models.IntegerField()
    work_order = models.CharField(max_length=150)
    conveyance = models.FloatField()
    pt = models.FloatField()
    tds = models.IntegerField()



class SalariesGenerated(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    designation = models.ForeignKey(ManageMasters)
    from_date = models.DateField()
    from_month = models.IntegerField()
    from_year = models.IntegerField()
    to_date = models.IntegerField()
    to_month = models.IntegerField()
    to_year = models.IntegerField()
    from_final_date = models.DateField()
    to_final_date = models.DateField()
    from_year_month = models.CharField(max_length=250)
    to_year_month = models.CharField(max_length=250)
    status = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    page = models.IntegerField()
    page_limit = models.IntegerField()
    page_current_limit = models.IntegerField()
    otnot = models.IntegerField()
    otallow = models.IntegerField()



class SalaryDisbursement(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    salary_type = models.CharField(max_length=255)
    client_id = models.ForeignKey('ManageClients')
    payment_to = models.CharField(max_length=255)
    emp_id = models.ForeignKey(Employee)
    emp_name = models.CharField(max_length=255)
    emp_code = models.CharField(max_length=255)
    designation = models.ForeignKey(ManageMasters)
    salary_month = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    incentive = models.CharField(max_length=255)
    voucher = models.CharField(max_length=255)
    house_rent = models.CharField(max_length=255)
    loan_amount = models.CharField(max_length=255)
    absent_amount = models.CharField(max_length=255)
    overtime_amount = models.CharField(max_length=255)
    final_amount = models.CharField(max_length=255)
    paid_amount = models.CharField(max_length=255)
    balance_amount = models.CharField(max_length=255)


class SalaryFixed(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    designation = models.ForeignKey(ManageMasters)
    amount = models.CharField(max_length=255)



class SalaryPaymentTransactions(models.Model):
    cash = "Cash"
    cheque = "Cheque"
    payment_method_choices = ((cash, "Cash"), (cheque, "Cheque"))
    salary_id = models.ForeignKey(Salaries)
    _emloyees_id = models.ForeignKey(Employee)
    voucherno = models.CharField(max_length=50)
    date = models.DateField()
    payment = models.CharField(max_length=50, choices=payment_method_choices)
    cqno = models.CharField(max_length=50)
    cqdate = models.DateField()
    bank = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    amount = models.IntegerField()


class ScaleDifference(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    scale_difference = models.CharField(max_length=255)
    effective_date = models.DateField()
    added_on = models.DateTimeField()


class Sendsms(models.Model):
     # AutoField?
    parentid = models.IntegerField()
    send_to = models.IntegerField()
    message = models.TextField()
    sms_no = models.CharField(max_length=255)
    number = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()


class Shifts(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.CharField(max_length=255)
    shift_name = models.CharField(max_length=255)
    from_time = models.CharField(max_length=255)
    to_time = models.CharField(max_length=255)
    status = models.CharField(max_length=25, choices=status_choices)
    added_on = models.DateTimeField()



class StipendDisbursement(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    paid = "Paid"
    partly_paid = "Partly Paid"
    not_paid = "Not Paid"
    payment_choices = ((active, "Active"), (inactive, "Inactive"))
    cash = "Cash"
    cheque = "Cheque"
    payment_method_choices = ((cash, "Cash"), (cheque, "Cheque"))
    
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=25, choices=status_choices)
    trainee_id = models.ForeignKey(Employee)
    session_id = models.ForeignKey(TrainingSession)
    payment_amt = models.CharField(max_length=255)
    paid_amount = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=25, choices=payment_choices)
    payment_method = models.CharField(max_length=25, choices=payment_method_choices)
    cheque_no = models.CharField(max_length=255)
    cheque_date = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    added_on = models.DateField()



class StipendTrainee(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=25, choices=status_choices)
    session_id = models.ForeignKey(TrainingSession)
    trainer_name = models.ForeignKey(Employee)
    location = models.CharField(max_length=255)
    training_days = models.CharField(max_length=255)
    perday_price = models.CharField(max_length=255)


class StockUpdate(models.Model):
     # AutoField?
    item = models.IntegerField()
    name = models.CharField(max_length=250)
    invoiceno = models.ForeignKey(ClientInvoice)
    invoice_date = models.DateField()
    quantity = models.IntegerField()



class Stocks(models.Model):
     # AutoField?
    vendor_id = models.ForeignKey(VendorWorkshop)
    store_id = models.ForeignKey(ManageStores)
    items = models.IntegerField()
    quantity = models.IntegerField()
    date_added = models.DateTimeField()


class StocksTransactions(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    _stocks_id = models.ForeignKey(Stocks)
    store_id = models.ForeignKey(ManageStores)
    vendor_id = models.ForeignKey(VendorWorkshop)
    employee_id = models.ForeignKey(Employee)
    quantity = models.IntegerField()
    _item_requisition_id = models.ForeignKey(ItemRequisition)
    _return_stock_id = models.ForeignKey(ReturnStock)
    datetime = models.DateTimeField()
    status_add = models.IntegerField()
    vendor_status = models.CharField(max_length=20, choices=status_choices)


class Submenus(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    menu_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    is_active = models.CharField(max_length=255)
    inner_menu = models.IntegerField()



class SuperAdmin(models.Model):
    super_admin_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)


class Supporticket(models.Model):
    slow = "Webpage slow"
    error = "Error in application"
    other = "Other"
    design = "Design"
    new_feature = "New Feature"
    
    open = "Open"
    closed = "Closed"

    status_choices = ((open, "Open"), (closed, "Closed"))
    status = models.CharField(max_length=30,
                                  choices=status_choices, default = open
                                  )
    category_choices = ((slow, "Webpage slow"), (error, "Error in application"), (design, "Design"), (new_feature, "New Feature"), (other, "Other"))
    category = models.CharField(max_length=30,
                                  choices=category_choices, null = True
                                  )
    
    medium = "Medium"
    urgent = "Urgent"
    
    priority_choices = ((medium, "Medium"),(urgent, "Urgent")) 
    priority = models.CharField(max_length=30,
                                  choices=priority_choices, null = True
                                  )
    owner = models.ForeignKey('k1emp.Employee')
    
    message = models.TextField(null =  False)
    created = models.DateTimeField(editable=False)
    approved = "Approved"
    rejected = "Rejected"

    action_choices = ((approved, "Approved"), (rejected, "Rejected"))
    action = models.CharField(max_length=30,
                                  choices=action_choices, null = True
                                  )
    supportfile = models.ImageField(upload_to="ticketsimages", null = True, blank = True)
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        return super(Supporticket, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.id
        
    
class SupporticketAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Supporticket._meta.fields]


class TaskManagement(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    normal = "Normal"
    priority = "Priority"
    urgent = "Urgent"
    priority_choices = ((normal, "Normal"), (priority, "Priority"), (urgent, "Urgent"))
    
    parentid = models.CharField(max_length=255)
    task = models.CharField(max_length=255)
    task_summery = models.CharField(max_length=255)
    assign_to = models.ForeignKey(Employee)
    assigned_by = models.CharField(max_length=255)
    status = models.CharField(max_length=25, choices=status_choices)
    assigned_on = models.DateField()
    assigned_time = models.CharField(max_length=255)
    time_duration = models.CharField(max_length=255)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=255)
    time_taken = models.CharField(max_length=255)
    start_date = models.DateField()
    starttime = models.TimeField()
    date_time = models.DateTimeField()
    priority = models.CharField(max_length=50, choices=priority_choices)
    taskremarks = models.TextField()


class TraineeAttendence(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255)
    trainee_id = models.ForeignKey(Employee)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    status = models.CharField(max_length=25, choices=status_choices)



class UploadWorkorder(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=25, choices=status_choices)
    client_name = models.ForeignKey('ManageClients')
    branch = models.CharField(max_length=255)
    order_name = models.CharField(max_length=255)
    order_no = models.CharField(max_length=255)
    order_date = models.DateField()
    order_price = models.CharField(max_length=255)
    order_upload = models.FileField(upload_to="documents")


class UserAccess(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    permission_id = models.CharField(max_length=255)
    menu_id = models.IntegerField()
    sub_menu_id = models.IntegerField()
    added_on = models.DateField()



class UserPermission(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255)
    status = models.CharField(max_length=25, choices=status_choices)
    permission_name = models.CharField(max_length=255)
    description = models.TextField()
    added_on = models.DateField()


class UsersLog(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255)
    login_type = models.CharField(max_length=255)
    login_id = models.CharField(max_length=255)
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField()
    loggedip = models.CharField(max_length=255)  # Field name made lowercase.

class Visitor(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    guid = models.IntegerField(primary_key=True)
    parentid = models.CharField(max_length=255)
    visitor_name = models.CharField(max_length=250)
    from_company = models.CharField(max_length=250)
    from_address = models.TextField()
    contact_number = models.CharField(max_length=255)
    emailid = models.CharField(max_length=250)
    staff_guid = models.CharField(max_length=250)
    purpose = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    avaliability = models.CharField(max_length=10)
    alternate_person = models.IntegerField()
    date_added = models.DateField()
    alert_status = models.CharField(max_length=20, choices=status_choices)
    visit_date_time = models.DateTimeField()
    update_person = models.CharField(max_length=100)
    remarks = models.TextField()
    out_time = models.TimeField()


class Washings(models.Model):
     # AutoField?
    start_amount = models.IntegerField()
    end_amount = models.IntegerField()
    limit_amount = models.IntegerField()
    limit_amount_months = models.IntegerField()
    limit_months = models.IntegerField()
    datetime = models.DateTimeField()


    

class ManageClients(models.Model):
    parentid = models.CharField(max_length=20)
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    status = models.CharField(max_length=30,
                                  choices=status_choices
                                  )
    
    login_type = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to="clientphotos")
    clientid = models.IntegerField()
    client_name = models.CharField(max_length=255)
    client_code = models.CharField(max_length=50)
    client_code_num = models.IntegerField()
    propreitor = models.CharField(max_length=50)
    entry_date = models.DateField()
    from_date = models.DateField()
    to_date = models.DateField()
    authorised_person = models.CharField(max_length=50)
    auth_designation = models.CharField(max_length=50)
    authorised_email = models.CharField(max_length=20)
    authorised_phone = models.CharField(max_length=50)
    authorised_mobile = models.CharField(max_length=50)
    panno = models.CharField(max_length=50)
    tanno = models.CharField(max_length=50)
    service_tax = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    designation = models.ForeignKey('ManageMasters')
    site_incharge = models.CharField(max_length=255)
    guard_deployement = models.DateField()
    rate = models.CharField(max_length=255)
    client_location = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    added_on = models.DateField()
    stax = models.IntegerField()
    created = models.IntegerField()

