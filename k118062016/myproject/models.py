# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib import admin
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
#import webcam.admin
#from webcam.fields import CameraField
from jsignature.mixins import JSignatureFieldsMixin
from smart_selects.db_fields import ChainedForeignKey

class JSignatureModel(JSignatureFieldsMixin):
    name = models.CharField(max_length=200, null=True, blank=True)
import urllib

import urllib2


'''class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now(null=True, blank=True)
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)
        
        


    

class Employee(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    name = models.CharField(_('name'), max_length=30, blank=True)
    phone = models.CharField(max_length = 20, blank = False, null = False)
    
    parentid = models.CharField(max_length=20)
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    status = models.CharField(max_length=30,
                                  choices=status_choices
                                  )
    male = "Male"
    female = "Female"
    gender_choices = ((male, "Male"), (female, "Female"))
    gender = models.CharField(max_length=10,
                                  choices=gender_choices
                                  )
    empcode = models.CharField(max_length=30)
    department = models.CharField(max_length=50, null=True, blank=True)
    client_location = models.CharField(max_length=50, null=True, blank=True)
    designation = models.CharField(max_length=50, null=True, blank=True)
    reporting_auth = models.CharField(max_length=50, null=True, blank=True)
    #reference_by = models.ForeignKey('Employee', related_name='referredby')
    photo = models.ImageField(upload_to="empphotos")
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    home_address1 = models.CharField(max_length=255, null=True, blank=True)
    joining_date = models.DateField(null = True, blank = True)
    home_address2 = models.CharField(max_length=255, null=True, blank=True)
    policestation = models.CharField(max_length=50, null=True, blank=True)
    district = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    panno = models.CharField(max_length=50, null=True, blank=True)
    aadhar = models.CharField(max_length=50, null=True, blank=True)
    esic = models.CharField(max_length=50, null=True, blank=True)
    epf = models.CharField(max_length=50, null=True, blank=True)
    work_phone = models.CharField(max_length=50, null=True, blank=True)
    work_phoneext = models.CharField(max_length=10)
    home_phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    fax = models.CharField(max_length=50, null=True, blank=True)
    home_email = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(null = True)
    birthplace = models.CharField(max_length=100)
    note = models.CharField(max_length=255, null=True, blank=True)
    father_name = models.CharField(max_length=100)
    father_age = models.IntegerField(null = True)
    mother_name = models.CharField(max_length=100)
    mother_age = models.IntegerField(null = True)
    spouse_name = models.CharField(max_length=100)
    spouse_age = models.IntegerField(null = True)
    brother_name = models.CharField(max_length=100)
    brother_no = models.CharField(max_length=50, null=True, blank=True)
    sister_no = models.CharField(max_length=50, null=True, blank=True)
    sister_name = models.CharField(max_length=100)
    year_school = models.CharField(max_length=20)
    year_college = models.CharField(max_length=20)
    school_college = models.CharField(max_length=100)
    exam_passed = models.CharField(max_length=20)
    qualification = models.CharField(max_length=20)
    subjects = models.CharField(max_length=255, null=True, blank=True)
    division = models.CharField(max_length=20)
    dateofjoining = models.DateField(null = True)
    dateofleaving = models.DateField(null = True)
    parent_occupation = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    identification_mark = models.CharField(max_length=255, null=True, blank=True)
    arrested_details = models.CharField(max_length=255, null=True, blank=True)
    requiring_certificate = models.CharField(max_length=255, null=True, blank=True)
    verification_period = models.CharField(max_length=255, null=True, blank=True)
    staying_place = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateField(null = True, blank = True)
    separation_date = models.DateField(null = True)
    reason = models.CharField(max_length=255, null=True, blank=True)
    separation_status = models.CharField(max_length=255, null=True, blank=True)
    issue_items = models.CharField(max_length=255, null=True, blank=True)
    alert_status = models.IntegerField(null = True)
    sep_date_time = models.DateTimeField(null = True)
    sept_alert = models.IntegerField(null = True)
    reference_paid_status = models.IntegerField(null = True)
    separation_net_pay = models.FloatField(null = True)
    separation_paid_amount = models.FloatField(null = True)
    issue_items_count = models.IntegerField(null = True)
    pol_ver_time = models.CharField(max_length=50, null=True, blank=True)
    pol_ver_remarks = models.CharField(max_length=255, null=True, blank=True)
    chest_expanded = models.CharField(max_length=50, null=True, blank=True)
    chest_unexpanded = models.CharField(max_length=50, null=True, blank=True)
    height = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    caste = models.CharField(max_length=30)
    religion = models.CharField(max_length=30)
    bike = models.CharField(max_length=30)
    dlicence = models.CharField(max_length=20)
    dtype = models.CharField(max_length=20)
    licence = models.CharField(max_length=20)
    prosecuted = models.CharField(max_length=255, null=True, blank=True)
    service_code = models.CharField(max_length=150)
    service_rank = models.CharField(max_length=255, null=True, blank=True)
    service_name = models.CharField(max_length=150)
    pre_village = models.CharField(max_length=50, null=True, blank=True)
    pre_post = models.CharField(max_length=50, null=True, blank=True)
    pre_dist = models.CharField(max_length=50, null=True, blank=True)
    pre_policestation = models.CharField(max_length=50, null=True, blank=True)
    pre_state = models.CharField(max_length=50, null=True, blank=True)
    pre_pincode = models.CharField(max_length=50, null=True, blank=True)
    perm_village = models.CharField(max_length=50, null=True, blank=True)
    perm_post = models.CharField(max_length=50, null=True, blank=True)
    perm_dist = models.CharField(max_length=50, null=True, blank=True)
    perm_policestation = models.CharField(max_length=50, null=True, blank=True)
    perm_state = models.CharField(max_length=50, null=True, blank=True)
    perm_pincode = models.CharField(max_length=50, null=True, blank=True)
    coming = models.IntegerField(null = True)
    cutting = models.IntegerField(null = True)
    approve_bonus = models.IntegerField(null = True)
    proof_type = models.CharField(max_length=20)
    ot_allowed = models.IntegerField(null = True)
    sendsms = models.IntegerField(null = True)
    emp_sign = models.ImageField(upload_to="empsign")
    interview_with = models.CharField(max_length=50, null=True, blank=True)
    interview_remarks = models.CharField(max_length=255, null=True, blank=True)
    post_applied_for =  models.CharField(max_length=30)
    #trainer_name = models.ForeignKey('Employee', related_name='trainedby')
    

    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = self.name
        return full_name.strip(null=True, blank=True)

    def get_short_name(self):
        "Returns the short name for the user."
        return self.name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])
        
'''        
class PomeMasters(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    master_name = models.CharField(max_length=255, null=True, blank=True)
    master_desc = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.master_name
    class Meta:
        verbose_name_plural = 'Masters Type'


class PomeManageMasters(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    master_id = models.ForeignKey(PomeMasters, null=True, blank=True)
    dept_id = models.CharField(max_length = 100, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateTimeField(null=True, blank=True)
    

    def __unicode__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Manage Masters'

class PomeEmloyees(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    general = "General"
    obc = "OBC"
    sc = "SC"
    st = "ST"
    caste_choices = ((general, "General"), (obc, "OBC"), (sc, 'SC'), (st, 'ST'))
    christian = "Christian"
    hindu = "Hindu"
    muslim = "Muslim"
    sikh = "Sikh"
    religion_choices = ((christian, "Christian"), (hindu, "Hindu"), (muslim, 'Muslim'), (sikh, 'Sikh'))
    database_table = models.CharField(max_length=150, null=True, blank=True)
    database_table_id = models.IntegerField(null=True, blank=True)
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=status_choices, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    type_id = models.CharField(max_length=255, null=True, blank=True)
    employeno = models.CharField(max_length=50, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    client_location = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    first_location = models.CharField(max_length=255, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    reporting_auth = models.CharField(max_length=255, null=True, blank=True, verbose_name="Reporting Authority")
    reference_by = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to="media/", null=True, blank=True)
    firstname = models.CharField(max_length=255, null=True, blank=True)
    middlename = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    shortname = models.CharField(max_length=250, null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    home_address1 = models.CharField(max_length=255, null=True, blank=True)
    home_address2 = models.CharField(max_length=255, null=True, blank=True)
    policestation = models.CharField(max_length=50, null=True, blank=True)
    district = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    panno = models.CharField(max_length=50, null=True, blank=True)
    aadhar = models.CharField(max_length=50, null=True, blank=True)
    esic = models.CharField(max_length=50, null=True, blank=True)
    epf = models.CharField(max_length=50, null=True, blank=True, verbose_name="EPF")
    work_phone = models.CharField(max_length=255, null=True, blank=True)
    work_phoneext = models.CharField(max_length=255, null=True, blank=True)
    home_phone = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    fax = models.CharField(max_length=255, null=True, blank=True)
    work_email = models.CharField(max_length=255, null=True, blank=True)
    home_email = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateField(null=True, blank=True, verbose_name="DOB")
    birthplace = models.CharField(max_length=255, null=True, blank=True)
    sin_ssn = models.CharField(max_length=255, null=True, blank=True, verbose_name="SSN/SIN")
    note = models.CharField(max_length=255, null=True, blank=True)
    father_name = models.CharField(max_length=255, null=True, blank=True)
    father_age = models.IntegerField(null=True, blank=True)
    mother_name = models.CharField(max_length=255, null=True, blank=True)
    mother_age = models.IntegerField(null=True, blank=True)
    husband_wife = models.CharField(max_length=255, null=True, blank=True)
    husband_wife_age = models.IntegerField(null=True, blank=True)
    issue = models.CharField(max_length=50, null=True, blank=True)
    brother = models.CharField(max_length=255, null=True, blank=True)
    brother_no = models.CharField(max_length=50, null=True, blank=True, verbose_name="No of Brothers")
    sister_no = models.CharField(max_length=50, null=True, blank=True, verbose_name="No of Sisters")
    sister = models.CharField(max_length=255, null=True, blank=True)
    years = models.CharField(max_length=255, null=True, blank=True)
    school_college = models.CharField(max_length=255, null=True, blank=True, verbose_name="School/College")
    exam_passed = models.CharField(max_length=255, null=True, blank=True)
    subjects = models.CharField(max_length=255, null=True, blank=True)
    division = models.CharField(max_length=255, null=True, blank=True)
    dateofjoining = models.CharField(max_length=255, null=True, blank=True, verbose_name="Date of joining")
    dateofleaving = models.CharField(max_length=255, null=True, blank=True, verbose_name="Date of leaving")
    parent_occupation = models.CharField(max_length=255, null=True, blank=True)
    details_employe = models.CharField(max_length=255, null=True, blank=True)
    identification_mark = models.CharField(max_length=255, null=True, blank=True)
    arrested_details = models.CharField(max_length=255, null=True, blank=True)
    requiring_certificate = models.CharField(max_length=255, null=True, blank=True)
    verification_period = models.CharField(max_length=255, null=True, blank=True)
    staying_place = models.CharField(max_length=255, null=True, blank=True)
    eminent_persons = models.CharField(max_length=255, null=True, blank=True)
    eminent_persons2 = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.CharField(max_length=255, null=True, blank=True)
    separation_date = models.CharField(max_length=255, null=True, blank=True)
    reason = models.CharField(max_length=255, null=True, blank=True)
    separation_status = models.IntegerField(null=True, blank=True)
    issue_items = models.IntegerField(null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    alert_status = models.IntegerField(null=True, blank=True)
    sep_date_time = models.DateTimeField(null=True, blank=True)
    sept_alert = models.IntegerField(null=True, blank=True)
    reference_paid_status = models.IntegerField(null=True, blank=True)
    separation_net_pay = models.FloatField(null=True, blank=True)
    separation_paid_amount = models.FloatField(null=True, blank=True)
    issue_items_count = models.IntegerField(null=True, blank=True)
    pol_ver_time = models.CharField(max_length=50, null=True, blank=True)
    pol_ver_remarks = models.CharField(max_length=255, null=True, blank=True)
    chest_expanded = models.CharField(max_length=255, null=True, blank=True)
    chest_unexpanded = models.CharField(max_length=255, null=True, blank=True)
    height = models.CharField(max_length=255, null=True, blank=True)
    weight = models.CharField(max_length=255, null=True, blank=True)
    caste = models.CharField(max_length=255,choices=caste_choices, null=True, blank=True)
    religian = models.CharField(max_length=255,choices=religion_choices, null=True, blank=True)
    bike = models.CharField(max_length=255, null=True, blank=True)
    dlicence = models.CharField(max_length=255, null=True, blank=True)
    dtype = models.CharField(max_length=255, null=True, blank=True)
    licence = models.CharField(max_length=255, null=True, blank=True)
    prosecuted = models.CharField(max_length=255, null=True, blank=True)
    service_code = models.CharField(max_length=150, null=True, blank=True)
    service_rank = models.CharField(max_length=255, null=True, blank=True)
    service_name = models.CharField(max_length=150, null=True, blank=True)
    pre_village = models.CharField(max_length=255, null=True, blank=True, verbose_name="Present Village")
    pre_post = models.CharField(max_length=255, null=True, blank=True, verbose_name="Present Post")
    pre_dist = models.CharField(max_length=255, null=True, blank=True, verbose_name="Present District")
    pre_policestation = models.CharField(max_length=255, null=True, blank=True, verbose_name="Present Police Station")
    pre_state = models.CharField(max_length=255, null=True, blank=True, verbose_name="Present State")
    pre_pincode = models.CharField(max_length=255, null=True, blank=True, verbose_name="Present Pincode")
    perm_village = models.CharField(max_length=255, null=True, blank=True, verbose_name="Permenant Village")
    perm_post = models.CharField(max_length=255, null=True, blank=True, verbose_name="Permenant Post")
    perm_dist = models.CharField(max_length=255, null=True, blank=True, verbose_name="Permenant District")
    perm_policestation = models.CharField(max_length=255, null=True, blank=True, verbose_name="Permenant Police Station")
    perm_state = models.CharField(max_length=255, null=True, blank=True, verbose_name="Permenant State")
    perm_pincode = models.CharField(max_length=255, null=True, blank=True, verbose_name="Permenant Pincode")
    coming = models.IntegerField(null=True, blank=True)
    cutting = models.IntegerField(null=True, blank=True)
    approve_bonus = models.IntegerField(null=True, blank=True)
    proof_type = models.CharField(max_length=20, null=True, blank=True)
    ot_allowed = models.IntegerField(null=True, blank=True)
    sendsms = models.IntegerField(null=True, blank=True, verbose_name="Send SMS")
    notfield = models.IntegerField(null=True, blank=True)
    emp_sign = models.CharField(max_length=255, null=True, blank=True)
    secondlot = models.CharField(max_length = 200, null=True, blank=True)
    uan_no = models.CharField(max_length=200, verbose_name='UAN NO', null=True, blank=True)
    bank_no = models.CharField(max_length=200, verbose_name='Bank Account Number')
    name_as_on_bank = models.CharField(max_length=200)
    ifsc_code = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=200)
    branch_name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return '%s %s - %s' % (self.firstname, self.lastname, self.employeno)
   
    def police_verification(self):
        return '<a href="/police_verification_id/%s/"> %s </a>'  % (self.id, self.employeno)
    police_verification.allow_tags = True

    class Meta:
        verbose_name_plural = 'Add | Manage Employees'



class PomeManageClients(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    tax_applicable = "Tax Applicable"
    tax_not_applicable = "Tax Not Applicable"
    stax_choices = ((tax_applicable, "Tax Applicable"), (tax_not_applicable, "Tax Not Applicable"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    login_type = models.CharField(max_length=255, null=True, blank=True)
    profile_pic = models.ImageField(upload_to="photos", null=True, blank=True)
    clientid = models.IntegerField(null=True, blank=True)
    client_name = models.CharField(max_length=255, null=True, blank=True)
    client_code_num = models.IntegerField(null=True, blank=True, verbose_name="Client Code Number")
    client_code = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    propreitor = models.CharField(max_length=255, null=True, blank=True, verbose_name="Proprietor")
    entry_date = models.DateField(null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    authorised_person = models.CharField(max_length=255, null=True, blank=True)
    auth_designation = models.CharField(max_length=50, null=True, blank=True)
    authorised_email = models.CharField(max_length=20, null=True, blank=True)
    authorised_phone = models.CharField(max_length=50, null=True, blank=True)
    authorised_mobile = models.CharField(max_length=50, null=True, blank=True)
    panno = models.CharField(max_length=50, null=True, blank=True, verbose_name="PAN NO")
    tanno = models.CharField(max_length=50, null=True, blank=True, verbose_name="TAN NO")
    service_tax = models.CharField(max_length=50, choices=stax_choices, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    site_incharge = models.CharField(max_length=255, null=True, blank=True)
    guard_deployement = models.DateField(null=True, blank=True, verbose_name="Guard Deployment")
    rate = models.CharField(max_length=255, null=True, blank=True)
    client_location = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=status_choices, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)
    stax = models.CharField(max_length = 20, null=True, blank=True)
    created = models.IntegerField(null=True, blank=True)
    GSTIN = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.client_name

    class Meta:
        verbose_name_plural = 'Add | Manage Clients'


    def calc_client_code(self, x):
        cnames = self.client_name.split(' ')
        client_code = ""
        for i in cnames:
            client_code = client_code + i[0]
        guarddep = self.guard_deployement.strftime('%m%Y')
        client_code = client_code + guarddep[:2] + guarddep[4:] + str(self.id)
        print "id is :", client_code
        return client_code.upper()

    def save(self, *args, **kwargs):
        super(PomeManageClients, self).save(*args, **kwargs)
        self.client_code = self.calc_client_code(self)
        super(PomeManageClients, self).save(*args, **kwargs)



class PomeManageClientsLocations(models.Model):
     # AutoField?
    cid = models.ForeignKey(PomeManageClients, verbose_name="CID")
    name = models.CharField(max_length=250)
    loc_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Location Name")
    address = models.CharField(max_length=50, null=True, blank=True)
    parentid = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    entry_date = models.DateField(null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    authorised_person = models.CharField(max_length=250, null=True, blank=True)
    panno = models.CharField(max_length=20, null=True, blank=True)
    tanno = models.CharField(max_length=20, null=True, blank=True, verbose_name="GSTIN")
    auth_designation = models.CharField(max_length=20, null=True, blank=True, verbose_name="Authorised Designation")
    guard_deployement = models.DateField(null=True, blank=True, verbose_name="Guard Deployment")
    email = models.CharField(max_length=50, null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    zipcode = models.CharField(max_length=20, null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)
    stax = models.CharField(max_length=20, null=True, blank=True, verbose_name="Service Tax")
    login_type = models.IntegerField(null=True, blank=True)
    created = models.IntegerField(null=True, blank=True)
    designation1 =  models.ForeignKey(PomeManageMasters,related_name="designation1", null=True, blank=True)
    payment_rate1 = models.CharField(max_length=250, null=True, blank=True)
    designation2 =  models.ForeignKey(PomeManageMasters,related_name="designation2", null=True, blank=True)
    payment_rate2 = models.CharField(max_length=250, null=True, blank=True)
    designation3 =  models.ForeignKey(PomeManageMasters,related_name="designation3", null=True, blank=True)
    payment_rate3 = models.CharField(max_length=250, null=True, blank=True)
    

    def __unicode__(self):
        return '%s %s' % (self.loc_name, self.name)

    class Meta:
        verbose_name_plural = 'Manage Clients Locations'




class PomeTrainer(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    trainer_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=status_choices, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.trainer_name

    class Meta:
        verbose_name_plural = 'Trainer Settings'


class PomeBiodata(models.Model):
    direct_employee = "Direct Employee"
    send_to_training = "Send to Training"
    not_joined = "Not Joined"
    action_choices = ((direct_employee, "Direct Employee"), (send_to_training, "Send to Training"), (not_joined, 'Not Joined'))
    general = "General"
    obc = "OBC"
    sc = "SC"
    st = "ST"
    caste_choices = ((general, "General"), (obc, "OBC"), (sc, 'SC'), (st, 'ST'))
    christian = "Christian"
    hindu = "Hindu"
    muslim = "Muslim"
    sikh = "Sikh"
    religion_choices = ((christian, "Christian"), (hindu, "Hindu"), (muslim, 'Muslim'), (sikh, 'Sikh'))
    male = "Male"
    female = "Female"
    gender_choices = ((male, "Male"), (female, "Female"))
    
    parentid = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=25, choices=action_choices, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    shortname = models.CharField(max_length=250, null=True, blank=True)
    gender = models.CharField(max_length=50,choices=gender_choices, null=True, blank=True)
    trainee_id = models.CharField(max_length=50, null=True, blank=True)
    mother_name = models.CharField(max_length=255, null=True, blank=True)
    father_name = models.CharField(max_length=255, null=True, blank=True)
    brother_name = models.CharField(max_length=255, null=True, blank=True)
    sister_name = models.CharField(max_length=255, null=True, blank=True)
    fage = models.CharField(max_length=255, null=True, blank=True, verbose_name="Father's age")
    mage = models.CharField(max_length=255, null=True, blank=True, verbose_name="Mother's age")
    #photo = CameraField(format='jpeg', null=True, blank=True, upload_to='media', verbose_name="Photo")
    photo = models.ImageField(upload_to="media", null=True, blank=True, verbose_name="Photo")
    chest_expanded = models.CharField(max_length=255, null=True, blank=True)
    chest_unexpanded = models.CharField(max_length=255, null=True, blank=True)
    height = models.CharField(max_length=255, null=True, blank=True)
    weight = models.CharField(max_length=255, null=True, blank=True)
    identification_mark = models.CharField(max_length=255, null=True, blank=True)
    pre_village = models.CharField(max_length=255, null=True, blank=True, verbose_name="Present Village")
    pre_post = models.CharField(max_length=255, null=True, blank=True, verbose_name="Present Post")
    pre_dist = models.CharField(max_length=255, null=True, blank=True, verbose_name="Present District")
    pre_policestation = models.CharField(max_length=255, null=True, blank=True, verbose_name="Present Police Station")
    pre_state = models.CharField(max_length=255, null=True, blank=True, verbose_name="Present State")
    pre_pincode = models.CharField(max_length=255, null=True, blank=True, verbose_name="Present Pincode")
    perm_village = models.CharField(max_length=255, null=True, blank=True, verbose_name="Permenant Village")
    perm_post = models.CharField(max_length=255, null=True, blank=True, verbose_name="Permenant Post")
    perm_dist = models.CharField(max_length=255, null=True, blank=True, verbose_name="Permenant District")
    perm_policestation = models.CharField(max_length=255, null=True, blank=True, verbose_name="Permenant Police Station")
    perm_state = models.CharField(max_length=255, null=True, blank=True, verbose_name="Permenant State")
    perm_pincode = models.CharField(max_length=255, null=True, blank=True, verbose_name="Permenant Pincode")
    dob = models.DateField(null=True, blank=True, verbose_name="DOB")
    telephone = models.CharField(max_length=255, null=True, blank=True)
    caste = models.CharField(max_length=255,choices=caste_choices, null=True, blank=True)
    religian = models.CharField(max_length=255,choices=religion_choices, null=True, blank=True, verbose_name="Religion")
    mobile = models.CharField(max_length=255, null=True, blank=True)
    bike = models.CharField(max_length=255, null=True, blank=True)
    dlicence = models.CharField(max_length=255, null=True, blank=True, verbose_name="Driving License")
    dtype = models.CharField(max_length=255, null=True, blank=True, verbose_name="Driving License Type")
    licence = models.CharField(max_length=255, null=True, blank=True)
    service_code = models.CharField(max_length=255, null=True, blank=True)
    service_rank = models.CharField(max_length=255, null=True, blank=True)
    service_name = models.CharField(max_length=255, null=True, blank=True)
    brother_no = models.CharField(max_length=255, null=True, blank=True, verbose_name="No of Brothers")
    sister_no = models.CharField(max_length=255, null=True, blank=True, verbose_name="No of Sisters")
    wife_name = models.CharField(max_length=255, null=True, blank=True)
    wife_age = models.CharField(max_length=255, null=True, blank=True)
    issue = models.CharField(max_length=255, null=True, blank=True)
    year = models.CharField(max_length=255, null=True, blank=True)
    school_college = models.CharField(max_length=255, null=True, blank=True, verbose_name="School/College")
    exam_passed = models.CharField(max_length=255, null=True, blank=True)
    subjects = models.CharField(max_length=255, null=True, blank=True)
    division = models.CharField(max_length=255, null=True, blank=True)
    prosecuted = models.CharField(max_length=255, null=True, blank=True)
    other_name1 = models.CharField(max_length=255, null=True, blank=True)
    other_name2 = models.CharField(max_length=255, null=True, blank=True)
    other_village1 = models.CharField(max_length=255, null=True, blank=True)
    other_village2 = models.CharField(max_length=255, null=True, blank=True)
    other_post1 = models.CharField(max_length=255, null=True, blank=True)
    other_post2 = models.CharField(max_length=255, null=True, blank=True)
    other_ps1 = models.CharField(max_length=255, null=True, blank=True)
    other_ps2 = models.CharField(max_length=255, null=True, blank=True)
    other_dist1 = models.CharField(max_length=255, null=True, blank=True)
    other_dist2 = models.CharField(max_length=255, null=True, blank=True)
    other_prof1 = models.CharField(max_length=255, null=True, blank=True)
    other_prof2 = models.CharField(max_length=255, null=True, blank=True)
    other_long1 = models.CharField(max_length=255, null=True, blank=True)
    other_long2 = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)
    post_applied = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    interview_with = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    trainer_name = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    training_session = models.CharField(max_length=255, null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    reference_by = models.ForeignKey(PomeEmloyees, related_name="reference", null=True, blank=True)
    emp_sign = models.ImageField(upload_to="photos", null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return '%s %s- %s' % (self.name, self.last_name, self.trainee_id)
    class Meta:
        verbose_name_plural = 'Bio-Data'

    def image(self):
        return '<img src="/media/%s/" width="100" height="100" />' % (self.photo)
    image.allow_tags = True    

    def calc_trainee_id(self, x):
        tnames = "TRA"
        trainee = tnames
        
        trainee_id = trainee +  str(self.id)
        print "trainee id is :", trainee_id
        return trainee_id.upper()

    def save(self, *args, **kwargs):
        super(PomeBiodata, self).save(*args, **kwargs)
        self.trainee_id = self.calc_trainee_id(self)
        super(PomeBiodata, self).save(*args, **kwargs)
    



class PomeTrainingSession(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    session_name = models.CharField(max_length=255, null=True, blank=True)
    trainer_name = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    place = models.CharField(max_length=255, null=True, blank=True)
    session_straingth = models.CharField(max_length=255, null=True, blank=True)
    total_days = models.CharField(max_length=255, null=True, blank=True)
    training_dates = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateTimeField(null=True, blank=True)
    perday_price = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.session_name
    class Meta:
        verbose_name_plural = 'Training Sessions'



class PomeOjtdeductions(models.Model):
    ojt_employees = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    hours = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    reason = models.CharField(max_length = 100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'OJT Deductions'


class PomeManageItems(models.Model):
    individual = "Individual"
    assignment = "Assignment"
    type_choices = ((individual, "Individual"), (assignment, "Assignment"))
    raw_material = "Raw Material"
    ready_to_use = "Ready To Use"
    category_choices = ((raw_material, "Raw Material"), (ready_to_use, "Ready To Use"))
    pieces = "Pieces"
    meters = "Meters"
    kilogram = "Kilogram"
    litres = "Litres"
    measurement_choices = ((pieces, "Pieces"), (meters, "Meters"), (kilogram, "Kilogram"), (litres, "Litres"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    item_code = models.CharField(max_length=255, null=True, blank=True)
    item_name = models.CharField(max_length=255, null=True, blank=True)
    itemtype = models.CharField(max_length=50, choices=type_choices, null=True, blank=True)
    category = models.CharField(max_length=255,choices=category_choices, null=True, blank=True)
    measurement = models.CharField(max_length=255,choices=measurement_choices, null=True, blank=True)
    threshold_limit = models.CharField(max_length=255, null=True, blank=True)
    unit_price = models.CharField(max_length=255, null=True, blank=True)
    charge_price = models.CharField(max_length=50, null=True, blank=True)
    threshold_to1 = models.ForeignKey(PomeEmloyees, related_name="threshold_to1")
    days1 = models.CharField(max_length=255, null=True, blank=True)
    threshold_to2 = models.CharField(max_length=255, null=True, blank=True)
    days2 = models.CharField(max_length=255, null=True, blank=True)
    threshold_to3 = models.ForeignKey(PomeEmloyees,null=True,blank=True, related_name="threshold_to3")
    days3 = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    initiated_by = models.IntegerField(null=True, blank=True)
    stockitem = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.item_name
    class Meta:
        verbose_name_plural = 'Add Item'
    

    def calc_item_code(self, x):
        cnames = self.item_name
        item_code = cnames
         
        item_code = item_code
        print "id is :", item_code
        return item_code.upper()

    def save(self, *args, **kwargs):
        super(PomeManageItems, self).save(*args, **kwargs)
        self.item_code = self.calc_item_code(self)
        super(PomeManageItems, self).save(*args, **kwargs)




class PomeAcknowledgement(models.Model):
     # AutoField?
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.IntegerField(null=True, blank=True)
    emp_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)

    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
   # emp_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    emp_name = models.CharField(max_length=255, null=True, blank=True)
    emp_code = models.CharField(max_length=255, null=True, blank=True)
    join_date = models.DateField(null=True, blank=True)
    receive_date = models.DateField(null=True, blank=True)
    receive_time = models.TimeField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    training_cost = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=status_choices, null=True, blank=True)
    document = models.FileField(upload_to="documents", null=True, blank=True)
    recept_no = models.CharField(max_length=255, null=True, blank=True)
    recept_date = models.DateField(null=True, blank=True)
    ack_reference_no = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Acknowledgement'

    def save(self, *args, **kwargs):
        self.designation = self.emp_id.designation
        super(PomeAcknowledgement, self).save(*args, **kwargs)

class PomeAcknowledgementDocuments(models.Model):
     # AutoField?
    parentid = models.IntegerField(null=True, blank=True)
    ackn_id = models.CharField(max_length=255, null=True, blank=True)
    upload_documents = models.FileField(upload_to="documents", null=True, blank=True)

    
    
    class Meta:
        verbose_name_plural = 'Manage AcknowledgementDocs'




class PomeActions(models.Model):
     # AutoField?
    name = models.CharField(max_length=250, null=True, blank=True)
    code = models.CharField(max_length=250, null=True, blank=True)

    
    class Meta:
        verbose_name_plural = 'Actions'


class PomeUpload(models.Model):
    photo = "Photo"
    signature = "Signature"
    type_choices = ((photo, "Photo"), (signature, "Signature"))
    employee = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    type = models.CharField(max_length=25, choices=type_choices, null=True, blank=True)
    upload = models.ImageField(upload_to="photos", null=True, blank=True)

    
    class Meta:
        verbose_name_plural = 'Photo or Signature Upload'




class PomeAdvancesTypes(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=status_choices, null=True, blank=True)
    loan_type = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    
    class Meta:
        verbose_name_plural = 'Advance Types'




class PomeAllowanceMaster(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    yes = "Yes"
    no = "No"
    ot_choices = ((yes, "Yes"), (no, "No"))
    percentage = "Percentage"
    number = "Number"
    unit_choices = ((percentage, "Percentage"), (number, "Number"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    employee_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    gross_salary = models.IntegerField(null=True, blank=True)
    basic_salary = models.IntegerField(null=True, blank=True)
    bonus_val = models.CharField(max_length=255, null=True, blank=True, verbose_name="Bonus Value")
    loyality_bonus_val = models.CharField(max_length=52, null=True, blank=True, verbose_name="Loyality Bonus Value")
    loyality_bonus_period = models.IntegerField(null=True, blank=True)
    bonus_unit = models.CharField(max_length=255, null=True, blank=True)
    hra_val = models.CharField(max_length=255, null=True, blank=True, verbose_name="HRA Value")
    hra_unit = models.CharField(max_length=255, null=True, blank=True, verbose_name="HRA Unit")
    others_val = models.CharField(max_length=255, null=True, blank=True, verbose_name="Others Value")
    others_unit = models.CharField(max_length=255, null=True, blank=True)
    washing_val = models.CharField(max_length=255, null=True, blank=True, verbose_name="Washing Value")
    washing_unit = models.CharField(max_length=255, null=True, blank=True)
    epf_val = models.CharField(max_length=255, null=True, blank=True, verbose_name="EPF Value")
    epf_unit = models.CharField(max_length=255,choices=unit_choices, null=True, blank=True)
    epf_emp_val = models.CharField(max_length=255, null=True, blank=True, verbose_name="EPF Employee Value")
    epf_emp_unit = models.CharField(max_length=255,choices=unit_choices, null=True, blank=True, verbose_name="EPF Employee Unit")
    conveyance_val = models.CharField(max_length=255, null=True, blank=True, verbose_name="Conveyance Value")
    conveyance_unit = models.CharField(max_length=255,choices=unit_choices, null=True, blank=True)
    esi_val = models.CharField(max_length=255, null=True, blank=True, verbose_name="ESI Value")
    esi_unit = models.CharField(max_length=255,choices=unit_choices, null=True, blank=True, verbose_name="ESI Unit")
    esi_emp_val = models.CharField(max_length=255, null=True, blank=True, verbose_name="ESI Employee Value")
    esi_emp_unit = models.CharField(max_length=255,choices=unit_choices, null=True, blank=True, verbose_name="ESI Employee Unit")
    percent_basic = models.CharField(max_length=50, null=True, blank=True)
    value_hra = models.CharField(max_length=50, null=True, blank=True, verbose_name="Value HRA")
    value_conveyance = models.CharField(max_length=50, null=True, blank=True)
    value_washing = models.CharField(max_length=50, null=True, blank=True)
    value_bonus = models.CharField(max_length=50, null=True, blank=True)
    value_others = models.CharField(max_length=50, null=True, blank=True)
    perday_wage = models.CharField(max_length=50, null=True, blank=True, verbose_name="per/day Wage")
    otallowed = models.CharField(max_length = 25, choices=ot_choices,null=True, blank=True, verbose_name="OT Allowed")
    ptax_val = models.CharField(max_length=50, null=True, blank=True, verbose_name="P-tax Value")
    ptax_unit = models.CharField(max_length=50,choices=unit_choices, null=True, blank=True, verbose_name="P-tax Unit")
    tds_val = models.CharField(max_length=50, null=True, blank=True, verbose_name="TDS Value")
    tds_unit = models.CharField(max_length=50,choices=unit_choices, null=True, blank=True, verbose_name="TDS Unit")
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    
    class Meta:
        verbose_name_plural = 'Payroll Settings'

    def save(self, *args, **kwargs):
        self.designation = self.employee_id.designation
        super(PomeAllowanceMaster, self).save(*args, **kwargs)


class PomeAnnualbonus(models.Model):
     # AutoField?
    from_month = models.IntegerField(null=True, blank=True)
    to_month = models.IntegerField(null=True, blank=True)
    month_eligible = models.IntegerField(null=True, blank=True)
    limit_months = models.IntegerField(null=True, blank=True)
    percentage = models.FloatField(null=True, blank=True)

    
    class Meta:
        verbose_name_plural = 'Annual Bonus'




class PomeBillingTax(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.IntegerField(null=True, blank=True)
    service_tax = models.CharField(max_length=255, null=True, blank=True)
    edu_cess = models.CharField(max_length=255, null=True, blank=True)
    high_edu_cess = models.CharField(max_length=255, null=True, blank=True)
    swacch_bharat = models.CharField(max_length=10, null=True, blank=True)
    krish_kalyan = models.CharField(max_length=10, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    
    class Meta:
        verbose_name_plural = 'Billing & Tax Settings'






class PomeCalendar(models.Model):
    yes = "Yes"
    no = "No"
    repeat_choices = ((yes, "Yes"), (no, "No"))
    every_day = "Every Day"
    every_week = "Every Week"
    every_month = "Every Month"
    repeat_on_choices = ((every_week, "Every Week"), (every_day,"Every Day"), (every_month, "Every Month"))
    
    title = models.CharField(max_length=160, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    allday = models.CharField(max_length=20, choices=repeat_choices, null=True, blank=True)
    color = models.CharField(max_length=7, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    repeat_type = models.CharField(max_length=20, choices=repeat_choices, null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    repeat_id = models.CharField(max_length=20, choices=repeat_on_choices, null=True, blank=True)


    
    class Meta:
        verbose_name_plural = 'Calendar'



class PomeClientBilling(models.Model):
    authorised = "Authorised"
    additional = "Additional"
    authorised_choices = ((authorised, "Authorised"), (additional, "Additional"))
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    weekly = "Weekly"
    monthly = "Monthly"
    quarterly = "Quarterly"
    semi_anually = "Semi Anually"
    anually = "Anually"
    billing_choices = ((weekly, "Weekly"), (monthly, "Monthly"), (quarterly, "quarterly"), (semi_anually, "Semi Anually"), (anually, "Anually"))
    
    eight = "8"
    nine = "9"
    twelve = "12"
    sixteen = "16"
    hour_choices = ((eight, "8"),(nine, "9"), (twelve, "12"), (sixteen, "16"))    
    parentid = models.IntegerField(null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)
    client_name = models.ForeignKey(PomeManageClients, null=True, blank=True)
    work_order_no = ChainedForeignKey(
		PomeManageClientsLocations, chained_field="client_name", chained_model_field="cid", auto_choose=True
	)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    hour = models.CharField(max_length=255, choices=hour_choices, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    noofpersons = models.IntegerField(null=True, blank=True, verbose_name="Number of Persons")
    rate = models.IntegerField(null=True, blank=True)
    clientrate = models.IntegerField(null=True, blank=True)
    k1rate = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    todate = models.DateField(null=True, blank=True)
    billingperiod = models.CharField(max_length=30, choices =billing_choices, null=True, blank=True)
    authorised = models.CharField(max_length=255, choices=authorised_choices, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    supervisor = models.CharField(max_length=255, null=True, blank=True)
    alert_status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    createdby = models.IntegerField(null=True, blank=True)
    #updatedby = models.ForeignKey(PomeEmloyees)
    updatetime = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.authorised
    class Meta:
        verbose_name_plural = 'Work Order'



class PomeClientAttendance(models.Model):
     # AutoField?
    parentid = models.IntegerField(null=True, blank=True)
    client_id = models.ForeignKey(PomeManageClients, null=True, blank=True)
    work_order = ChainedForeignKey(
		PomeManageClientsLocations, chained_field="client_id", chained_model_field="cid", auto_choose=True
	)
    employee_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    month = models.CharField(max_length=20, null=True, blank=True)
    year = models.CharField(max_length=20, null=True, blank=True)
    one = models.CharField(max_length=20, null=True, blank=True)
    two = models.CharField(max_length=20, null=True, blank=True)
    three = models.CharField(max_length=20, null=True, blank=True)
    four = models.CharField(max_length=20, null=True, blank=True)
    five = models.CharField(max_length=20, null=True, blank=True)
    six = models.CharField(max_length=20, null=True, blank=True)
    seven = models.CharField(max_length=20, null=True, blank=True)
    eight = models.CharField(max_length=20, null=True, blank=True)
    nine = models.CharField(max_length=20, null=True, blank=True)
    ten = models.CharField(max_length=20, null=True, blank=True)
    eleven = models.CharField(max_length=20, null=True, blank=True)
    twelve = models.CharField(max_length=20, null=True, blank=True)
    thirteen = models.CharField(max_length=20, null=True, blank=True)
    fourteen = models.CharField(max_length=20, null=True, blank=True)
    fifteen = models.CharField(max_length=20, null=True, blank=True)
    sixteen = models.CharField(max_length=20, null=True, blank=True)
    seventeen = models.CharField(max_length=20, null=True, blank=True)
    eightteen = models.CharField(max_length=20, null=True, blank=True)
    nineteen = models.CharField(max_length=20, null=True, blank=True)
    twenty = models.CharField(max_length=20, null=True, blank=True)
    twentyone = models.CharField(max_length=20, null=True, blank=True)
    twentytwo = models.CharField(max_length=20, null=True, blank=True)
    twentythree = models.CharField(max_length=20, null=True, blank=True)
    twentyfour = models.CharField(max_length=20, null=True, blank=True)
    twentyfive = models.CharField(max_length=20, null=True, blank=True)
    twentysix = models.CharField(max_length=20, null=True, blank=True)
    twentyseven = models.CharField(max_length=20, null=True, blank=True)
    twentyeight = models.CharField(max_length=20, null=True, blank=True)
    twentynine = models.CharField(max_length=20, null=True, blank=True)
    thirty = models.CharField(max_length=20, null=True, blank=True)
    thirtyone = models.CharField(max_length=20, null=True, blank=True)
    total_hours = models.CharField(max_length=20, null=True, blank=True)
    sessionid = models.CharField(max_length=20, null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
   
    
    class Meta:
        verbose_name_plural = 'Editable Attendance'






class PomeClientBranches(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    client_id = models.ForeignKey(PomeManageClients, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    branch_name = models.CharField(max_length=255, null=True, blank=True)
    branch_addr = models.CharField(max_length=255, null=True, blank=True)
    branch_tele = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.branch_name
        
    class Meta:
        verbose_name_plural = 'Client Branches'



class PomeClientInvoice(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    paid = "Paid"
    not_paid = "Not Paid"
    present_status_choices = ((paid, "Paid"), (not_paid, "Not Paid"))
    
    client_id = models.ForeignKey(PomeManageClients, null=True, blank=True)
    work_order_no = ChainedForeignKey(
		PomeManageClientsLocations, chained_field="client_id", chained_model_field="cid", auto_choose=True
	)
    parentid = models.IntegerField(null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    invoice_no = models.CharField(max_length=50, null=True, blank=True)
    invnumber = models.IntegerField(null=True, blank=True)
    sub_total = models.IntegerField(null=True, blank=True)
    others = models.IntegerField(null=True, blank=True)
    final_total = models.IntegerField(null=True, blank=True)
    stax = models.IntegerField(null=True, blank=True)
    edu_cess = models.IntegerField(null=True, blank=True)
    high_edu_cess = models.IntegerField(null=True, blank=True)
    swacch_bharat = models.IntegerField(null=True, blank=True)
    krish_kalyan = models.IntegerField(null=True, blank=True)
    total_amount = models.IntegerField(null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    sub_total_authorised = models.IntegerField(null=True, blank=True)
    sub_total_additional = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True)
    prtstatus = models.CharField(max_length=20, choices=present_status_choices, null=True, blank=True)

    def __unicode__(self):
        return self.invoice_no
    class Meta:
        verbose_name_plural = 'Client Invoice ST 14%'



class PomeClientInvoiceTransactions(models.Model):
    authorised = "Authorised"
    additional = "Additional"
    authorised_choices = ((authorised, "Authorised"), (additional, "Additional"))
    
    pome_client_invoice_id = models.ForeignKey(PomeClientInvoice, null=True, blank=True)
    client_id = models.ForeignKey(PomeManageClients, null=True, blank=True)
    work_order_no = models.ForeignKey(PomeManageClientsLocations, null=True, blank=True)
    status_auth = models.CharField(max_length=50, choices=authorised_choices, null=True, blank=True)
    no_of_employees = models.IntegerField(null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    hours = models.IntegerField(null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    no_of_employees_want = models.IntegerField(null=True, blank=True)
    no_of_hours_want = models.IntegerField(null=True, blank=True)
    no_of_rate_want = models.IntegerField(null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Invoice Transactions'



class PomeClientPatrolling(models.Model):
     # AutoField?
    parentid = models.IntegerField(null=True, blank=True)
    clientid = models.ForeignKey(PomeManageClients, null=True, blank=True)
    patrollingno = models.CharField(max_length=50, null=True, blank=True)
    employeeid = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.patrollingno
    class Meta:
        verbose_name_plural = 'Client Patrolling'



class PomeClientPaymentTransactions(models.Model):
    cash = "Cash"
    cheque = "Cheque"
    payment_choices = ((cash, "Cash"), (cheque, "Cheque"))
    
    invoice_id = models.ForeignKey(PomeClientInvoice, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    payment = models.CharField(max_length=50, choices=payment_choices, null=True, blank=True)
    cqno = models.CharField(max_length=50, null=True, blank=True)
    cqdate = models.DateField(null=True, blank=True)
    bank = models.CharField(max_length=50, null=True, blank=True)
    branch = models.CharField(max_length=50, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    tds = models.IntegerField(null=True, blank=True)
    otherded = models.IntegerField(null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    work_order_no = models.ForeignKey(PomeManageClientsLocations, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Client Payment Transactions'

class PomeConsultancies(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.IntegerField(null=True, blank=True)
    consultancy_name = models.CharField(max_length=50, null=True, blank=True)
    consultancy_address = models.CharField(max_length=250, null=True, blank=True)
    consultancy_phoneno = models.IntegerField(null=True, blank=True)
    consultancy_emailid = models.CharField(max_length=50, null=True, blank=True)
    contactperson_name = models.CharField(max_length=50, null=True, blank=True)
    contactperson_phoneno = models.CharField(max_length=20, null=True, blank=True)
    contactperson_emailid = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True)

    def __unicode__(self):
        return self.consultancy_name
    class Meta:
        verbose_name_plural = 'Manage Consultancies'

class PomeCustomerFeedback(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    yes = "Yes"
    no = "No"
    customer_choices = ((yes, "Yes"), (no, "No"))
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"    
    incharge_choices = ((one, "1"), (two, "2"),(three, "3"), (four, "4"),(five, "5"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=status_choices, null=True, blank=True)
    customer_id = models.ForeignKey(PomeManageClients, null=True, blank=True)
    customer_name = models.CharField(max_length=255, null=True, blank=True)
    customer_address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    incharge_perform = models.CharField(max_length=25, choices=incharge_choices, null=True, blank=True)
    guard_perform = models.CharField(max_length=25, choices=incharge_choices, null=True, blank=True)
    dressup_rate = models.CharField(max_length=25, choices=incharge_choices, null=True, blank=True)
    record_communicate = models.CharField(max_length=25, choices=incharge_choices, null=True, blank=True)
    head_office_staff = models.CharField(max_length=25, choices=incharge_choices, null=True, blank=True)
    daily_report = models.CharField(max_length=25, choices=incharge_choices, null=True, blank=True)
    night_patrolling = models.CharField(max_length=25, choices=incharge_choices, null=True, blank=True)
    service_quality = models.CharField(max_length=25, choices=customer_choices, null=True, blank=True)
    lodged_compt = models.CharField(max_length=25, choices=customer_choices, null=True, blank=True)
    complaint = models.TextField(null=True, blank=True)
    improvement = models.TextField(null=True, blank=True)
    remarks = models.CharField(max_length=25, choices=incharge_choices, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    work_order_no = work_order_no = ChainedForeignKey(
		PomeManageClientsLocations, chained_field="customer_id", chained_model_field="cid", auto_choose=True
	)

    class Meta:
        verbose_name_plural = 'Customer Feedback'


    def customer_feedback(self):
        return '<a href="/customer_feedback_id/%s/"> %s </a>'  % (self.id, self.id)
    customer_feedback.allow_tags = True


class PomeDefaultAccess(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    permission_id = models.CharField(max_length=255, null=True, blank=True)
    menu_id = models.IntegerField(null=True, blank=True)
    sub_menu_id = models.IntegerField(null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Default Access'

class PomeDefaultAdvances(models.Model):
     # AutoField?
    parentid = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    installment_no = models.IntegerField(null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    first_slot = models.IntegerField(null=True, blank=True)
    second_slot = models.IntegerField(null=True, blank=True)
    first_slot_installment = models.IntegerField(null=True, blank=True)
    second_slot_installment = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Default Advances'

class PomeDisciplineCompliance(models.Model):
    normal = "Normal"
    priority = "Priority"
    serious = "Serious"
    priority_choices = ((normal, "Normal"), (priority, "Priority"), (serious,"Serious"))
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.IntegerField(null=True, blank=True)
    group_id = models.IntegerField(null=True, blank=True)
    initiated_by = models.ForeignKey(PomeEmloyees, related_name="initiated_by", null=True)
    send_date = models.DateField(null=True, blank=True)
    send_time = models.TimeField(null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    send_to = models.ForeignKey(PomeEmloyees,related_name="send_to_whom", null=True)
    priority = models.CharField(max_length=25, choices=priority_choices, null=True, blank=True)
    alert_status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    penality_amount = models.IntegerField(null=True, blank=True)
    reason = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.subject
    class Meta:
        verbose_name_plural = 'Discipline & Compliance'

class PomeDonation(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    cash = "Cash"
    cheque = "Cheque"
    payment_choices = ((cash, "Cash"), (cheque, "Cheque"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    donation_date = models.DateField(null=True, blank=True)
    donation_to = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    payment_method = models.CharField(max_length=25, choices=payment_choices, null=True, blank=True)
    cheque_no = models.CharField(max_length=255, null=True, blank=True)
    cheque_date = models.CharField(max_length=255, null=True, blank=True)
    bank_name = models.CharField(max_length=255, null=True, blank=True)
    branch_name = models.CharField(max_length=255, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Donations'

class PomeEmpAdvances(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    emp_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    month = models.CharField(max_length=255, null=True, blank=True)
    opening_balance = models.CharField(max_length=255, null=True, blank=True)
    issued_adv1 = models.CharField(max_length=255, null=True, blank=True)
    issued_adv2 = models.CharField(max_length=255, null=True, blank=True)
    deduct_adv1 = models.CharField(max_length=255, null=True, blank=True)
    deduct_adv2 = models.CharField(max_length=255, null=True, blank=True)
    closing_balance = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Employee Advances'

class PomeEmpLoans(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=status_choices, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    apply_date = models.DateField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    loan_type = models.CharField(max_length=255, null=True, blank=True)
    emp_id = models.ForeignKey(PomeEmloyees, related_name='employee')
    designation = models.ForeignKey(PomeManageMasters)
    loan_amount = models.CharField(max_length=255, null=True, blank=True)
    reason = models.CharField(max_length=11, null=True, blank=True)
    int_apli = models.CharField(max_length=255, null=True, blank=True)
    interest = models.CharField(max_length=255, null=True, blank=True)
    amount_with_interest = models.CharField(max_length=255, null=True, blank=True)
    instalment_no = models.IntegerField(null=True, blank=True)
    instalment_amount = models.CharField(max_length=255, null=True, blank=True)
    approval = models.ForeignKey(PomeEmloyees, related_name='approval')
    approved_by = models.ForeignKey(PomeEmloyees, related_name='approved_by')
    approved_on = models.DateField(null=True, blank=True)
    default_advance_id = models.IntegerField(null=True, blank=True)
    training_cost_type = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.loan_type
    class Meta:
        verbose_name_plural = 'Loans / Advances Approve'


class PomeEmpLoansTransactions(models.Model):
    paid = "Paid"
    not_paid = "Not Paid"
    partly_paid = "Partly Paid"
    paid_choices = ((paid, "Paid"), (not_paid, "Not Paid"), (partly_paid,"Partly Paid"))
    yes = "Yes"
    no = "No"
    approve_choices = ((yes, "Yes"), (no, "No"))
    advances = "Advances"
    training_cost = "Training Cost"
    type_choices = ((advances, "Advances"), (training_cost, "Training Cost"))
    
    pome_employee_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    pome_emp_loans_id = models.ForeignKey(PomeEmpLoans, null=True, blank=True)
    type = models.CharField(max_length=15,  choices=type_choices, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    instalment_amount = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=25, choices=paid_choices, null=True, blank=True)
    approve_status = models.CharField(max_length=25, choices=approve_choices, null=True, blank=True)
    view_status = models.IntegerField(null=True, blank=True)
    

    class Meta:
        verbose_name_plural = 'Loans/Advances'

class PomeEmployeeAttendence(models.Model):
    present = "Present"
    absent = "Absent"
    leave = "Leave"
    tour = "Tour"
    leave_choices = ((present, "Present"), (absent, "Absent"),(leave, "Leave"), (tour, "Tour"))
    
    employee_id = models.ForeignKey(PomeEmloyees, related_name="employees_id")
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    pome_leaves_absents_id = models.IntegerField(null=True, blank=True)
    applied_for = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    month_year = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=leave_choices, null=True, blank=True)
    work_order = models.ForeignKey(PomeManageClientsLocations, null=True, blank=True)
    actual_hours = models.IntegerField(null=True, blank=True)
    hours = models.IntegerField(null=True, blank=True)
    minutes = models.IntegerField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    locations_id = models.IntegerField(null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    entered = models.ForeignKey(PomeEmloyees, related_name="entered_name", null=True, blank=True)
    intime = models.DateTimeField(null=True, blank=True)
    outtime = models.DateTimeField(null=True, blank=True)
    latitude = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.CharField(max_length=30, null=True, blank=True)
    out_latitude = models.CharField(max_length=30, null=True, blank=True)
    out_longitude = models.CharField(max_length=30, null=True, blank=True)
    inphoto = models.ImageField(upload_to="/media/photos/", null=True, blank=True)
    outphoto = models.ImageField(upload_to="/media/photos/", null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Employee Attendance'

    def image_thumb(self):
    	return '<img src="/media/photos/%s" width="100" height="100" />' % (self.inphoto)
    image_thumb.allow_tags = True

class PomeEmployeeCtc(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    ctc_name = models.CharField(max_length=255, null=True, blank=True)
    ctc_amount = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.ctc_name
    class Meta:
        verbose_name_plural = 'Employee CTC'


class PomeEmployeeExpenditure(models.Model):
    savings = "Savings"
    current = "Current"
    others = "Others"
    account_choices = ((savings, "Savings"), (current, "Current"), (others,"Others"))
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    acc_type = models.CharField(max_length=25, choices=account_choices, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    account_id = models.CharField(max_length=255, null=True, blank=True)
    auth_person = models.CharField(max_length=255, null=True, blank=True)
    emp_name = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    expenditure_name = models.CharField(max_length=255, null=True, blank=True)
    purpose = models.TextField(null=True, blank=True)
    expenditure_amount = models.CharField(max_length=255, null=True, blank=True)
    expenditure_date = models.DateField(null=True, blank=True)
    upload = models.FileField(upload_to ="documents", null=True, blank=True)
    reference_no = models.CharField(max_length=255, null=True, blank=True)
    approver = models.CharField(max_length=255, null=True, blank=True)
    approved_by = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.expenditure_name
    class Meta:
        verbose_name_plural = 'Employee Expenditure'

class PomeEmployeeMovement(models.Model):
    permanent = "Permanent"
    temporary = "Temporary"
    job_choices = ((permanent, "Permanent"), (temporary, "Temporary"))
    new = "New"
    transfer = "Transfer"
    emp_choices = ((new, "New"), (transfer, "Transfer"))
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    client_id = models.ForeignKey(PomeManageClients, null=True, blank=True, verbose_name="Client ID")
    hours = models.IntegerField(null=True, blank=True)
    work_order = ChainedForeignKey(
		PomeManageClientsLocations, chained_field="client_id", chained_model_field="cid", auto_choose=True
	)
    auto_work_order_no = models.CharField(max_length=50, null=True, blank=True)
    order_number = models.IntegerField(null=True, blank=True)
    emp_name = models.ForeignKey(PomeEmloyees, related_name='emp_name', verbose_name="Employee Name")
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    order_by = models.ForeignKey(PomeEmloyees, related_name='order_by', null=True, blank=True)
    order_designation = models.CharField(max_length=250, null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)
    order_time = models.TimeField(null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    from_time = models.TimeField(null=True, blank=True)
    to_time = models.TimeField(null=True, blank=True)
    reason = models.CharField(max_length=255, null=True, blank=True)
    emp_status = models.CharField(max_length=25, choices=emp_choices, null=True, blank=True, verbose_name="Employee Status")
    job_status = models.CharField(max_length=25, choices=job_choices, null=True, blank=True)
    gmo = models.ForeignKey(PomeEmloyees, related_name='gmo', null=True, blank=True, verbose_name="GMO")
    exc_site = models.IntegerField(null=True, blank=True)
    old_site = models.IntegerField(null=True, blank=True)
    allowance = models.CharField(max_length=20, null=True, blank=True)
    reach_update = models.DateTimeField(null=True, blank=True)
    alert_status = models.IntegerField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    reporting_date = models.DateField(null=True, blank=True)
    reporting_time = models.TimeField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Employee Movement'



    def save(self, *args, **kwargs):

	authkey = "73233ADi7CjnTmOXH589d1fa2" # Your authentication key.


        phone = PomeEmloyees.objects.get(employeno  = str(self.emp_name)[-10:])
        x = str(self.work_order).split(" ")[-1]
        print x
        location = PomeManageClientsLocations.objects.get(name = str(x))
        print "phne is ", location

        url = "http://sms.rpsms.in/api/sendhttp.php" # API URL
	sender = "MANASA" 

	route = 4 
        message = "Employee : " + str(self.emp_name) + " moved to " + location.loc_name + " - " + location.name
        mobiles = phone.work_phone
	values = {

              'authkey' : authkey,

              'mobiles' : mobiles,

              'message' : message,

              'sender' : sender,

              'route' : route

              }

        postdata = urllib.urlencode(values) # URL encoding the data here.

	req = urllib2.Request(url, postdata)

	response = urllib2.urlopen(req)

	output = response.read()
        print "sms is " , output

	self.designation = self.emp_name.designation
        super(PomeEmployeeMovement, self).save(*args, **kwargs)

class PomeEmployeePosting(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    emp_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    emp_name = models.CharField(max_length=255, null=True, blank=True)
    emp_code = models.CharField(max_length=255, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    moveto_client = models.CharField(max_length=255, null=True, blank=True)
    client_branch = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    order_by = models.CharField(max_length=255, null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    reason = models.CharField(max_length=255, null=True, blank=True)
    emp_status = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Employee Posting'

class PomeEmployeeSeparations(models.Model):
     # AutoField?
    pome_employees_id = models.ForeignKey(PomeEmloyees)
    separation_net_pay = models.FloatField(null=True, blank=True)
    total_earnings = models.FloatField(null=True, blank=True)
    epf_esi = models.FloatField(null=True, blank=True)
    adp = models.FloatField(null=True, blank=True)
    ldp = models.FloatField(null=True, blank=True)
    other_deductions = models.FloatField(null=True, blank=True)
    sub_total = models.FloatField(null=True, blank=True)
    mess = models.FloatField(null=True, blank=True)
    total_amount = models.FloatField(null=True, blank=True)
    message = models.FloatField(null=True, blank=True)
    training_cost = models.FloatField(null=True, blank=True)
    others_recovery = models.FloatField(null=True, blank=True)
    acknowledge = models.FloatField(null=True, blank=True)
    separation_paid_amount = models.FloatField(null=True, blank=True)
    payment_type = models.CharField(max_length=50, null=True, blank=True)
    cqno = models.CharField(max_length=50, null=True, blank=True)
    cqdate = models.DateField(null=True, blank=True)
    bank = models.CharField(max_length=150)
    branch = models.CharField(max_length=150)
    online_type = models.CharField(max_length=150)
    reference_number = models.CharField(max_length=150)
    datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Employee Separation'


class PomeSeparations(models.Model):
     # AutoField?
    terminated = "Terminated"
    retirement = "Retirement"
    resigned = "Resigned"
    separation_choices = ((terminated, "Terminated"), (retirement, "Retirement"), (resigned, "Resigned"))
    separation_date = models.DateField(null=True, blank=True)
    employees_id = models.ForeignKey(PomeEmloyees)
    designation = models.ForeignKey(PomeManageMasters)
    joining_date = models.DateField(null=True, blank=True)
    vintage = models.CharField(max_length = 255, null=True, blank=True)
    separation_type = models.CharField(max_length=20, choices=separation_choices,null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Separation'


class PomeEmployeeSettlement(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    paid = "Paid"
    not_paid = "Not Paid"
    settlement_choices = ((paid, "Paid"), (not_paid, "Not Paid"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    emp_id = models.ForeignKey(PomeEmloyees)
    emp_name = models.CharField(max_length=255, null=True, blank=True)
    emp_code = models.CharField(max_length=255, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters)
    settlement_amt = models.CharField(max_length=255, null=True, blank=True)
    paid_amount = models.CharField(max_length=255, null=True, blank=True)
    balance_amount = models.CharField(max_length=255, null=True, blank=True)
    settlement_status = models.CharField(max_length=25,choices=settlement_choices,  null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Employee Settlement'

class PomeEodManagement(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    eod_subject = models.TextField(null=True, blank=True)
    eod_data = models.TextField(null=True, blank=True)
    eod_by = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    sended_on = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.eod_subject
    class Meta:
        verbose_name_plural = 'EOD Management'

class PomeEodForward(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    eod_id = models.ForeignKey(PomeEodManagement, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    forward_to = models.ForeignKey(PomeEmloyees, null=True, blank=True)


    class Meta:
        verbose_name_plural = 'EOD Forward'


class PomeStaffType(models.Model):
    office_staff = "Office Staff"
    special_field = "Special Field"    
    staff_choices = ((office_staff, "Office Staff"), (special_field , "Special Field"))
    employee_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    emp_type = models.CharField(max_length=255,choices=staff_choices, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Staff Type'


class PomeExcessAttendance(models.Model):
    employee_id = models.ForeignKey(PomeEmloyees, related_name="employee_id", null=True, blank=True)
    work_order = models.ForeignKey(PomeManageClientsLocations, null=True, blank=True)
    day_balance = models.CharField(max_length=50, blank=True)
    rota_entry = models.CharField(max_length=50, blank=True)
    entered = models.ForeignKey(PomeEmloyees, related_name="entered", null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    date_entered = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Excess Attendance'

class PomeExcessLocAttendance(models.Model):
     # AutoField?
    employee_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    work_order = models.ForeignKey(PomeManageClientsLocations, null=True, blank=True)
    day_balance = models.CharField(max_length=50, null=True, blank=True)
    rota_entry = models.CharField(max_length=50, null=True, blank=True)
    entered = models.ForeignKey(PomeEmloyees, related_name="entereeed", null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    date_entered = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Rota Exceeded'

class PomeFinalReport(models.Model):
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"    
    final_choices = ((one, "1"), (two, "2"),(three, "3"), (four, "4"),(five, "5"))
    selected = "Selected"
    not_selected = "Not_Selected"    
    recom_choices = ((selected, "Selected"), (not_selected, "Not_Selected"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    biodata_id = models.ForeignKey(PomeBiodata, null=True, blank=True)
    attire = models.CharField(max_length=25, choices=final_choices, null=True, blank=True)
    punctuality = models.CharField(max_length=25, choices=final_choices, null=True, blank=True)
    behaviour = models.CharField(max_length=25, choices=final_choices, null=True, blank=True)
    tabacco = models.CharField(max_length=25, choices=final_choices, null=True, blank=True)
    command = models.CharField(max_length=25, choices=final_choices, null=True, blank=True)
    drill = models.CharField(max_length=25, choices=final_choices, null=True, blank=True)
    recom = models.CharField(max_length=25, choices=recom_choices, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Final Report'



class PomeFine(models.Model):
     # AutoField?
    name = models.CharField(max_length=50, null=True, blank=True)
    link = models.CharField(max_length=50, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Fine'

class PomeFineDeductions(models.Model):
     # AutoField?
    parentid = models.IntegerField(null=True, blank=True)
    apply_date = models.DateField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    emp_id = models.ForeignKey(PomeEmloyees, related_name="eemp_id", null=True)
    amount = models.IntegerField(null=True, blank=True)
    selc_fine_ids = models.ForeignKey(PomeFine, null=True, blank=True)
    others = models.CharField(max_length = 200, null=True, blank=True)
    pot = models.ForeignKey(PomeEmloyees, related_name="pot", null=True)
    datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Employee Fine'


class PomeGallery(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    gallery_type = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="photos", null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Gallery'

class PomeGatepass(models.Model):
    stock = "Stock"
    employees = "Employees"    
    gatepass_choices = ((stock, "Stock"), (employees, "Employees"))
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.IntegerField(null=True, blank=True)
    gatepass_type = models.CharField(max_length=25, choices=gatepass_choices, null=True, blank=True)
    out_date = models.DateField(null=True, blank=True)
    out_time = models.TimeField(null=True, blank=True)
    in_date = models.DateField(null=True, blank=True)
    in_time = models.TimeField(null=True, blank=True)
    gateno = models.CharField(max_length=255, null=True, blank=True)
    purpose = models.CharField(max_length=255, null=True, blank=True)
    emp_name = models.ForeignKey(PomeEmloyees, related_name="emplo_name", null=True)
    emp_code = models.CharField(max_length=255, null=True, blank=True)
    gatepass_no = models.CharField(max_length=255, null=True, blank=True)
    gpnumber = models.IntegerField(null=True, blank=True)
    approver = models.CharField(max_length=255, null=True, blank=True)
    issuedby = models.ForeignKey(PomeEmloyees,related_name="issued_by", null=True, blank=True)
    stock_to = models.CharField(max_length=255, null=True, blank=True)
    srno = models.CharField(max_length=255, null=True, blank=True)
    particulars = models.CharField(max_length=255, null=True, blank=True) 
    quantity = models.CharField(max_length=255, null=True, blank=True)
    inventoryno = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    splinstruction = models.CharField(max_length=255, null=True, blank=True)
    update_remarks = models.CharField(max_length=60, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    first_emp = models.IntegerField(null=True, blank=True)
    cancel_remarks = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
          #return self.continent_nm       
          return u'%s %s %s' % (self.gatepass_no, self.emp_name, self.issuedby)
    class Meta:
        verbose_name_plural = 'Employee Gatepass'

    def calc_gatepass_no(self, x):
        gnames = "EMPGP"
        gate = gnames
        
        out_dateee = self.out_date.strftime('%m%Y')
        gatepass_no = gate + out_dateee[:2] + out_dateee[4:] + str(self.id)
        print "gatepass no is :", gatepass_no
        return gatepass_no.upper()

    def save(self, *args, **kwargs):
        super(PomeGatepass, self).save(*args, **kwargs)
        self.gatepass_no = self.calc_gatepass_no(self)
        self.designation = self.emp_name.designation
        super(PomeGatepass, self).save(*args, **kwargs)
  

class PomeGraderateSetting(models.Model):
    grade_a = "Grade A"
    grade_b = "Grade B"
    grade_c = "Grade C"
    grade_d = "Grade D"
    grade_choices = ((grade_a,"Grade A"),(grade_b,"Grade B"), (grade_c,"Grade C"),(grade_d,"Grade D"))
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    grade_name = models.CharField(max_length=25, choices=grade_choices, null=True, blank=True)
    rate = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.grade_name
    class Meta:
        verbose_name_plural = 'Graderate Setting'

class PomeGuardPlacement(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    client_name = models.ForeignKey(PomeManageClients, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    emp_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    employe_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    post_from = models.DateField(null=True, blank=True)
    post_to = models.DateField(null=True, blank=True)
    added_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Guard Placement'

class PomeHolidays(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    full = "Full Day"
    half = "Half Day"
    holiday_choices = ((full, "Full Day"), (half, "Half Day"))
    
    parentid = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    holiday = models.CharField(max_length=20, choices=holiday_choices, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Holidays'

class PomeIncentive(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=status_choices, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)
    purpose = models.CharField(max_length=255, null=True, blank=True)
    totamount = models.IntegerField(null=True, blank=True)
    generated_id = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Designation Incentive Setting'


class PomeIncentiveLoc(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    location = models.ForeignKey(PomeManageClientsLocations, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    purpose = models.CharField(max_length=255, null=True, blank=True)
    totamount = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices,  null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)
    generated_id = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Location Wise Incentive'

class PomeInnermenus(models.Model):
     # AutoField?
    submenu_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    link = models.CharField(max_length=150, null=True, blank=True)
    is_active = models.IntegerField(null=True, blank=True)



class PomeManageStores(models.Model):
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    store_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    contact_no = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return "(%s) %s" % (self.designation, self.name)
    def __unicode__(self):
        return self.store_name
    class Meta:
        verbose_name_plural = 'Manage Stores'

class PomeVendorWorkshop(models.Model):
    vendor = "Vendor"
    workshop = "Workshop"
    type_choices = ((vendor, "Vendor"), (workshop, "Workshop"))
    private_limited = "Private Limited"
    public_limited = "Public Limited"
    soul_propreitor = "Soul Propreitor"
    partnership = "Partnership"
    others = "Others"
    company_type_choices = ((private_limited, "Private Limited"), (public_limited, "Public Limited"),(soul_propreitor, "Soul Propreitor"),
    (partnership, "Partnership"), (others, "Others"))
    savings = "Savings"
    current = "Current"
    others = "Others"
    bank_choices = ((savings, "Savings"), (current, "Current"),(others, "Others"))
        

    login_type = models.CharField(max_length=50,choices=type_choices, null=True, blank=True)
    profile_pic = models.CharField(max_length=255, null=True, blank=True)
    parentid = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, choices=type_choices, null=True, blank=True)
    company_vendor_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    vendor_code = models.CharField(max_length=50, null=True, blank=True)
    registration_no = models.CharField(max_length=255, null=True, blank=True)
    company_type = models.CharField(max_length=255, choices=company_type_choices, null=True, blank=True)
    agreement_date = models.DateField(null=True, blank=True)
    purpose = models.CharField(max_length=50,  null=True, blank=True)
    regd_office_addr = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    pin_code = models.CharField(max_length=255, null=True, blank=True)
    company_email = models.CharField(max_length=255, null=True, blank=True)
    company_telephone = models.CharField(max_length=255, null=True, blank=True)
    fax = models.CharField(max_length=255, null=True, blank=True)
    amc_period = models.CharField(max_length=50, null=True, blank=True, verbose_name="AMC Period")
    tin_tan = models.CharField(max_length=255, null=True, blank=True, verbose_name="TIN TAN")
    service_tax = models.CharField(max_length=50, null=True, blank=True)
    bank_details = models.TextField(null=True, blank=True)
    bank = models.CharField(max_length=255, null=True, blank=True)
    ac_no = models.CharField(max_length=255, null=True, blank=True, verbose_name="Account Number")
    ifsc_no = models.CharField(max_length=255, null=True, blank=True, verbose_name="IFSC Number")
    branch = models.CharField(max_length=255, null=True, blank=True)
    bank_type = models.CharField(max_length=25, choices=bank_choices, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    pan_no = models.CharField(max_length=255, null=True, blank=True, verbose_name="PAN Number")
    designation = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    contact_no = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)
    def __unicode__(self):
        return self.company_vendor_name
    class Meta:
        verbose_name_plural = 'Add | Manage Vendor/Workshop'
    
    def calc_vendor_code(self, x):
        vnames = self.company_vendor_name.split(' ')
        vendor_code = ""
        for i in vnames:
            vendor_code = vendor_code + i[0]
        aggdep = self.agreement_date.strftime('%m%Y')
        vendor_code = vendor_code + aggdep[:2] + aggdep[4:] + str(self.id)
        print "id is :", vendor_code
        return vendor_code.upper()

    def save(self, *args, **kwargs):
        super(PomeVendorWorkshop, self).save(*args, **kwargs)
        self.vendor_code = self.calc_vendor_code(self)
        super(PomeVendorWorkshop, self).save(*args, **kwargs)



class PomeInvoicePaymentDelete(models.Model):
    cash = "Cash"
    cheque = "Cheque"
    payment_choices = ((cash, "Cash"), (cheque, "Cheque"))
    
    invoice_id = models.ForeignKey(PomeClientInvoice, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    payment = models.CharField(max_length=50, choices=payment_choices, null=True, blank=True)
    cqno = models.CharField(max_length=50, null=True, blank=True)
    cqdate = models.DateField(null=True, blank=True)
    bank = models.CharField(max_length=50, null=True, blank=True)
    branch = models.CharField(max_length=50, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    tds = models.IntegerField(null=True, blank=True)
    otherded = models.IntegerField(null=True, blank=True)
    reason = models.CharField(max_length=50, null=True, blank=True)
    entered = models.IntegerField(null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Invoice Payment Delete'


class PomeInwardInvoice(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    invoice_no = models.ForeignKey(PomeClientInvoice, null=True, blank=True)
    vendor_id = models.ForeignKey(PomeVendorWorkshop, null=True, blank=True)
    total_amount = models.IntegerField(null=True, blank=True)
    paid_amount = models.IntegerField(null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)

   
    class Meta:
        verbose_name_plural = 'Inward Invoice'

class PomePurchaseRequisition(models.Model):
    approved = "Approved"
    rejected = "Rejected"
    clarified = "Clarified"
    question = "Question"
    status_choices = ((approved, "Approved"), (rejected, "Rejected"), (clarified, "Clarified"), (question, "Question"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255,choices=status_choices, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)
    store_id = models.ForeignKey(PomeManageStores, null=True, blank=True)
    vendor = models.ForeignKey(PomeVendorWorkshop, null=True, blank=True)
    orderno = models.CharField(max_length=255, null=True, blank=True)
    orderno_value = models.IntegerField(null=True, blank=True)
    initiated_by = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    items = models.ForeignKey(PomeManageItems, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.CharField(max_length=255, null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    approved_by = models.CharField(max_length=255, null=True, blank=True)
    approved_on = models.CharField(max_length=255, null=True, blank=True)
    info1 = models.IntegerField(null=True, blank=True)
    day1 = models.IntegerField(null=True, blank=True)
    info2 = models.IntegerField(null=True, blank=True)
    day2 = models.IntegerField(null=True, blank=True)
    info3 = models.IntegerField(null=True, blank=True)
    day3 = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    clarify = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Purchase Requisition'

class PomeInward(models.Model):
    partially_received = "Partially Received"
    partially_cancelled = "Partially Received and Cancelled"
    cancelled = "Cancelled"
    status_choices = ((partially_received, "Partially Received"), (partially_cancelled, "Partially Cancelled"), (cancelled, "Cancelled"))
    courier = "Couries"
    transport = "Transport"
    person = "Person"
    courier_choices = ((courier, "Courier"), (transport, "Transport"), (person, "Person"))
    
    pome_inward_invoice_id = models.ForeignKey(PomeInwardInvoice, null=True, blank=True)
    status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True)
    pome_purchase_requisition_id = models.IntegerField(null=True, blank=True)
    pome_inward_id = models.IntegerField(null=True, blank=True)
    parentid = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    to = models.ForeignKey(PomeEmloyees, null=True, blank=True, related_name = "to")
    invoice_no = models.ForeignKey(PomeClientInvoice, null=True, blank=True)
    vendor_id = models.ForeignKey(PomeVendorWorkshop, null=True, blank=True)
    store_id = models.ForeignKey(PomeManageStores, null=True, blank=True)
    items = models.ForeignKey(PomeManageItems, null=True)
    ordered = models.IntegerField(null=True, blank=True)
    received = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    total_amount = models.IntegerField(null=True, blank=True)
    paid_amount = models.IntegerField(null=True, blank=True)
    exceed = models.IntegerField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    courier_type = models.CharField(max_length=25, choices=courier_choices, null=True, blank=True)
    courier_name = models.CharField(max_length=250, null=True, blank=True)
    pod_number = models.CharField(max_length=250, null=True, blank=True)
    driver_number_plate = models.CharField(max_length=250, null=True, blank=True)
    driver_name = models.CharField(max_length=250, null=True, blank=True)
    driver_contact = models.CharField(max_length=250, null=True, blank=True)
    per_name = models.CharField(max_length=250, null=True, blank=True)
    per_contact = models.CharField(max_length=250, null=True, blank=True)
    received_by = models.ForeignKey(PomeEmloyees, null=True, blank=True, related_name = "received_by")
    datetime = models.DateTimeField(null=True, blank=True)
    inward_type = models.CharField(max_length=50, null=True, blank=True)
    alert_status = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Inward Others'

class PomeInwardDocuments(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    inward_id = models.ForeignKey(PomeInward, null=True, blank=True)
    upload_documents = models.FileField(upload_to="documents", null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Inward Documents'


class PomeInwardOutwardCourier(models.Model):
    courier = "Couries"
    transport = "Transport"
    person = "Person"
    courier_choices = ((courier, "Courier"), (transport, "Transport"), (person, "Person"))
    
    guid = models.IntegerField(primary_key=True)
    parentid = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=25, choices=courier_choices, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    from_field = models.CharField(max_length=250, null=True, blank=True)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=250, null=True, blank=True)
    courier_type = models.CharField(max_length=250, null=True, blank=True)
    courier_name = models.CharField(max_length=250, null=True, blank=True)
    pod_number = models.CharField(max_length=250, null=True, blank=True)
    received_by = models.CharField(max_length=250, null=True, blank=True)
    dateandtime_delivery = models.DateTimeField(null=True, blank=True)
    courier_particulars = models.TextField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    date_added = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Inward Outward Courier'

class PomeInwardOutwardFixedAssets(models.Model):
    courier = "Couries"
    transport = "Transport"
    person = "Person"
    courier_choices = ((courier, "Courier"), (transport, "Transport"), (person, "Person"))
    
    guid = models.IntegerField(primary_key=True)
    parentid = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=25, choices=courier_choices, null=True, blank=True)
    fixed_date = models.DateField(null=True, blank=True)
    fixed_visitor_name = models.CharField(max_length=250, null=True, blank=True)
    fixed_from = models.CharField(max_length=250, null=True, blank=True)
    fixed_contact = models.CharField(max_length=250, null=True, blank=True)
    fixed_email = models.CharField(max_length=250, null=True, blank=True)
    fixed_whom = models.CharField(max_length=250, null=True, blank=True)
    fixed_purpose = models.CharField(max_length=250, null=True, blank=True)
    fixed_issued_entry_pass = models.CharField(max_length=250, null=True, blank=True)
    fixed_issued_ppe = models.CharField(max_length=250, null=True, blank=True)
    date_added = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.fixed_visitor_name
    class Meta:
        verbose_name_plural = 'Inward Outward Fixed Assets'

class PomeInwardOutwardMaterial(models.Model):
    courier = "Couries"
    transport = "Transport"
    person = "Person"
    courier_choices = ((courier, "Courier"), (transport, "Transport"), (person, "Person"))
    
    guid = models.IntegerField(primary_key=True)
    parentid = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=25, choices=courier_choices, null=True, blank=True)
    receipts_date = models.DateField(null=True, blank=True)
    receipts_invoice_number = models.CharField(max_length=250, null=True, blank=True)
    receipts_received_from = models.CharField(max_length=250, null=True, blank=True)
    receipts_quantity = models.CharField(max_length=250, null=True, blank=True)
    receipts_cumulative = models.CharField(max_length=250, null=True, blank=True)
    receipts_remarks = models.TextField(null=True, blank=True)
    issues_date = models.DateField(null=True, blank=True)
    issues_requisition_no = models.CharField(max_length=250, null=True, blank=True)
    issues_issued_to = models.CharField(max_length=250, null=True, blank=True)
    issues_quantity = models.CharField(max_length=250, null=True, blank=True)
    issues_cumulative = models.CharField(max_length=250, null=True, blank=True)
    issues_remarks = models.CharField(max_length=250, null=True, blank=True)
    net_balance = models.CharField(max_length=250, null=True, blank=True)
    date_added = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Inward Outward Materials'

class PomeIssuance(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    emp_name = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    emp_username = models.CharField(max_length=255, null=True, blank=True)
    emp_code = models.CharField(max_length=255, null=True, blank=True)
    join_date = models.CharField(max_length=255, null=True, blank=True)
    department = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    supervisor = models.CharField(max_length=255, null=True, blank=True)
    issuance_date = models.CharField(max_length=255, null=True, blank=True)
    items = models.ForeignKey(PomeManageItems, null=True, blank=True)
    quantity = models.CharField(max_length=255, null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Issuance'

class PomeItemDesignationwise(models.Model):
     # AutoField?
    parentid = models.IntegerField(null=True, blank=True)
    designation_id = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    items_id = models.ForeignKey(PomeManageItems, null=True, blank=True)
    second = models.IntegerField(null=True, blank=True)
    added_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Item According To Designation'

class PomeItemRequisition(models.Model):
    assignment = "Assignment"
    individual = "Individual"
    type_choices = ((assignment, "Assignment"), (individual, "Individual"))
    free = "Free"
    discount = "Discount"
    issuance_choices = ((free, "Free"), (discount, "Discount"))
    approved = "Approved"
    rejected = "Rejected"
    status_choices = ((approved, "Approved"), (rejected, "Rejected"))
    type = models.CharField(max_length=50,choices=type_choices, null=True, blank=True)
    parentid = models.CharField(max_length=255, null=True, blank=True)
    issuance_type = models.CharField(max_length=255,choices=issuance_choices, null=True, blank=True)
    pome_emloyees_id = models.ForeignKey(PomeEmloyees, null=True,related_name="pome_emloyees_id")
    discount = models.CharField(max_length=255, null=True, blank=True)
    discountval = models.CharField(max_length=255, null=True, blank=True)
    emp_name = models.CharField(max_length=255, null=True, blank=True)
    emp_code = models.CharField(max_length=255, null=True, blank=True)
    department = models.ForeignKey(PomeManageMasters, related_name="dept", null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, related_name="design", null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    supervisor = models.CharField(max_length=255, null=True, blank=True)
    request_date = models.DateField(null=True, blank=True)
    items = models.ForeignKey(PomeManageItems, null=True, blank=True)
    unit_price = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.CharField(max_length=255, null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    reason = models.CharField(max_length=255, null=True, blank=True)
    approver = models.ForeignKey(PomeEmloyees, null=True, blank=True, related_name="approver")
    approve_date = models.DateField(null=True, blank=True)
    store_id = models.ForeignKey(PomeManageStores, null=True, blank=True)
    status = models.CharField(max_length=255,choices=status_choices, null=True, blank=True)
    stores_status = models.IntegerField(null=True, blank=True)
    returned = models.IntegerField(null=True, blank=True)
    remaining = models.IntegerField(null=True, blank=True)
    designationwise = models.IntegerField(null=True, blank=True)
    penality_amount = models.IntegerField(null=True, blank=True)
    returned_date = models.DateField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Item Requisition'

class PomeK1Details(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    st_no = models.CharField(max_length=255, null=True, blank=True)
    pan_no = models.CharField(max_length=255, null=True, blank=True)
    epf_no = models.CharField(max_length=255, null=True, blank=True)
    esi_no = models.CharField(max_length=255, null=True, blank=True)
    cin_no = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    fax = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    invioce_no = models.CharField(max_length=255, null=True, blank=True)
    service_tax = models.CharField(max_length=255, null=True, blank=True)
    edu_cess = models.CharField(max_length=255, null=True, blank=True)
    high_edu_cess = models.CharField(max_length=255, null=True, blank=True)
    condition1 = models.TextField(null=True, blank=True)
    condition2 = models.TextField(null=True, blank=True)
    condition3 = models.TextField(null=True, blank=True)
    condition4 = models.TextField(null=True, blank=True)
    condition5 = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.company_name
    class Meta:
        verbose_name_plural = 'K1 Details'

class PomeLeaveManagement(models.Model):
    paid = "Paid"
    unpaid = "Unpaid"
    payment_choices = ((paid, "Paid"), (unpaid, "Unpaid"))
    leave_accrue = "Leave Accrue"
    carried_forward = "Carried Forward"
    leave_choices = ((leave_accrue, "Leave Accrue"), (carried_forward, "Carried Forward"))
    yes = "Yes"
    no = "No"
    emp_choices = ((yes, "Yes"), (no, "No"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    leave_name = models.CharField(max_length=255, null=True, blank=True)
    leave_code = models.CharField(max_length=50, null=True, blank=True)
    payment = models.CharField(max_length=50,choices=payment_choices, null=True, blank=True)
    noofleaves = models.IntegerField(null=True, blank=True)
    emp_apply = models.CharField(max_length=50,choices=emp_choices, null=True, blank=True)
    emp_beyond = models.CharField(max_length=50,choices=emp_choices, null=True, blank=True)
    leavetype = models.CharField(max_length=50,choices=leave_choices, null=True, blank=True)
    percentage = models.IntegerField(null=True, blank=True)
    stop_period = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.leave_name
    class Meta:
        verbose_name_plural = 'Leave Types'

class PomeLeavePeriod(models.Model):
     # AutoField?
    parentid = models.IntegerField(null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Leave Period'

class PomeLeavesAbsents(models.Model):
    casual_leave = "Casual Leave"
    sick_leave = "Sick Leave"
    previlage_leave = "Previlage Leave"
    leave_choices = ((casual_leave, "Casual Leave"), (sick_leave, "Sick Leave"), (previlage_leave, "Previlage Leave"))
    approved = "Approved"
    not_approved = "Not Approved"
    status_choices = ((approved, "Approved"), (not_approved, "Not Approved"))
    january = "January"
    february = "February"
    march = "March"
    april = "April"
    may = "May"
    june = "June"
    july = "July"
    august = "August"
    september = "September"
    october = "October"
    november = "November"
    december = "December"
    month_choices = ((january, "January"), (february, "February"), (march, "March"), (april, "April"), (may, "May"),(june, "June"), (july, "July"), (august, "August"), (september, "September"), (october, "October"), (november, "November"), (december, "December"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=25,choices=status_choices, null=True, blank=True)
    name = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    father_name = models.CharField(max_length=255, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    applied_for = models.CharField(max_length=25, choices=leave_choices, null=True, blank=True)
    applied_month = models.CharField(max_length=25, choices=month_choices, null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    reason_for = models.TextField(null=True, blank=True)
    send_to = models.CharField(max_length=255, null=True, blank=True)
    contact_at = models.CharField(max_length=255, null=True, blank=True)
    contact_po = models.CharField(max_length=255, null=True, blank=True)
    contact_dist = models.CharField(max_length=255, null=True, blank=True)
    contact_phone = models.CharField(max_length=255, null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Leaves Absents'

class PomeLoanTypes(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    loan_type = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    def __unicode__(self):
        return self.loan_type
    class Meta:
        verbose_name_plural = 'Loan Types'

class PomeLoansAdvances(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    loan_limit = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Loan/Advance Limit Setting'

class PomeLoansCalculation(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    emp_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    loan_id = models.CharField(max_length=255, null=True, blank=True)
    loan_type = models.CharField(max_length=255, null=True, blank=True)
    loan_amount = models.CharField(max_length=255, null=True, blank=True)
    inst_month = models.CharField(max_length=255, null=True, blank=True)
    inst_no = models.CharField(max_length=255, null=True, blank=True)
    inst_paid = models.CharField(max_length=255, null=True, blank=True)
    inst_amount = models.CharField(max_length=255, null=True, blank=True)
    balance = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Loans Calculation'

class PomeLocDesgMaster(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    basic = models.CharField(max_length=50, null=True, blank=True)
    hra = models.CharField(max_length=50, null=True, blank=True)
    conveyance = models.CharField(max_length=50, null=True, blank=True)
    others = models.CharField(max_length=50, null=True, blank=True)
    epf = models.CharField(max_length=50, null=True, blank=True)
    esi = models.CharField(max_length=50, null=True, blank=True)
    perday_wage = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Location Designation Master'

class PomeLocationIncentive(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    date = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Location Not Incentive'

class PomeLocationIncharge(models.Model):
     # AutoField?
    parentid = models.IntegerField(null=True, blank=True)
    client_id = models.ForeignKey(PomeManageClients, null=True, blank=True)
    work_order = ChainedForeignKey(
		PomeManageClientsLocations, chained_field="client_id", chained_model_field="cid", auto_choose=True
	)
    employee_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Location Incharge'


class PomeCutSalary(models.Model):
     # AutoField?
    parentid = models.IntegerField(null=True, blank=True)
    employee = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Cut Salary'

class PomeLocationInchargeSalaries(models.Model):
     # AutoField?
    parentid = models.IntegerField(null=True, blank=True)
    emp_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    total_amount = models.IntegerField(null=True, blank=True)
    thousands = models.IntegerField(null=True, blank=True)
    fivehundreds = models.IntegerField(null=True, blank=True)
    hundreds = models.IntegerField(null=True, blank=True)
    fifties = models.IntegerField(null=True, blank=True)
    twenties = models.IntegerField(null=True, blank=True)
    tens = models.IntegerField(null=True, blank=True)
    fives = models.IntegerField(null=True, blank=True)
    twos = models.IntegerField(null=True, blank=True)
    ones = models.IntegerField(null=True, blank=True)
    generated_id = models.IntegerField(null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Location Incharge Salaries'

class PomeLocationsalarySettings(models.Model):
     # AutoField?
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    clientid = models.ForeignKey(PomeManageClients, null=True, blank=True)
    work_order = models.ForeignKey(PomeManageClientsLocations, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Location Salary Settings'

class PomeLocdesg(models.Model):
     # AutoField?
    designation = models.CharField(max_length=255, null=True, blank=True)
    desg_id = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Location Designation'

class PomeLocpayIncentive(models.Model):
     # AutoField?
    parentid = models.IntegerField(null=True, blank=True)
    work_order = models.ForeignKey(PomeManageClientsLocations, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    perday = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    added_on = models.DateTimeField(null=True, blank=True)
    generated_id = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Location Pay Incentive'

class PomeLoginDetails(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    send_to = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    messages = models.TextField(null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Login Details'
  
class PomeLogins(models.Model):
     # AutoField?
    username = models.CharField(max_length=250, null=True, blank=True)
    password = models.CharField(max_length=250, null=True, blank=True)
    type = models.CharField(max_length=250, null=True, blank=True)
    pome_emloyees_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    def __unicode__(self):
        return self.username
    class Meta:
        verbose_name_plural = 'Logins'

class PomeLoyalityBonous(models.Model):
    six_months = "6 months"
    one_year = "1 year"
    two_years = "2 years"
    three_years = "3 years"
    four_years = "4 years"
    five_years = "5 years"
    loyality_choices = ((six_months, "6 months"), (one_year, "1 year"), (two_years, "2 years"), (three_years, "3 years"), (four_years, "4 years"), (five_years, "5 years"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    loyality_bonous = models.CharField(max_length=255, null=True, blank=True)
    loyality_period = models.CharField(max_length=25, choices=loyality_choices)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    def __unicode__(self):
        return self.loyality_bonous

    class Meta:
        verbose_name_plural = 'Loyality Bonus'





class PomeManageDepartments(models.Model):
     # AutoField?
    name = models.CharField(max_length=250, null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Manage Departments'

class PomeManageQuotation(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    client = models.ForeignKey(PomeManageClients, null=True, blank=True)
    branch = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    work_order_no = ChainedForeignKey(
		PomeManageClientsLocations, chained_field="client", chained_model_field="cid", auto_choose=True
	)
    authorised = models.CharField(max_length=255, null=True, blank=True)
    additional = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    def __unicode__(self):
        return self.subject

    class Meta:
        verbose_name_plural = 'Add | Manage Quotation'






class PomeMenus(models.Model):
     # AutoField?
    name = models.CharField(max_length=150, null=True, blank=True)
    link = models.CharField(max_length=150, null=True, blank=True)
    icon = models.CharField(max_length=150, null=True, blank=True)
    is_active = models.IntegerField(null=True, blank=True)
    sub_menu = models.IntegerField(null=True, blank=True)
    actions_id = models.IntegerField(null=True, blank=True)
    inner_menu = models.IntegerField(null=True, blank=True)
    sub_menu_id = models.IntegerField(null=True, blank=True)
    menu_id = models.IntegerField(null=True, blank=True)
    employee = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Menu'

class PomeMobilePatrolling(models.Model):
    yes = "Yes"
    no = "No"
    call_choices = ((yes, "Yes"), (no, "No"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    patrolling_person = models.ForeignKey(PomeEmloyees, related_name="patrolling_person")
    date = models.DateField(null=True, blank=True)
    clientid = models.ForeignKey(PomeManageClients, null=True, blank=True)
    employeeid = models.ForeignKey(PomeEmloyees, related_name="employeeid", null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    time1 = models.TimeField(null=True, blank=True)
    time2 = models.TimeField(null=True, blank=True)
    time3 = models.TimeField(null=True, blank=True)
    time4 = models.TimeField(null=True, blank=True)
    time5 = models.TimeField(null=True, blank=True)
    time6 = models.TimeField(null=True, blank=True)
    time7 = models.TimeField(null=True, blank=True)
    call_1 = models.CharField(max_length=25, choices=call_choices, null=True, blank=True)
    call_2 = models.CharField(max_length=25,choices=call_choices, null=True, blank=True)
    call_3 = models.CharField(max_length=25,choices=call_choices, null=True, blank=True)
    call_4 = models.CharField(max_length=25,choices=call_choices, null=True, blank=True)
    call_5 = models.CharField(max_length=25,choices=call_choices, null=True, blank=True)
    call_6 = models.CharField(max_length=25,choices=call_choices, null=True, blank=True)
    call_7 = models.CharField(max_length=25,choices=call_choices, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Mobile Patrolling'

    def mobile_patrolling(self):
        return '<a href="/mobile_patrolling/%s/"> %s </a>'  % (self.id, self.id)
    mobile_patrolling.allow_tags = True

    def save(self, *args, **kwargs):
        self.mobile = self.employeeid.mobile
        super(PomeMobilePatrolling, self).save(*args, **kwargs)
   


class PomeMoneytransferPettycash(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    petty_account = models.CharField(max_length=255, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    approver = models.CharField(max_length=255, null=True, blank=True)
    approved_by = models.CharField(max_length=255, null=True, blank=True)
    approved_on = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Money Tranfer Petty Cash'


class PomeNoticeboard(models.Model):
    
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    employees = "Employees"
    vendors = "Vendors"
    clients = "Clients"
    post_choices = ((employees, "Employees"), (vendors, "Vendors"), (clients, "Clients"))

    normal = "Normal"
    urgent = "Urgent"
    priority_choices = ((normal, "Normal"), (urgent, "Urgent"))
   
    notice_board = "Notice Board"
    sms = "SMS"
    email = "Email"
    notice_choices = ((notice_board, "Notice Board"), (sms, "SMS"), (email, "Email"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)
    post_to = models.CharField(max_length=255, null=True, blank=True, choices=post_choices)
    post_count = models.ForeignKey(PomeEmloyees, null=True, related_name="get_employees")
    priority = models.CharField(max_length=255, null=True, blank=True, choices=priority_choices)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    notice_type = models.CharField(max_length=255, null=True, blank=True, choices=notice_choices)
    alert_status = models.IntegerField(null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    send_by = models.ForeignKey(PomeEmloyees, null=True, related_name="send_by")
    status = models.CharField(max_length=20,choices=status_choices, null=True, blank=True)

    def __unicode__(self):
        return self.subject
    class Meta:
        verbose_name_plural = 'Notice Board'

class PomeNotifications(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    notification = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.notification
    class Meta:
        verbose_name_plural = 'Notifications'

class PomeOtherBenefits(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    benefit_name = models.CharField(max_length=255, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.benefit_name
    class Meta:
        verbose_name_plural = 'Other Benefits'


class PomeOutward(models.Model):
    refundable = "Refundable"
    non_refundable = "Non Refundable"
    ref_choices = ((refundable, "Refundable"), (non_refundable, "Non Refundable"))
    courier = "Courier"
    transport = "Transport"
    person = "Person"
    
    type_choices = ((courier, "Courier"), (transport, "Transport"), (person, "Person"))
    parentid = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    gatepass_no = models.CharField(max_length=50, null=True, blank=True)
    invoice_no = models.CharField(max_length=250, null=True, blank=True)
    stock_to = models.ForeignKey(PomeEmloyees,related_name="stock_to", null=True)
    type = models.CharField(max_length=25,choices=type_choices, null=True, blank=True)
    courier_name = models.CharField(max_length=250, null=True, blank=True)
    pod_number = models.CharField(max_length=250, null=True, blank=True)
    number_plate = models.CharField(max_length=250, null=True, blank=True)
    driver_name = models.CharField(max_length=255, null=True, blank=True)
    driver_contact = models.CharField(max_length=255, null=True, blank=True)
    per_name = models.ForeignKey(PomeEmloyees,related_name="per_name", null=True)
    approver = models.ForeignKey(PomeEmloyees,related_name="approver_name", null=True)
    ref_nonref = models.CharField(max_length=50,choices=ref_choices, null=True, blank=True)
    items = models.ForeignKey(PomeManageItems, null=True, blank=True)
    quantity = models.CharField(max_length=255, null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
    reason = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    approve = models.IntegerField(null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    alert_status = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Outward Management'

    def out_gatepass_no(self, x):
        gnames = "OUTGP"
        gate = gnames
        
        out_date = self.date.strftime('%m%Y')
        gatepass_no = gate + out_date[:2] + out_date[4:] + str(self.id)
        print "gatepass no is :", gatepass_no
        return gatepass_no.upper()

    def save(self, *args, **kwargs):
        super(PomeOutward, self).save(*args, **kwargs)
        self.gatepass_no = self.out_gatepass_no(self)
        super(PomeOutward, self).save(*args, **kwargs)
  

class PomeOvertime(models.Model):
     # AutoField?
    parentid = models.IntegerField(null=True, blank=True)
    pome_emloyees_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    total_hours_ot = models.IntegerField(null=True, blank=True)
    total_hours = models.IntegerField(null=True, blank=True)
    absent_count = models.IntegerField(null=True, blank=True, verbose_name="Total Ot earnings")
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    total_days = models.IntegerField(null=True, blank=True)
    leave_count = models.IntegerField(null=True, blank=True, verbose_name="Total Salary earnings")
    overtime_hours = models.IntegerField(null=True, blank=True)
    own_ot = models.IntegerField(null=True, blank=True)
    inctot = models.IntegerField(null=True, blank=True)
    tots = models.IntegerField(null=True, blank=True)
    work_order = models.ForeignKey(PomeManageClientsLocations, null=True, blank=True)
    generated_id = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Incentive Disbursement' 
    
    def calc_tots(self, x):
        total_hours = self.total_hours
        ot_hours = self.overtime_hours
        tots = ""
        tots = total_hours  + ot_hours
        print "tot :", tot
        return tots

    def save(self, *args, **kwargs):
        super(PomeOvertime, self).save(*args, **kwargs)
        self.tots = self.calc_tots(self)
        super(PomeOvertime, self).save(*args, **kwargs)

   

class PomeOvertimeGenerated(models.Model):
     # AutoField?
    parentid = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    page = models.IntegerField(null=True, blank=True)
    page_limit = models.IntegerField(null=True, blank=True)
    page_current_limit = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Overtime Generated'

class PomeOvertimePayment(models.Model):
     # AutoField?
    ot_id = models.ForeignKey(PomeOvertime)
    employee_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    payment = models.CharField(max_length=50, null=True, blank=True)
    cqno = models.CharField(max_length=50, null=True, blank=True)
    cqdate = models.DateField(null=True, blank=True)
    bank = models.CharField(max_length=50, null=True, blank=True)
    branch = models.CharField(max_length=50, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    voucherno = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Overtime Payment'


class PomePatrolling(models.Model):
    day = "Day"
    night = "Night"
    time_choices = ((day, "Day"), (night, "Night"))
    yes = "Yes"
    no = "No"
    pat_choices = ((yes, "Yes"), (no, "No"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    patrolling_officer = models.ForeignKey(PomeEmloyees,null=True, related_name='officer1')
    patrolling_officer2 = models.ForeignKey(PomeEmloyees, null=True,related_name='officer2')
    patrolling_time = models.CharField(max_length=25,choices=time_choices, null=True, blank=True)
    name = models.ForeignKey(PomeEmloyees, null=True, related_name='name')
    code = models.CharField(max_length=255, null=True, blank=True)
    dress_up = models.CharField(max_length=25,choices=pat_choices, null=True, blank=True)
    wear_belt = models.CharField(max_length=25,choices=pat_choices, null=True, blank=True)
    wear_tie = models.CharField(max_length=25,choices=pat_choices, null=True, blank=True)
    wear_shoes = models.CharField(max_length=25,choices=pat_choices, null=True, blank=True)
    b_polish = models.CharField(max_length=25,choices=pat_choices, verbose_name="Boot Polish", null=True, blank=True)
    cap_batch = models.CharField(max_length=25,choices=pat_choices, null=True, blank=True)
    wear_cap = models.CharField(max_length=25,choices=pat_choices, null=True, blank=True)
    wear_whistle = models.CharField(max_length=25,choices=pat_choices, null=True, blank=True)
    wear_saving = models.CharField(max_length=25,choices=pat_choices, null=True, blank=True)
    wear_haircut = models.CharField(max_length=25,choices=pat_choices, null=True, blank=True)
    sleeping = models.CharField(max_length=25,choices=pat_choices, null=True, blank=True)
    post_out = models.CharField(max_length=25,choices=pat_choices, null=True, blank=True)
    wear_icard = models.CharField(max_length=25,choices=pat_choices, null=True, blank=True)
    wear_socks = models.CharField(max_length=25,choices=pat_choices, null=True, blank=True)
    dozzing = models.CharField(max_length=25,choices=pat_choices, null=True, blank=True)
    tabaco = models.CharField(max_length=25,choices=pat_choices, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    loc_assign = models.ForeignKey(PomeManageClientsLocations, null=True, blank=True)
    deduction_amount = models.IntegerField(null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Patrolling Day/Night'


    def single_patrolling(self):
        return '<a href="/single_patrolling/%s/"> %s </a>'  % (self.id, self.id)
    single_patrolling.allow_tags = True









class PomePattycashAccounts(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    account_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    auth_person = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)
    def __unicode__(self):
        return self.account_name
    class Meta:
        verbose_name_plural = 'Petty Cash Accounts'

class PomePayment(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    client_name = models.ForeignKey(PomeManageClients, null=True, blank=True)
    branch_name = models.CharField(max_length=255, null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    work_order = models.ForeignKey(PomeManageClientsLocations, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    payment_type = models.CharField(max_length=255, null=True, blank=True)
    payment_status = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Payment to Vendor'

class PomePaymentCollection(models.Model):
    vendor = "Vendor"
    workshop = "Workshop"
    type_choices = ((vendor, "Vendor"), (workshop, "Workshop"))
    neft = "NEFT"
    rtgs = "RTGS"
    pay_choices = ((neft, "NEFT"), (rtgs, "RTGS"))
    cash = "Cash"
    cheque = "Cheque"
    online_payment = "Online Payment"
    payment_choices = ((cash, "Cash"), (cheque, "Cheque"), (online_payment, "Online Payment"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    company_id = models.ForeignKey(PomeK1Details, null=True, blank=True)
    type = models.CharField(max_length=25,choices=type_choices, null=True, blank=True)
    company_name = models.ForeignKey(PomeVendorWorkshop, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    work_order = models.ForeignKey(PomeManageClientsLocations, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    payment_type = models.CharField(max_length=25,choices=pay_choices, null=True, blank=True)
    payment_status = models.CharField(max_length=25, choices=payment_choices, null=True, blank=True)
    cqno = models.CharField(max_length=50, null=True, blank=True)
    cqdate = models.CharField(max_length=50, null=True, blank=True)
    bank = models.CharField(max_length=50, null=True, blank=True)
    branch = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Payment Collection'


class PomePaymentReceiptIncharge(models.Model):
    pending = "Pending"
    completed = "Completed"
    status_choices = ((pending, "Pending"), (completed, "Completed"))
    parentid = models.IntegerField(null=True, blank=True)
    prepared_by = models.ForeignKey(PomeEmloyees, related_name="prepared_by",null=True)
    achead = models.ForeignKey(PomeEmloyees, related_name="achead",null=True)
    paidby = models.ForeignKey(PomeEmloyees, related_name="paidby",null=True)
    receivedby = models.ForeignKey(PomeEmloyees, related_name="receivedby",null=True)
    salary = models.IntegerField(null=True, blank=True)
    incentive = models.IntegerField(null=True, blank=True)
    barekrent = models.IntegerField(null=True, blank=True)
    others = models.IntegerField(null=True, blank=True)
    subtotal = models.IntegerField(null=True, blank=True)
    advance = models.IntegerField(null=True, blank=True)
    balance = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    thousands = models.IntegerField(null=True, blank=True)
    fivehundreds = models.IntegerField(null=True, blank=True)
    hundreds = models.IntegerField(null=True, blank=True)
    fifties = models.IntegerField(null=True, blank=True)
    twenties = models.IntegerField(null=True, blank=True)
    tens = models.IntegerField(null=True, blank=True)
    fives = models.IntegerField(null=True, blank=True)
    twos = models.IntegerField(null=True, blank=True)
    ones = models.IntegerField(null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    siteincharge = models.ForeignKey(PomeEmloyees, related_name="site_incharge",null=True)
    status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    final_amount = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Salary Release Update'


class PomePaymentsTransfers(models.Model):
     # AutoField?
    database_table = models.CharField(max_length=50, null=True, blank=True)
    database_table_id = models.IntegerField(null=True, blank=True)
    vendor_id = models.ForeignKey(PomeVendorWorkshop, null=True, blank=True)
    paid_amount = models.IntegerField(null=True, blank=True)
    invoice_number = models.CharField(max_length=150, null=True, blank=True)
    payment_type = models.CharField(max_length=50, null=True, blank=True)
    cqno = models.CharField(max_length=50, null=True, blank=True)
    cqdate = models.DateField(null=True, blank=True)
    bank = models.CharField(max_length=250, null=True, blank=True)
    branch = models.CharField(max_length=250, null=True, blank=True)
    online_type = models.CharField(max_length=250, null=True, blank=True)
    reference_number = models.CharField(max_length=250, null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Payment Transfers'

class PomePayscaleSetting(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    below_salary = models.CharField(max_length=255, null=True, blank=True)
    full_salary = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Payscale Settings'


class PomePoliceVerificationForm(models.Model):
    guid = models.IntegerField(primary_key=True)
    parentid = models.IntegerField(null=True, blank=True)
    full_name = models.CharField(max_length=250, null=True, blank=True)
    father_name = models.CharField(max_length=250, null=True, blank=True)
    present_address = models.TextField(null=True, blank=True)
    permanent_address = models.TextField(null=True, blank=True)
    residence_no = models.CharField(max_length=250, null=True, blank=True)
    office_no = models.CharField(max_length=250, null=True, blank=True)
    mobile_no = models.CharField(max_length=250, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=250, null=True, blank=True)
    family_father = models.CharField(max_length=250, null=True, blank=True)
    family_mother = models.CharField(max_length=250, null=True, blank=True)
    family_husband = models.CharField(max_length=250, null=True, blank=True)
    family_brother = models.CharField(max_length=250, null=True, blank=True)
    family_sister = models.CharField(max_length=250, null=True, blank=True)
    parent_occupation = models.CharField(max_length=250, null=True, blank=True)
    fullname_of_the_employer = models.CharField(max_length=250, null=True, blank=True)
    identification_mark = models.TextField(null=True, blank=True)
    arrested = models.CharField(max_length=250, null=True, blank=True)
    purpose_for_requiring = models.TextField(null=True, blank=True)
    period_of_verification = models.CharField(max_length=250, null=True, blank=True)
    place_of_stay = models.CharField(max_length=250, null=True, blank=True)
    locality_verification = models.CharField(max_length=250)
    date_added = models.IntegerField(null=True, blank=True)
    def __unicode__(self):
        return self.full_name
    class Meta:
        verbose_name_plural = 'Police Verification Form'

class PomePurchaseOrder(models.Model):
     # AutoField?
    parentid = models.IntegerField(null=True, blank=True)
    store_id = models.ForeignKey(PomeManageStores, null=True, blank=True)
    item_name = models.ForeignKey(PomeManageItems, null=True, blank=True)
    vendor = models.ForeignKey(PomeVendorWorkshop, null=True, blank=True)
    item_price = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.CharField(max_length=255, null=True, blank=True)
    refno = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    delivery_mode = models.CharField(max_length=255, null=True, blank=True)
    payment_mode = models.CharField(max_length=255, null=True, blank=True)
    credit_days = models.CharField(max_length=255, null=True, blank=True)
    payment_type = models.CharField(max_length=255, null=True, blank=True)
    discount = models.CharField(max_length=255, null=True, blank=True)
    initiated_by = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    approved_by = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Purchase Order'



class PomeReferenceIncentive(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=100, choices=status_choices, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Reference Incentive Setting'

 
class PomeReferencePayment(models.Model):
     # AutoField?
    paid = "Paid"
    unpaid = "Unpaid"
    paid_choices = ((paid, "Paid"), (unpaid, "Unpaid"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    reference_id = models.ForeignKey(PomeEmloyees, null=True, related_name="reference_id")
    emp_id = models.ForeignKey(PomeEmloyees, null=True, related_name="emp_id")
    amount = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=25, choices=paid_choices, null=True, blank=True)
    month_year = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Reference Payment'
 
class PomeReturnStock(models.Model):
    yes = "Yes"
    no = "No"
    type_choices = ((yes, "Yes"), (no, "No"))
    damaged = "Damaged"
    emp_resigned = "Emp Resigned"
    expiry = "Expiry"
    reason_choices = ((damaged, "Damaged"), (emp_resigned, "Emp Resigned"), (expiry, "Expiry"))
    pid = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    parentid = models.IntegerField(null=True, blank=True)
    employee_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    item_id = models.ForeignKey(PomePurchaseOrder, null=True, blank=True)
    designation_id = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    pome_item_requisition_id = models.ForeignKey(PomePurchaseRequisition, null=True, blank=True)
    returned_stock = models.IntegerField(null=True, blank=True)
    remarks_stock = models.TextField(null=True, blank=True)
    reason_stock = models.CharField(max_length=30, choices=reason_choices, null=True, blank=True)
    reusable = models.CharField(max_length=30, choices=type_choices, null=True, blank=True)
    penality_charges = models.CharField(max_length=30, choices=type_choices, null=True, blank=True)
    penality_amount_stock = models.IntegerField(null=True, blank=True)
    returned_date_stock = models.DateField(null=True, blank=True)
    siteincharge = models.IntegerField(null=True, blank=True)
    status_add = models.IntegerField(null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Return Stock'

class PomeReturnStockVendor(models.Model):
    courier = "Courier"
    transport = "Transport"
    person = "Person"
    
    mode_choices = ((courier, "Courier"), (transport, "Transport"), (person, "Person"))
    refundable = "Refundable"
    non_refundable = "Non Refundable"
    gp_choices = ((refundable, "Refundable"), (non_refundable, "Non Refundable"))
    parentid = models.IntegerField(null=True, blank=True)
    vendor_id = models.ForeignKey(PomeVendorWorkshop, null=True, blank=True)
    item_id = models.ForeignKey(PomeManageItems, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    unit_price = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    mode = models.CharField(max_length=50,choices=mode_choices, null=True, blank=True)
    courier_no = models.CharField(max_length=150, null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    reference_no = models.CharField(max_length=100, null=True, blank=True)
    approved_by = models.CharField(max_length=150, null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    courier_name = models.CharField(max_length=50, null=True, blank=True)
    pod_number = models.CharField(max_length=50, null=True, blank=True)
    number_plate = models.CharField(max_length=50, null=True, blank=True)
    driver_name = models.CharField(max_length=50, null=True, blank=True)
    driver_contact = models.CharField(max_length=50, null=True, blank=True)
    per_name = models.CharField(max_length=50, null=True, blank=True)
    return_time = models.CharField(max_length=50, null=True, blank=True)
    gatepass_no = models.CharField(max_length=50, null=True, blank=True)
    in_date = models.DateField(null=True, blank=True)
    in_time = models.TimeField(null=True, blank=True)
    remarks_gp = models.CharField(max_length=25,choices=gp_choices, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Return Stock To Vendor'

class PomeSalAssignment(models.Model):
     # AutoField?
    parentid = models.IntegerField(null=True, blank=True)
    client_name = models.ForeignKey(PomeManageClients, null=True, blank=True)
    work_order_no = models.ForeignKey(PomeManageClientsLocations, null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    supervisor = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)
    payment_salary = models.FloatField(null=True, blank=True)
    balance_salary = models.FloatField(null=True, blank=True)
    incentive = models.FloatField(null=True, blank=True)
    payment_incentive = models.FloatField(null=True, blank=True)
    balance_incentive = models.FloatField(null=True, blank=True)
    house_rent = models.FloatField(null=True, blank=True)
    payment_house_rent = models.FloatField(null=True, blank=True)
    balance_house_rent = models.FloatField(null=True, blank=True)
    voucher = models.FloatField(null=True, blank=True)
    payment_ottotal = models.FloatField(null=True, blank=True)
    balance_ottotal = models.FloatField(null=True, blank=True)
    others = models.FloatField(null=True, blank=True)
    payment_others = models.FloatField(null=True, blank=True)
    balance_others = models.FloatField(null=True, blank=True)
    totamount = models.FloatField(null=True, blank=True)
    payment_totamount = models.FloatField(null=True, blank=True)
    balance_totamount = models.FloatField(null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Salary Assignment'


class PomeSalAssignmentEmps(models.Model):
     # AutoField?
    psa_id = models.ForeignKey(PomeSalAssignment, null=True, blank=True)
    pome_emloyees_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    net_pay = models.FloatField(null=True, blank=True)
    hra = models.FloatField(null=True, blank=True)
    ot_got = models.FloatField(null=True, blank=True)
    paid_mess = models.FloatField(null=True, blank=True)
    cash_return = models.FloatField(null=True, blank=True)
    incentive_ind = models.FloatField(null=True, blank=True)
    net_pay_total = models.FloatField(null=True, blank=True)
    hra_total = models.FloatField(null=True, blank=True)
    ot_got_total = models.FloatField(null=True, blank=True)
    incentive_ind_total = models.FloatField(null=True, blank=True)
    paid_mess_total = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Salary Assignments Employees'

class PomeSalaries(models.Model):
    paid = "Paid"
    not_paid = "Not Paid"
    
    payment_choices = ((paid, "Paid"), (not_paid, "Not Paid"))
    parentid = models.IntegerField(null=True, blank=True)
    pome_emloyees_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    supervisor = models.IntegerField(null=True, blank=True)
    month_year = models.CharField(max_length=50, null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    work_days = models.IntegerField(null=True, blank=True)
    paid_leaves = models.IntegerField(null=True, blank=True)
    total_days = models.IntegerField(null=True, blank=True)
    total_hours = models.FloatField(null=True, blank=True)
    basic = models.IntegerField(null=True, blank=True)
    cal_basic = models.FloatField(null=True, blank=True)
    hra = models.FloatField(null=True, blank=True)
    washing = models.FloatField(null=True, blank=True)
    other = models.FloatField(null=True, blank=True)
    bonus = models.FloatField(null=True, blank=True)
    annual_bonus = models.FloatField(null=True, blank=True)
    loyality_bonus = models.FloatField(null=True, blank=True)
    total_allowances = models.FloatField(null=True, blank=True)
    epf = models.FloatField(null=True, blank=True)
    esi = models.FloatField(null=True, blank=True)
    fines = models.IntegerField(null=True, blank=True)
    advances = models.FloatField(null=True, blank=True)
    loans = models.FloatField(null=True, blank=True)
    other_deductions = models.FloatField(null=True, blank=True)
    total_deductions = models.FloatField(null=True, blank=True)
    net_pay = models.FloatField(null=True, blank=True)
    payment_status = models.CharField(max_length=50,choices=payment_choices, null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    generated_id = models.IntegerField(null=True, blank=True)
    work_order = models.ForeignKey(PomeManageClientsLocations, null=True, blank=True)
    conveyance = models.FloatField(null=True, blank=True)
    pt = models.FloatField(null=True, blank=True)
    tds = models.IntegerField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Salaries'

class PomeSalariesGenerated(models.Model):
     # AutoField?
    parentid = models.IntegerField(null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    from_month = models.IntegerField(null=True, blank=True)
    from_year = models.IntegerField(null=True, blank=True)
    to_date = models.IntegerField(null=True, blank=True)
    to_month = models.IntegerField(null=True, blank=True)
    to_year = models.IntegerField(null=True, blank=True)
    from_final_date = models.DateField(null=True, blank=True)
    to_final_date = models.DateField(null=True, blank=True)
    from_year_month = models.CharField(max_length=250, null=True, blank=True)
    to_year_month = models.CharField(max_length=250, null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    page = models.IntegerField(null=True, blank=True)
    page_limit = models.IntegerField(null=True, blank=True)
    page_current_limit = models.IntegerField(null=True, blank=True)
    otnot = models.IntegerField(null=True, blank=True)
    otallow = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Salary Generation Field'

class PomeSalaryDisbursement(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    salary_type = models.CharField(max_length=255, null=True, blank=True)
    client_id = models.ForeignKey(PomeManageClients, null=True, blank=True)
    payment_to = models.CharField(max_length=255, null=True, blank=True)
    emp_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    emp_name = models.CharField(max_length=255, null=True, blank=True)
    emp_code = models.CharField(max_length=255, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    salary_month = models.CharField(max_length=255, null=True, blank=True)
    salary = models.CharField(max_length=255, null=True, blank=True)
    incentive = models.CharField(max_length=255, null=True, blank=True)
    voucher = models.CharField(max_length=255, null=True, blank=True)
    house_rent = models.CharField(max_length=255, null=True, blank=True)
    loan_amount = models.CharField(max_length=255, null=True, blank=True)
    absent_amount = models.CharField(max_length=255, null=True, blank=True)
    overtime_amount = models.CharField(max_length=255, null=True, blank=True)
    final_amount = models.CharField(max_length=255, null=True, blank=True)
    paid_amount = models.CharField(max_length=255, null=True, blank=True)
    balance_amount = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Salary Disbursement'

class PomeSalaryFixed(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    designation = models.ForeignKey(PomeManageMasters, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Salary Fixed'


class PomeSalaryPaymentTransactions(models.Model):
    cash = "Cash"
    cheque = "Cheque"
    payment_method_choices = ((cash, "Cash"), (cheque, "Cheque"))
    salary_id = models.ForeignKey(PomeSalaries, null=True, blank=True)
    pome_emloyees_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    voucherno = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    payment = models.CharField(max_length=50, choices=payment_method_choices, null=True, blank=True)
    cqno = models.CharField(max_length=50, null=True, blank=True)
    cqdate = models.DateField(null=True, blank=True)
    bank = models.CharField(max_length=50, null=True, blank=True)
    branch = models.CharField(max_length=50, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    def __unicode__(self):
        return self.voucherno
    class Meta:
        verbose_name_plural = 'Salary Payment Transactions'

class PomeScaleDifference(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    scale_difference = models.CharField(max_length=255, null=True, blank=True)
    effective_date = models.DateField(null=True, blank=True)
    added_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Scale Difference'

class PomeSendsms(models.Model):
     # AutoField?
    parentid = models.IntegerField(null=True, blank=True)
    send_to = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    sms_no = models.CharField(max_length=255, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    def __unicode__(self):
        return self.message
    class Meta:
        verbose_name_plural = 'Send SMS'

class PomeShifts(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    shift_name = models.CharField(max_length=255, null=True, blank=True)
    from_time = models.CharField(max_length=255, null=True, blank=True)
    to_time = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    added_on = models.DateTimeField(null=True, blank=True)
    def __unicode__(self):
        return self.shift_name
    class Meta:
        verbose_name_plural = 'Shifts'

class PomeStipendDisbursement(models.Model):
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
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices)
    trainee_id = models.ForeignKey(PomeBiodata, null=True, blank=True)
    session_id = models.ForeignKey(PomeTrainingSession, null=True, blank=True)
    payment_amt = models.CharField(max_length=255, null=True, blank=True)
    paid_amount = models.CharField(max_length=255, null=True, blank=True)
    payment_status = models.CharField(max_length=25, choices=payment_choices, null=True, blank=True)
    payment_method = models.CharField(max_length=25, choices=payment_method_choices, null=True, blank=True)
    cheque_no = models.CharField(max_length=255, null=True, blank=True)
    cheque_date = models.CharField(max_length=255, null=True, blank=True)
    bank_name = models.CharField(max_length=255, null=True, blank=True)
    branch_name = models.CharField(max_length=255, null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Stipend Disbursements'

class PomeStipendTrainee(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    session_id = models.ForeignKey(PomeTrainingSession, null=True, blank=True)
    trainer_name = models.ForeignKey(PomeTrainer, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    training_days = models.CharField(max_length=255, null=True, blank=True)
    perday_price = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.trainer_name
    class Meta:
        verbose_name_plural = 'Stipend Trainee'

class PomeStocks(models.Model):
     # AutoField?
    vendor_id = models.ForeignKey(PomeVendorWorkshop, null=True, blank=True)
    store_id = models.ForeignKey(PomeManageStores, null=True, blank=True)
    items = models.ForeignKey(PomeManageItems, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Stocks'

class PomeStockUpdate(models.Model):
     # AutoField?
    item = models.ForeignKey(PomeManageItems, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    invoiceno = models.ForeignKey(PomeClientInvoice, null=True, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Update Stock'


class PomeStocksTransactions(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    pome_stocks_id = models.ForeignKey(PomeStocks, null=True, blank=True)
    store_id = models.ForeignKey(PomeManageStores, null=True, blank=True)
    vendor_id = models.ForeignKey(PomeVendorWorkshop, null=True, blank=True)
    employee_id = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    pome_item_requisition_id = models.ForeignKey(PomeItemRequisition, null=True, blank=True)
    pome_return_stock_id = models.ForeignKey(PomeReturnStock, null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    status_add = models.IntegerField(null=True, blank=True)
    vendor_status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Stocks Transactions'

class PomeSubmenus(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    menu_id = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.CharField(max_length=255, null=True, blank=True)
    inner_menu = models.IntegerField(null=True, blank=True)



class PomeSuperAdmin(models.Model):
    super_admin_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.username
    class Meta:
        verbose_name_plural = 'Super Admin'

class PomeSupporticket(models.Model):
    approved = "Approved"
    cancelled = "Cancelled"
    wait_for_approval = "Wait For Approval"
    status_choices = ((approved, "Approved"), (cancelled, "Cancelled"), (wait_for_approval, "Wait For Approval"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    name = models.ForeignKey(PomeEmloyees, related_name="mail_name", null=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    mail_from = models.ForeignKey(PomeEmloyees, related_name="mail_from", null=True)
    message = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    sended_on = models.DateTimeField(null=True, blank=True)
    empid = models.ForeignKey(PomeEmloyees, null=True, related_name="empid")
    update_message = models.TextField(null=True, blank=True)
    update_status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True)
    image = models.ImageField(upload_to = "support-images/", null=True, blank=True)

    def __unicode__(self):
        return self.subject
    class Meta:
        verbose_name_plural = 'Support Ticket'

class PomeTaskManagement(models.Model):
    completed = "Completed"
    pending = "Pending"
    status_choices = ((completed, "Completed"), (pending, "Pending"))
    normal = "Normal"
    priority = "Priority"
    urgent = "Urgent"
    priority_choices = ((normal, "Normal"), (priority, "Priority"), (urgent, "Urgent"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    task = models.CharField(max_length=255, null=True, blank=True)
    task_summery = models.CharField(max_length=255, null=True, blank=True)
    assign_to = models.ForeignKey(PomeEmloyees, related_name="assigned_to", null=True)
    assigned_by = models.ForeignKey(PomeEmloyees, related_name="assigned_by", null=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    assigned_on = models.DateField(null=True, blank=True)
    assigned_time = models.TimeField(null=True, blank=True)
    time_duration = models.DateTimeField(null=True, blank=True)
    start_time = models.CharField(max_length=50, null=True, blank=True)
    end_time = models.CharField(max_length=255, null=True, blank=True)
    time_taken = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    starttime = models.TimeField(null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=50, choices=priority_choices, null=True, blank=True)
    taskremarks = models.TextField(null=True, blank=True)
    start = models.CharField(max_length=255, null=True, blank=True)
    end = models.CharField(max_length=255, null=True, blank=True)
    def __unicode__(self):
        return self.task
    class Meta:
        verbose_name_plural = 'Task Management'

class PomeTraineeAttendence(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    trainee_id = models.ForeignKey(PomeBiodata, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    hours = models.IntegerField(null=True, blank=True)
    work_order = models.ForeignKey(PomeManageClientsLocations, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Trainee Attendance'

class PomeUploadWorkorder(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    client_name = models.ForeignKey(PomeManageClients, null=True, blank=True)
    branch = models.CharField(max_length=255, null=True, blank=True)
    order_name = models.CharField(max_length=255, null=True, blank=True)
    order_no = models.CharField(max_length=255, null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)
    order_price = models.CharField(max_length=255, null=True, blank=True)
    order_upload = models.FileField(upload_to="documents", null=True, blank=True)
    def __unicode__(self):
        return self.order_name
    class Meta:
        verbose_name_plural = 'Upload Workorder'

class PomeUserAccess(models.Model):
     # AutoField?
    parentid = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.CharField(max_length=255, null=True, blank=True)
    permission_id = models.CharField(max_length=255, null=True, blank=True)
    menu_id = models.IntegerField(null=True, blank=True)
    sub_menu_id = models.IntegerField(null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'User Access'

class PomeUserPermission(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    
    parentid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=25, choices=status_choices, null=True, blank=True)
    permission_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    added_on = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'User Permission'

class PomeUsersLog(models.Model):
    user = "User"
    client = "Client"
    vendor = "Vendor"
    login_choices = ((user, "User"), (client, "Client"), (vendor, "Vendor"))
    parentid = models.CharField(max_length=255, null=True, blank=True)
    login_type = models.CharField(max_length=255, choices=login_choices, null=True, blank=True)
    login_id = models.CharField(max_length=255, null=True, blank=True)
    login_time = models.DateTimeField(null=True, blank=True)
    logout_time = models.DateTimeField(null=True, blank=True)
    loggedip = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)  # Field name made lowercase.

    class Meta:
        verbose_name_plural = 'Users Log'

class PomeVisitor(models.Model):
    active = "Active"
    inactive = "Inactive"
    status_choices = ((active, "Active"), (inactive, "Inactive"))
    available = "Available"
    not_available = "Not Available"
    availability_choices = ((available, "Available"), (not_available, "Not Available"))
    
    parentid = models.CharField(max_length=255, null=True,blank=True)
    visitor_name = models.CharField(max_length=250, null=True,blank=True)
    from_company = models.CharField(max_length=250, null=True,blank=True)
    from_address = models.TextField(null=True,blank=True)
    contact_number = models.CharField(max_length=255, null=True,blank=True)
    emailid = models.CharField(max_length=250, null=True,blank=True)
    staff_guid = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    purpose = models.TextField(null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True,blank=True)
    avaliability = models.CharField(max_length=10,choices=availability_choices, null=True,blank=True)
    alternate_person = models.IntegerField(null=True,blank=True)
    date_added = models.DateField(null=True,blank=True)
    alert_status = models.CharField(max_length=20, choices=status_choices, null=True,blank=True)
    visit_date_time = models.DateTimeField(null=True,blank=True)
    update_person = models.CharField(max_length=100, null=True,blank=True)
    remarks = models.TextField(null=True,blank=True)
    out_time = models.TimeField(null=True,blank=True)
    def __unicode__(self):
        return self.visitor_name
    class Meta:
        verbose_name_plural = 'Visitor Management'

class PomeWashings(models.Model):
     # AutoField?
    washing_emp = models.ForeignKey(PomeEmloyees, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    #limit_amount = models.IntegerField(null=True, blank=True)
    #limit_amount_months = models.IntegerField(null=True, blank=True)
    #limit_months = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Washings'

