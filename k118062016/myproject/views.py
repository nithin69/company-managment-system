from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from notifications.signals import notify
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _
#from k1emp.forms import *
from myproject.forms import *
from myproject import models as mymodels
from myproject.serializers import *
#from myproject import forms as myforms
#from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from rest_framework import generics
from django.db.models import Q
import datetime
import calendar
from calendar import monthrange
from django.db import connection
from reportlab.pdfgen import canvas
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
from dal import autocomplete


# Create your views here.


def advsearchform(request):
    loans = mymodels.PomeEmpLoans.objects.order_by().values('loan_type').distinct()
    context_dict = {'loans': loans}
    return render(request, 'advsearchform.html', context_dict)



def advreport(request):
    #loans = mymodels.PomeEmpLoans.objects.order_by().values('loan_type').distinct()
    context_dict = {}
    return render(request, '/var/www/html/adv_report.php/', context_dict)



def advsearch(request):
    
    context = RequestContext(request)
    if 'q' in request.GET:
        q = request.GET['q']
    
    print q
    
    adv = mymodels.PomeEmpLoans.objects.filter(Q(loan_type__contains = q) | Q(loan_type__exact=q))

    return render_to_response('advsearch.html', {'adv': adv,'category': q}, context)



class BdAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return PomeEmloyees.objects.none()
        qs = PomeEmloyees.objects.all()
        if self.q:
            qs = qs.filter(firstname__istartswith=self.q) | qs.filter(employeno__iendswith=self.q)
            
        return qs


class DesignationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return PomeManageMasters.objects.none()

        qs = PomeManageMasters.objects.all()
	print qs
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class ItemAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return PomeManageItems.objects.none()

        qs = PomeManageItems.objects.all()
	print qs
        if self.q:
            qs = qs.filter(item_name__istartswith=self.q)

        return qs


class BiodataAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return PomeBiodata.objects.none()

        qs = PomeBiodata.objects.all()
	print qs
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs



class ClientsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return PomeManageClients.objects.none()

        qs = PomeManageClients.objects.all()
	print qs
        if self.q:
            qs = qs.filter(client_name__istartswith=self.q)

        return qs


class InvoiceAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return PomeClientInvoice.objects.none()

        qs = PomeClientInvoice.objects.all()
	print qs
        if self.q:
            qs = qs.filter(invoice_no__istartswith=self.q)

        return qs



def userlogform(request):
    userlog = mymodels.PomeUsersLog.objects.order_by().values('login_type').distinct()
   
    context_dict = {'userlog': userlog}
    return render(request, 'userlogform.html', context_dict)


def userlog(request):
    
    context = RequestContext(request)
    if 'q' in request.GET:
        q = request.GET['q']
    
    print q
    
    log = mymodels.PomeUsersLog.objects.filter(Q(login_type__contains = q) | Q(login_type__exact=q))

    return render_to_response('userlog.html', {'log': log,'category': q}, context)


def authorisedstrengthform(request):
    client = mymodels.PomeClientBilling.objects.values('authorised').distinct()
    context_dict = {'client': client}
    return render(request, 'authorisedstrengthform.html', context_dict)

def authorisedstrengthreport(request):
    
    context = RequestContext(request)
    if 'q' in request.GET:
        q = request.GET['q']
    print q
        
    authstrength = mymodels.PomeClientBilling.objects.filter(Q(authorised__contains = q) | Q(authorised__exact=q))
    
    return render_to_response('authorisedstrengthreport.html', {'authstrength': authstrength, 'category': q}, context)



def webservices(request):
    context_dict = {}
    return render(request, 'webservicesupdated.php', context_dict)
    
    
@login_required	
def myprofile(request):
    context = RequestContext(request)
    context_dict = {}
    try:
        e = Employee.objects.get(email=request.user)
        print e
        context_dict['employee'] = e
        print "e is :", e
        objfields = EmployeeForm(data=model_to_dict(e))
        context_dict['objfields'] = objfields
    except:
        print "profile not found: "
        e = None
    return render_to_response('myprofile.html', context_dict, context)


@login_required	
def biodata(request):
    context = RequestContext(request)
    context_dict = {}
    try:
        employees = mymodels.PomeBiodata.objects.all()
        context_dict['employees'] = employees
        
    except:
        print "profile not found: "
        e = None
    return render_to_response('biodatas.html', context_dict, context)

def biodata_view(request, id):
    context = RequestContext(request)
    context_dict = {}
    try:
        employees = mymodels.PomeBiodata.objects.filter(id=id)
        context_dict['employees'] = employees
        
    except:
        print "profile not found: "
        e = None
    return render_to_response('biodatas.html', context_dict, context)

def biodata_delete(request, id):
    context = RequestContext(request)
    context_dict = {}
    try:
        employees = mymodels.PomeBiodata.objects.filter(id=id).delete()
        context_dict['employees'] = employees
        
    except:
        print "profile not found: "
        e = None
    return render_to_response('biodatas.html', context_dict, context)
    

@login_required
def support(request):
    context = RequestContext(request)
    context_dict = {}
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    done = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        ticket_form = SupporticketForm(data=request.POST)
        # If the two forms are valid...
        print ticket_form
            
        if ticket_form.is_valid():
            # Save the user's form data to the database.
            ticket = ticket_form.save(commit=False)
            ticket.owner = Employee.objects.get(email=request.user)
            ticket = ticket_form.save()
            # Update our variable to tell the template registration was successful.
            done = True
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
            context_dict['done'] = True
        else:
            context_dict['errors'] = ticket_form.errors
            print ticket_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        context_dict['ticket_form'] = SupporticketForm()
        context_dict['tickets'] = Supporticket.objects.all()
        
        
    # Render the template depending on the context.
    return render(request, 'Supporticket.html', context_dict)
    
    
@login_required
def genobj(request, modelname = "", objid= "", action = ""):
    context = RequestContext(request)
    context_dict = {}
    
    if objid != "":
        genobj = model.objects.get(id = int(objid))
        context_dict['objfields']  = myforms.SupporticketForm(model_to_dict(genobj))
        context_dict['genid'] = genobj.id
        context_dict['modelname'] = modelname


    if modelname == "supporticket":
        model = modelname
        context_dict['gen_form'] = myforms.SupporticketForm()
        postform = myforms.SupporticketForm(request.POST)
        
    if modelname == "gatepass":
        model = mymodels.Supporticket
        context_dict['gen_form'] = myforms.SupporticketForm()
        postform = myforms.SupporticketForm(request.POST)
    
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    done = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        
        gen_form = postform
        # If the two forms are valid...
            
        if gen_form.is_valid():
            # Save the user's form data to the database.
            gen = gen_form.save(commit=False)
            gen.owner = Employee.objects.get(email=request.user)
            gen = gen_form.save()
            # Update our variable to tell the template registration was successful.
            done = True
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
            context_dict['done'] = True
        else:
            context_dict['errors'] = gen_form.errors
            print gen_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:

        if objid != "":
            template_name = 'genread.html'
            context_dict['page_title'] = "Ticket Detail"
            return render(request, template_name, context_dict)
        else:

            context_dict['gens'] = model.objects.all()
            
    template_name = '%s.html' % model.__name__.lower()   
    
    context_dict['page_title'] = "Employee Support"
    # Render the template depending on the context.
    return render(request, template_name, context_dict)



def employee_gatepass(request):
    context_dict = {}
    passes = mymodels.PomeGatepass.objects.all()
    context_dict['passes'] = passes
    return render(request, 'gatepass_employee.html', context_dict)


def employee_gatepass_delete(request, id):
    passes = PomeGatepass.objects.filter(id=id).delete()
    context_dict = {'passes': passes}
    return render(request, 'gatepass_employee.html', context_dict)	

    
def employee_attendance_bulk(request):
    context_dict = {}
    emp_attendance = mymodels.PomeEmployeeAttendence.objects.all()

    clients = PomeManageClientsLocations.objects.all()

    context_dict = {'emp_attendance': emp_attendance}
    context_dict['clients'] = clients
    return render(request, 'employee_attendance_bulk.html', context_dict)


def otallow_details(request):
    context_dict = {}
    emp_details = PomeEmloyees.objects.all()

    clients = PomeManageClientsLocations.objects.all()

    context_dict = {'emp_details': emp_details}
    context_dict['clients'] = clients
    return render(request, 'otallow_details.html', context_dict)



def empbulksearch(request):
    context_dict = {}
    if 'loca' in request.GET and request.GET['loca']:
        loca = request.GET['loca']

    if 'to_date' in request.GET and request.GET['to_date']:
        to_date = request.GET['to_date']
    
    clients = mymodels.PomeManageClientsLocations.objects.all()

    context_dict['clients'] = clients

    tod = datetime.datetime.strptime(to_date, '%d-%m-%Y')
    print tod
    diff_days = datetime.timedelta(days=5)
    from_date = tod - diff_days
    print from_date
    condition_days = 7
  
    cbs = mymodels.PomeClientBilling.objects.filter(work_order_no = loca)
    
    totalallowch = 0
    for i in range(5):
         totallo = cbs['hours'] + cbs['noofpersons']
         totallocwh = totallo + totallocwh 
  
    

    '''hours = mymodels.PomeEmployeeAttendence.objects.aggregate(Sum('hours')).filter(work_order = loca and date = from_date)
    balance = totallocwh - hours
    loca = mymodels.PomeManageClientsLocations.objects.get(name = loca)'''


    rota = mymodels.PomeEmployeeAttendence.objects.filter(locations_id = loca.id)
    
    context_dict['loca'] = loca
    context_dict['excess_loc_att'] = excess_loc_att

    return render(request, 'employee_attendance_bulk.html', context_dict)	

    
def employee_gatepass_add(request):
    passes = Gatepass.objects.all()
    context_dict = {'passes': passes}
    return render(request, 'gatepass_employee.html', context_dict)

def master_type(request):
    master = PomeMasters.objects.all()
    context_dict = {'master': master}
    return render(request, 'master_type.html', context_dict)

def incentive_setting_loc(request):
    locationwise_incentive = PomeIncentiveLoc.objects.all()
    context_dict = {'locationwise_incentive': locationwise_incentive}
    return render(request, 'incentive_setting_loc.html', context_dict)


def consultancy(request):
    consultancy = PomeConsultancies.objects.all()
    context_dict = {'consultancy': consultancy}
    return render(request, 'consultancy.html', context_dict)

def loyality_bonus(request):
    loyality = PomeLoyalityBonous.objects.all()
    context_dict = {'loyality': loyality}
    return render(request, 'loyality_bonus.html', context_dict)


def trainee_attendance(request):
    trainee = PomeBiodata.objects.all()
    context_dict = {'trainee': trainee}
    return render(request, 'trainee_attendance.html', context_dict)

def trainee_attendance_view(request, id):
    trainee = PomeBiodata.objects.filter(id= id)
    context_dict = {'trainee': trainee}
    return render(request, 'trainee_attendance.html', context_dict)

def outward_gatepass(request):
    outward_gatepass = mymodels.PomeOutward.objects.all()
    context_dict = {'outward_gatepass': outward_gatepass}
    return render(request, 'outward_gatepass.html', context_dict)

def manage_employee(request):
    employee = mymodels.PomeEmloyees.objects.all()
    context_dict = {'employee': employee}
    return render(request, 'manage_employee.html', context_dict)

def employee_view(request, id):
    employee = mymodels.PomeEmloyees.objects.filter(id=id)
    context_dict = {'employee': employee}
    return render(request, 'manage_employee.html', context_dict)

def employee_delete(request, id):
    employee = mymodels.PomeEmloyees.objects.filter(id=id).delete()
    context_dict = {'employee': employee}
    return render(request, 'manage_employee.html', context_dict)


def discipline_compliance(request):
    
    discipline = mymodels.PomeDisciplineCompliance.objects.all()
    context_dict = {'discipline': discipline}
    return render(request, 'discipline_compliance.html', context_dict)

def employee_attendance(request):
    context_dict = {}
    employee_attendance = mymodels.PomeEmployeeAttendence.objects.all()
    context_dict = {'employee_attendance': employee_attendance}
    return render(request, 'employee_attendance.html', context_dict)



def manage_vendor(request):
    vendor = mymodels.PomeVendorWorkshop.objects.all()
    context_dict = {'vendor': vendor}
    return render(request, 'manage_vendors_workshops.html', context_dict)

def task_management(request):
    task = mymodels.PomeTaskManagement.objects.all()
    context_dict = {'task': task}
    return render(request, 'task_management.html', context_dict)

def visitor_management(request):
    visitor = mymodels.PomeVisitor.objects.all()
    context_dict = {'visitor': visitor}
    return render(request, 'visitor.html', context_dict)

def search_profile(request):
    profile = mymodels.Profile.objects.all()
    context_dict = {'profile': profile}
    return render(request, 'search_profile.html', context_dict)

def location_incentive_setting(request):
    locnot = mymodels.PomeLocationIncentive.objects.all()
    context_dict = {'locnot': locnot}
    return render(request, 'location_incentive_setting.html', context_dict)


def trainer_settings(request):
    trainer_settings = mymodels.PomeTrainer.objects.all()
    context_dict = {'trainer_settings': trainer_settings}
    return render(request, 'trainer_settings.html', context_dict)

def reference_incentive_settings(request):
    incentive = mymodels.PomeReferenceIncentive.objects.all()
    context_dict = {'incentive': incentive}
    return render(request, 'reference_incentive_settings.html', context_dict)

def incentive_settings(request):
    incentive_settings = mymodels.PomeTrainer.objects.all()
    context_dict = {'trainer_settings': trainer_settings}
    return render(request, 'trainer_settings.html', context_dict)


def trainer_delete(request, id):
    trainer = mymodels.PomeTrainer.objects.filter(id=id).delete()
    context_dict = {'trainer': trainer}
    return render(request, 'trainer_settings.html', context_dict)


def customer_feedback(request):
    feedback = PomeCustomerFeedback.objects.all().values()
    context_dict = {'feedback': feedback}
    return render(request, 'customer_feedback.html', context_dict)

def notice_board(request):
    notice = mymodels.PomeNoticeboard.objects.all()
    context_dict = {'notice': notice}
    return render(request, 'notice_board.html', context_dict)

def notice_delete(request, id):
    notice = mymodels.PomeNoticeboard.objects.filter(id=id).delete()
    context_dict = {'notice': notice}
    return render(request, 'notice_board.html', context_dict)

def final_report(request):
    final_report = mymodels.PomeFinalReport.objects.all()
    context_dict = {'final_report': final_report}
    return render(request, 'final_report.html', context_dict)

def loan_types(request):
    loan_types = mymodels.PomeLoanTypes.objects.all()
    context_dict = {'loan_types': loan_types}
    return render(request, 'loan_types.html', context_dict)

def final_report_view(request, id):
    final_report = mymodels.PomeFinalReport.objects.filter(id=id)
    context_dict = {'final_report': final_report}
    return render(request, 'final_report.html', context_dict)


def support(request):
    try:
        e = Employee.objects.get(email=request.user)
        print e
        print "e is :", e
        objfields = PomeSupporticketForm(data=model_to_dict(e))       
    except:
        print "profile not found: "
        e = None
    support = mymodels.PomeSupporticket.objects.all()
    context_dict = {'support': support, 'e': e, 'objfields': objfields}
    return render(request, 'support_ticket.html', context_dict)


def loan_advance_setting(request):
    loan_advance = mymodels.PomeLoansAdvances.objects.all()
    context_dict = {'loan_advance': loan_advance}
    return render(request, 'loan_advance_setting.html', context_dict)

class OutwardList(APIView):
    def get(self, request, format=None):
        outward = PomeOutward.objects.all()
        serialized = OutwardSerializer(outward, many=True)
        return Response(serialized.data)    

class EmployeeList(APIView):
    def get(self, request, format=None):
        employee = PomeEmloyees.objects.all()
        serialized = EmployeeSerializer(employee, many=True)
        return Response(serialized.data)

class DisciplineList(APIView):
    def get(self, request, format=None):
        discipline = PomeDisciplineCompliance.objects.all()
        serialized = DisciplineSerializer(discipline, many=True)
        return Response(serialized.data)

class ClientList(APIView):
    def get(self, request, format=None):
        client = PomeManageClients.objects.all()
        serialized = ClientSerializer(client, many=True)
        return Response(serialized.data)

class VendorList(APIView):
    def get(self, request, format=None):
        vendor = PomeVendorWorkshop.objects.all()
        serialized = VendorSerializer(vendor, many=True)
        return Response(serialized.data)

class VisitorList(APIView):
    def get(self, request, format=None):
        visitor = PomeVisitor.objects.all()
        serialized = VisitorSerializer(visitor, many=True)
        return Response(serialized.data)

class TaskList(APIView):
    def get(self, request, format=None):
        task = PomeTaskManagement.objects.all()
        serialized = TaskSerializer(task, many=True)
        return Response(serialized.data)
 
class BiodataList(APIView):
    def get(self, request, format=None):
        biodata = PomeBiodata.objects.all()
        serialized = BiodataSerializer(biodata, many=True)
        return Response(serialized.data)

class EmployeeAttendanceList(APIView):
    def get(self, request, format=None):
        attendance = PomeEmployeeAttendence.objects.all()
        serialized = AttendanceSerializer(attendance, many=True)
        return Response(serialized.data)

class NoticeBoardList(APIView):
    def get(self, request, format=None):
        notice = PomeNoticeboard.objects.all()
        serialized = NoticeBoardSerializer(notice, many=True)
        return Response(serialized.data)

class FinalReportList(APIView):
    def get(self, request, format=None):
        report = PomeFinalReport.objects.all()
        serialized = FinalReportSerializer(report, many=True)
        return Response(serialized.data)

class SupportTicketList(APIView):
    def get(self, request, format=None):
        ticket = PomeSupporticket.objects.all()
        serialized = SupportSerializer(ticket, many=True)
        return Response(serialized.data)

class CustomerFeedbackList(APIView):
    def get(self, request, format=None):
        feedback = PomeCustomerFeedback.objects.all()
        serialized = CustomerFeedbackSerializer(feedback, many=True)
        return Response(serialized.data)

class GatepassList(APIView):
    def get(self, request, format=None):
        gatepass = PomeGatepass.objects.all()
        serialized = GatepassSerializer(gatepass, many=True)
        return Response(serialized.data)

def gatepass_add(request):
    context_dict = {}
    emp = mymodels.PomeEmloyees.objects.all()
    
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        gatepass_form = PomeGatepassForm(data=request.POST)
        #print "request post : ", request.POST
        if gatepass_form.is_valid():
            gatepass = gatepass_form.save()
            done = True
        else:
            "sorry "
            print gatepass_form
    else:
        gatepass_form = PomeGatepassForm()
    return render_to_response('gatepass_add.html',
     {'gatepass_form': gatepass_form,
     'done': done, 'emp':emp}, context)


def notice_board_add(request):
    context_dict = {}
    
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        notice_form = PomeNoticeBoardForm(data=request.POST)
        #print "request post : ", request.POST
        if notice_form.is_valid():
            notice = notice_form.save()
            done = True
        else:
            "sorry "
            print notice_form
    else:
        notice_form = PomeNoticeBoardForm()
    return render_to_response('notice_board_add.html',
     {'notice_form': notice_form,
     'done': done}, context)


def discipline_add(request):
    
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        discipline_form = PomeDisciplineComplianceForm(data=request.POST)
        #print "request post : ", request.POST
        if discipline_form.is_valid():
            discipline = discipline_form.save()
            done = True
        else:
            "sorry "
            print discipline_form
    else:
        discipline_form = PomeDisciplineComplianceForm()
    
    
    return render_to_response('discipline_add.html',
     {'discipline_form': discipline_form,
     'done': done}, context)


def biodata_add(request):
    
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        biodata_form = PomeEmloyeesForm(data=request.POST)
        #print "request post : ", request.POST
        if biodata_form.is_valid():
            biodata = biodata_form.save()
            done = True
        else:
            "sorry "
            print biodata_form
    else:
        biodata_form = PomeEmloyeesForm()
    
    
    return render_to_response('biodata_add.html',
     {'biodata_form': biodata_form,
     'done': done}, context)


def locationwise_incentive_add(request):
    loc = mymodels.PomeManageClientsLocations.objects.all()
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        location_form = PomeIncentiveLocForm(data=request.POST)
        #print "request post : ", request.POST
        if location_form.is_valid():
            location = location_form.save()
            done = True
        else:
            "sorry "
            print location_form
    else:
        location_form = PomeIncentiveLocForm()
    
    
    return render_to_response('locationwise_incentive_add.html',
     {'location_form': location_form,
     'done': done, 'loc':loc}, context)


def location_setting_incentive_not_add(request):
    loc = mymodels.PomeManageClientsLocations.objects.all()
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        location_incentive_form = PomeLocationIncentiveForm(data=request.POST)
        #print "request post : ", request.POST
        if location_incentive_form.is_valid():
            location_incentive = location_incentive_form.save()
            done = True
        else:
            "sorry "
            print location_incentive_form
    else:
        location_incentive_form = PomeLocationIncentiveForm()
       
    return render_to_response('location_setting_incentive_not_add.html',
     {'location_incentive_form': location_incentive_form,
     'done': done, 'loc':loc}, context)


def loan_types_add(request):
    
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        loantypes_form = PomeLoanTypesForm(data=request.POST)
        #print "request post : ", request.POST
        if loantypes_form.is_valid():
            loantypes = loantypes_form.save()
            done = True
        else:
            "sorry "
            print loantypes_form
    else:
        loantypes_form = PomeLoanTypesForm()
       
    return render_to_response('loan_types_add.html',
     {'loantypes_form': loantypes_form,
     'done': done}, context)


def client_add(request):
    
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        client_form = PomeManageClientsForm(data=request.POST)
        #print "request post : ", request.POST
        if client_form.is_valid():
            client = client_form.save()
            done = True
        else:
            "sorry "
            print client_form
    else:
        client_form = PomeManageClientsForm()
    
    
    return render_to_response('client_add.html',
     {'client_form': client_form,
     'done': done}, context)


def loyality_bonus_add(request):
    
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        loyality_form = PomeLoyalityBonusForm(data=request.POST)
        #print "request post : ", request.POST
        if loyality_form.is_valid():
            loyality = loyality_form.save()
            done = True
        else:
            "sorry "
            print loyality_form
    else:
        loyality_form = PomeLoyalityBonusForm()
    
    
    return render_to_response('loyality_bonus_add.html',
     {'loyality_form': loyality_form,
     'done': done}, context)


def vendor_add(request):
    
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        vendor_form = PomeManageVendorWorkshopForm(data=request.POST)
        #print "request post : ", request.POST
        if vendor_form.is_valid():
            vendor = vendor_form.save()
            done = True
        else:
            "sorry "
            print vendor_form
    else:
        vendor_form = PomeManageVendorWorkshopForm()
    
    
    return render_to_response('vendor_add.html',
     {'vendor_form': vendor_form,
     'done': done}, context)


def ticket_add(request):
    
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        ticket_form = PomeSupporticketForm(data=request.POST)
        #print "request post : ", request.POST
        if ticket_form.is_valid():
            ticket = ticket_form.save()
            done = True
        else:
            "sorry "
            print ticket_form
    else:
        ticket_form = PomeSupporticketForm()
    
    
    return render_to_response('ticket_add.html',
     {'ticket_form': ticket_form,
     'done': done}, context)


def visitor_add(request):
    emp = mymodels.PomeEmloyees.objects.all()
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        visitor_form = PomeVisitorForm(data=request.POST)
        #print "request post : ", request.POST
        if visitor_form.is_valid():
            visitor = visitor_form.save()
            done = True
        else:
            "sorry "
            print visitor_form
    else:
        visitor_form = PomeVisitorForm()
    
    return render_to_response('visitor_add.html',
     {'visitor_form': visitor_form,
     'done': done, 'emp': emp}, context)


def task_add(request):
    emp = mymodels.PomeEmloyees.objects.all()
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        task_form = PomeTaskManagementForm(data=request.POST)
        #print "request post : ", request.POST
        if task_form.is_valid():
            task = task_form.save()
            done = True
        else:
            "sorry "
            print task_form
    else:
        task_form = PomeTaskManagementForm()

    return render_to_response('task_add.html',
     {'task_form': task_form,
     'done': done, 'emp': emp}, context)


def trainer_add(request):
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        trainer_form = PomeTrainerForm(data=request.POST)
        #print "request post : ", request.POST
        if trainer_form.is_valid():
            trainer = trainer_form.save()
            done = True
        else:
            "sorry "
            print trainer_form
    else:
        trainer_form = PomeTrainerForm()

    return render_to_response('trainer_add.html',
     {'trainer_form': trainer_form,
     'done': done}, context)


def incentive_add(request):
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        incentive_form = PomeReferenceIncentiveForm(data=request.POST)
        #print "request post : ", request.POST
        if incentive_form.is_valid():
            incentive = incentive_form.save()
            done = True
        else:
            "sorry "
            print incentive_form
    else:
        incentive_form = PomeReferenceIncentiveForm()

    return render_to_response('incentive_add.html',
     {'incentive_form': incentive_form,
     'done': done}, context)


def master_add(request):
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        master_form = PomeMastersForm(data=request.POST)
        #print "request post : ", request.POST
        if master_form.is_valid():
            master = master_form.save()
            done = True
        else:
            "sorry "
            print master_form
    else:
        master_form = PomeMastersForm()

    return render_to_response('master_add.html',
     {'master_form': master_form,
     'done': done}, context)


def consultancy_add(request):
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        consultancy_form = PomeConsultancyForm(data=request.POST)
        #print "request post : ", request.POST
        if consultancy_form.is_valid():
            consultancy = consultancy_form.save()
            done = True
        else:
            "sorry "
            print consultancy_form
    else:
        consultancy_form = PomeConsultancyForm()

    return render_to_response('consultancy_add.html',
     {'consultancy_form': consultancy_form,
     'done': done}, context)


def loan_advance_setting_add(request):
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        loan_form = PomeLoanAdvancesForm(data=request.POST)
        #print "request post : ", request.POST
        if loan_form.is_valid():
            loan = loan_form.save()
            done = True
        else:
            "sorry "
            print loan_form
    else:
        loan_form = PomeLoanAdvancesForm()

    return render_to_response('loan_advance_setting_add.html',
     {'loan_form': loan_form,
     'done': done}, context)


def master_edit(request, id):
    context = RequestContext(request)
    instance = get_object_or_404(PomeMasters, id=id)
    form = PomeMastersForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/master_type/')
    return render_to_response('master_add.html', {'form': form}, context)


def loyality_edit(request, id):
    context = RequestContext(request)
    instance = get_object_or_404(PomeLoyalityBonous, id=id)
    form = PomeLoyalityBonousForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/loyality_bonus/')
    return render_to_response('loyality__bonus_add.html', {'form': form}, context)



def gatepass_edit(request, id):
    context = RequestContext(request)
    instance = get_object_or_404(PomeGatepass, id=id)
    form = PomeGatepassForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('gatepass_employee.html')
    return render_to_response('gatepass_add.html', {'form': form}, context)


def clients_edit(request, id):
    context = RequestContext(request)
    instance = get_object_or_404(PomeManageClients, id=id)
    form = PomeManageClientsForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('manage_clients.html')
    return render_to_response('client_add.html', {'form': form}, context)


def incentive_edit(request, id):

    context = RequestContext(request)
    instance = get_object_or_404(PomeReferenceIncentive, id=id)
    form = PomeReferenceIncentiveForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/reference_incentive_settings/')
    return render_to_response('incentive_add.html', {'form': form}, context)


def vendor_edit(request, id):
    context = RequestContext(request)
    instance = get_object_or_404(PomeVendorWorkshop, id=id)
    form = PomeManageVendorWorkshopForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('manage_vendors_workshops.html')
    return render_to_response('vendor_add.html', {'form': form}, context)

def trainer_edit(request, id):
    context = RequestContext(request)
    instance = get_object_or_404(PomeTrainer, id=id)
    form = PomeTrainerForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('trainer_settings.html')
    return render_to_response('trainer_add.html', {'form': form}, context)


def consultancy_edit(request, id):
    context = RequestContext(request)
    instance = get_object_or_404(PomeConsultancies, id=id)
    form = PomeConsultancyForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/consultancy/')
    return render_to_response('consultancy_add.html', {'form': form}, context)

def locationwise_incentive_edit(request, id):
    loc = mymodels.PomeManageClientsLocations.objects.all()
    context = RequestContext(request)
    instance = get_object_or_404(PomeIncentiveLoc, id=id)
    form = PomeIncentiveLocForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/incentive_setting_loc/')
    return render_to_response('locationwise_incentive_add.html', {'form': form, 'loc':loc}, context)


def locationwise_incentive_delete(request, id):
    incentive = mymodels.PomeIncentiveLoc.objects.filter(id=id).delete()
    context_dict = {'incentive': incentive}
    return render(request, 'incentive_setting_loc.html', context_dict)


def vendor_view(request, id):
    vendor = mymodels.PomeVendorWorkshop.objects.filter(id=id)
    context_dict = {'vendor': vendor}
    return render(request, 'manage_vendors_workshops.html', context_dict)

def client_view(request, id):
    client = mymodels.PomeManageClients.objects.filter(id=id)
    context_dict = {'client': client}
    return render(request, 'manage_clients.html', context_dict)

def client_delete(request, id):
    client = mymodels.PomeManageClients.objects.filter(id=id).delete()
    context_dict = {'client': client}
    return render(request, 'manage_clients.html', context_dict)

def incentive_delete(request, id):
    incentive = mymodels.PomeReferenceIncentive.objects.filter(id=id).delete()
    context_dict = {'incentive': incentive}
    return render(request, 'reference_incentive_settings.html', context_dict)

def loyality_delete(request, id):
    loyality = mymodels.PomeLoyalityBonous.objects.filter(id=id).delete()
    context_dict = {'loyality': loyality}
    return render(request, 'loyality_bonus.html', context_dict)



def manage_client(request):
    client = mymodels.PomeManageClients.objects.all()
    context_dict = {'client': client}
    return render(request, 'manage_clients.html', context_dict)


def task_view(request, id):
    task = mymodels.PomeTaskManagement.objects.filter(id=id)
    context_dict = {'task': task}
    return render(request, 'task_management.html', context_dict)

def task_delete(request, id):
    task = mymodels.PomeTaskManagement.objects.filter(id=id).delete()
    context_dict = {'task': task}
    return render(request, 'task_management.html', context_dict)

def loan_advances_delete(request, id):
    loan = mymodels.PomeLoanAdvances.objects.filter(id=id).delete()
    context_dict = {'loan': loan}
    return render(request, 'loan_advance_setting.html', context_dict)


def location_setting_incentive_not_delete(request, id):
    loc = mymodels.PomeLocationIncentive.objects.filter(id=id).delete()
    context_dict = {'loc': loc}
    return render(request, 'location_incentive_setting.html', context_dict)


def master_delete(request, id):
    master = mymodels.PomeMasters.objects.filter(id=id).delete()
    context_dict = {'master': master}
    return render(request, 'master_type.html', context_dict)

def loan_advance_delete(request, id):
    loan = mymodels.PomeLoansAdvances.objects.filter(id=id).delete()
    context_dict = {'loan': loan}
    return render(request, 'loan_advance_setting.html', context_dict)


def consultancy_delete(request, id):
    consultancy = mymodels.PomeConsultancies.objects.filter(id=id).delete()
    context_dict = {'consultancy': consultancy}
    return render(request, 'consultancy.html', context_dict)


    	
'''def readonly(request, model_name):
    context_dict = {}
    template_name = '%s.html' % model_name.lower()
    return render(request, template_name, context_dict)'''

def inward_others(request):
    context_dict = {}
    inward_others = mymodels.PomeInward.objects.all()
    context_dict = {'inward_others': inward_others}
    return render(request, 'inward_others.html', context_dict)
	
def inward_stock(request):
    context_dict = {}
    inward_stock = mymodels.PomeInward.objects.all()
    context_dict = {'inward_stock': inward_stock}
    return render(request, 'inward_stock.html', context_dict)
	
def outward_management(request):
    context_dict = {}
    outward_management = mymodels.PomeOutward.objects.all()
    context_dict = {'outward_management': outward_management}
    return render(request, 'outward_management.html', context_dict)
	
def acknowledgement(request):
    context_dict = {}
    Acknowledgement = mymodels.PomeAcknowledgement.objects.all()
    context_dict = {'Acknowledgement': Acknowledgement}
    return render(request, 'Acknowledgement.html', context_dict)

def cut_salary(request):
    context_dict = {}
    cut_salary = mymodels.PomeEmloyees.objects.all()
    context_dict = {'cut_salary': cut_salary}
    return render(request, 'cut_salary.html', context_dict)	
	
def attendance_ho(request):
    context_dict = {}
    attendance_ho = mymodels.PomeEmployeeAttendence.objects.all()
    context_dict = {'attendance_ho': attendance_ho}
    return render(request, 'attendance_ho.html', context_dict)

def employee_leaves(request):
    context_dict = {}
    employee_leaves = mymodels.PomeEmloyees.objects.all()
    context_dict = {'employee_leaves': employee_leaves}
    return render(request, 'employee_leaves.html', context_dict)

def leaves_applications(request):
    context_dict = {}
    leaves_applications = mymodels.PomeLeavesAbsents.objects.all()
    context_dict = {'leaves_applications': leaves_applications}
    return render(request, 'leaves_applications.html', context_dict)

def leaves_application_approval(request):
    context_dict = {}
    leaves_application_approval = mymodels.PomeLeavesAbsents.objects.all()
    context_dict = {'leaves_application_approval': leaves_application_approval}
    return render(request, 'leaves_application_approval.html', context_dict)

def location_attendence(request):
    context_dict = {}
    location_attendence = mymodels.PomeEmployeeAttendence.objects.all()
    context_dict = {'location_attendence': location_attendence}
    return render(request, 'location_attendence.html', context_dict)
	
def location_incharge(request):
    context_dict = {}
    location_incharge = mymodels.PomeEmloyees.objects.all()
    context_dict = {'location_incharge': location_incharge}
    return render(request, 'location_incharge.html', context_dict)

def designation_payroll(request):
    context_dict = {}
    designation_payroll = mymodels.PomeAllowanceMaster.objects.all()
    context_dict = {'designation_payroll': designation_payroll}
    return render(request, 'designation_payroll.html', context_dict)

def employee_wise(request):
    context_dict = {}
    employee_wise = mymodels.PomeAllowanceMaster.objects.all()
    context_dict = {'employee_wise': employee_wise}
    return render(request, 'employee_wise.html', context_dict)

def photoupload(request):
    context_dict = {}
    photoupload = mymodels.PomeEmloyees.objects.all()
    context_dict = {'photoupload': photoupload}
    return render(request, 'photoupload.html', context_dict)
	


def rota_hours_exceeded(request):
    context_dict = {}
    rota_hours_exceeded = mymodels.PomeExcessAttendance.objects.all()
    context_dict = {'rota_hours_exceeded': rota_hours_exceeded}
    return render(request, 'rota_hours_exceeded.html', context_dict)

def send_sms(request):
    context_dict = {}
    send_sms = mymodels.PomeExcessAttendance.objects.all()
    context_dict = {'send_sms': send_sms}
    return render(request, 'send_sms.html', context_dict)

def separation(request):
    context_dict = {}
    separation = mymodels.PomeEmloyees.objects.all()
    context_dict = {'separation': separation}
    return render(request, 'separation.html', context_dict)	
	
def staff_type(request):
    context_dict = {}
    staff_type = mymodels.PomeEmloyees.objects.all()
    context_dict = {'staff_type': staff_type}
    return render(request, 'staff_type.html', context_dict)	

def manage_vendors_workshops(request):
    context_dict = {}
    manage_vendors_workshops = mymodels.PomeVendorWorkshop.objects.all()
    context_dict = {'manage_vendors_workshops': manage_vendors_workshops}
    return render(request, 'manage_vendors_workshops.html', context_dict)

def manage_quotation(request):
    context_dict = {}
    client = mymodels.PomeManageClient.objects.all()
    manage_quotation = mymodels.PomeManageQuotation.objects.all()
    context_dict = {'manage_quotation': manage_quotation, 'client':client}
    return render(request, 'manage_quotation.html', context_dict)


def client(request):
    context_dict = {}
    client = mymodels.PomeClientBilling.objects.all()
    work_order = mymodels.PomeManageClient.objects.all()
    context_dict = {'work_order': work_order, 'client':client}
    return render(request, 'work_order.html', context_dict)	
	
def editable_attendance(request):
    context_dict = {}
    editable_attendance = mymodels.PomeVendorWorkshop.objects.all()
    context_dict = {'editable_attendance': editable_attendance}
    return render(request, 'editable_attendance.html', context_dict)

def employee_movement(request):
    context_dict = {}
    client = mymodels.PomeEmployeeMovement.objects.all()
    employee_movement = mymodels.PomeClientBilling.objects.all()
    context_dict = {'employee_movement': employee_movement, 'client':client}
    return render(request, 'employee_movement.html', context_dict)

def item_requisition_approve(request):
    context_dict = {}
    item_requisition_approve = mymodels.PomeItemRequisition.objects.all()
    context_dict = {'item_requisition_approve': item_requisition_approve}
    return render(request, 'item_requisition_approve.html', context_dict)

def item_requisition_assignment(request):
    context_dict = {}
    item_requisition_assignment = mymodels.PomeItemRequisition.objects.all()
    context_dict = {'item_requisition_assignment': item_requisition_assignment}
    return render(request, 'item_requisition_assignment.html', context_dict)



def manage_item(request):
    items = mymodels.PomeManageItems.objects.all()
    context_dict = {'items': items}
    return render(request, 'manage_item.html', context_dict)
  
  
def manage_itemedit(request, id):
    context = RequestContext(request)
    instance = get_object_or_404(PomeManageItems, id=id)
    item_form = PomeManageItemsForm(request.POST or None, instance=instance)
    if item_form.is_valid():
        item_form.save()
        done = "True"
        return render_to_response('manage_itemadd.html', {'item_form': item_form, 'done':done},  context)
    return render_to_response('manage_itemadd.html', {'item_form': item_form}, context)
 
 
def idcard(request):
    ids = mymodels.PomeBiodata.objects.all()
    context_dict = {'ids': ids}
    return render(request, 'listidcard.html', context_dict)


 
 
def individual_issuance(request):
    issn = mymodels.PomeItemRequisition.objects.all()
    context_dict = {'issn': issn}
    return render(request, 'individual_issuance_admin.html', context_dict) 
 
 
def issue_item_emp(request):
    emps = mymodels.PomeEmloyees.objects.all()
    context_dict = {'emps': emps}
    return render(request, 'issue_item_emp.html', context_dict)
 
 
def manage_store(request):
    stores = mymodels.PomeManageStores.objects.all()
    context_dict = {'stores': stores}
    return render(request, 'manage_store.html', context_dict)
 

def store_edit(request, id):
    context_dict = {}
    store = mymodels.PomeManageStores.objects.get(id = id)
    instance = get_object_or_404(PomeManageStores, id=id)
    store_form = PomeManageStoresForm(request.POST or None, instance=instance)
    if store_form.is_valid():
        store_form.save()
        done = "True"
        return render_to_response('manage_store.html', {'done':done},  context_dict)
    return render_to_response('store_edit.html', {'store_form': store_form}, context_dict)
 
def store_delete(request, id):
    store = mymodels.PomeManageStores.objects.get(id = id).delete()
    return render(request, 'manage_store.html', context_dict)
 

  
def purchase_order(request):
    porders = mymodels.PomePurchaseOrder.objects.all()
    context_dict = {'porders': porders}
    return render(request, 'purchase_order.html', context_dict)



'''def stock_status(request):
    context = RequestContext(request)
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    print q
    
    status = PomeUsersLog.objects.filter(Q(login_type__icontains = q) | Q(login_type__contains=q))
    return render_to_response('userlog.html', {'log': log, 'category': q}, context)'''




def movementreport(request):
    context = RequestContext(request)
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    print q
    
    movement = PomeEmployeeMovement.objects.filter(Q(job_status__contains = q) | Q(job_status__contains=q))
    emp = mymodels.PomeEmloyees.objects.all()
    return render_to_response('movementreport.html', {'movement': movement,'emp':emp, 'category': q}, context)


def clientdetailsform(request):
    client = mymodels.PomeManageClients.objects.all()
    context_dict = {'client': client}
    return render(request, 'clientdetailsform.html', context_dict)



def clientdetailsreport(request):
    
    context = RequestContext(request)
    
    
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    print q
    
    cdetails = PomeManageClients.objects.filter(Q(client_name__contains = q) | Q(client_name__contains=q))
    
    return render_to_response('clientdetailsreport.html', {'cdetails': cdetails, 'category': q}, context)



def epfesiform(request):
    emp = mymodels.PomeSalaries.objects.all()
    context_dict = {'emp': emp}
    return render(request, 'epfesiform.html', context_dict)

def epfesireport(request):
    
    context = RequestContext(request)
    
    
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        print q
    
    epfesi = PomeSalaries.objects.filter(Q(work_order_id__exact = q) | Q(work_order_id__exact=q))
    
    return render_to_response('epfesireport.html', {'epfesi': epfesi, 'category': q}, context)


def paymentfieldform(request):
    emp = mymodels.PomeSalaries.objects.all()
    context_dict = {'emp': emp}
    return render(request, 'paymentfieldform.html', context_dict)


def paymentfieldreport(request):
    
    context = RequestContext(request)
    
    
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        print "q is ", q
    
    payment = PomeSalaries.objects.filter(Q(work_order_id__exact = q) | Q(work_order_id__exact=q))
    
    return render_to_response('paymentfieldreport.html', {'payment': payment, 'category': q}, context)



def authorisedstrengthform(request):
    client = mymodels.PomeClientBilling.objects.all()
    context_dict = {'client': client}
    return render(request, 'authorisedstrengthform.html', context_dict)

def authorisedstrengthreport(request):
    
    context = RequestContext(request)
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    print q
        
    authstrength = mymodels.PomeClientBilling.objects.filter(Q(authorised__icontains = q) | Q(authorised__icontains=q))
    
    return render_to_response('authorisedstrengthreport.html', {'authstrength': authstrength, 'category': q}, context)


def locationattendanceform(request):
    employee = mymodels.PomeClientAttendance.objects.all()
    context_dict = {'employee': employee}
    return render(request, 'locationattendanceform.html', context_dict)

def locationattendancereport(request):
    
    context = RequestContext(request)
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    print q

    attendance = mymodels.PomeClientAttendance.objects.filter(Q(work_order_id__exact = q) | Q(work_order_id__iexact = q))

    return render_to_response('locationattendancereport.html', {'attendance': attendance, 'category': q}, context)


def idcardform(request):
    employee = mymodels.PomeEmloyees.objects.all()
    context_dict = {'employee': employee}
    return render(request, 'idcardform.html', context_dict)


def idcardreport(request):
    
    context = RequestContext(request)
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    print q
    idcard = mymodels.PomeEmloyees.objects.filter(Q(id__exact = q) | Q(id__exact=q))
    return render_to_response('idcardreport.html', {'idcard': idcard, 'category': q}, context)



def otallowform(request):
    salaries = mymodels.PomeSalaries.objects.all()
   
    context_dict = {'salaries': salaries}
    return render(request, 'otallowform.html', context_dict)


def otnotform(request):
    salaries = mymodels.PomeSalaries.objects.all()
   
    context_dict = {'salaries': salaries}
    return render(request, 'otnotform.html', context_dict)

def specialfieldform(request):
    salaries = mymodels.PomeSalaries.objects.all()
   
    context_dict = {'salaries': salaries}
    return render(request, 'specialfieldform.html', context_dict)


def otnot(request):
    context = RequestContext(request)

    '''if 'month' in request.GET and request.GET['month']:
        month = request.GET['month']
    if 'year' in request.GET and request.GET['year']:
        year = request.GET['year']'''
    
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    '''print q
    print month
    print year
    
    no_of_days = monthrange(year,month)[1]
    start_date = "year" + "-month" + "-01"
    end_date = "year" + "-month" + "-no_of_days"
    
    sundays = len([1 for i in calendar.monthcalendar(datetime.now().year,
                                  datetime.now().month) if i[6] != 0])'''
    
    designation = mymodels.PomeSalaries.objects.filter(Q(pome_emloyees_id_id__exact = q) & Q(month__exact=q)& Q(year__exact=q))
    #employee1 = PomeSalaries.objects.filter(Q(pome_emloyees_id_id__contains = q) | Q(pome_emloyees_id_id__contains=q))
    return render_to_response('otnot.html', {'designation': designation, 'category': q}, context)


def specialfield(request):
    context = RequestContext(request)

    if 'month' in request.GET and request.GET['month']:
        month = request.GET['month']
    if 'year' in request.GET and request.GET['year']:
        year = request.GET['year']
    
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    print q
    print month
    print year
    
    ''' no_of_days = monthrange(year,month)[1]
    start_date = "year" + "-month" + "-01"
    end_date = "year" + "-month" + "-no_of_days"
    
    sundays = len([1 for i in calendar.monthcalendar(datetime.now().year,
                                  datetime.now().month) if i[6] != 0])'''
    
    designation2 = mymodels.PomeSalaries.objects.filter(Q(pome_emloyees_id_id__exact = q) & Q(month__exact=month) & Q(year__exact=year))
    #employee1 = PomeSalaries.objects.filter(Q(pome_emloyees_id_id__contains = q) | Q(pome_emloyees_id_id__contains=q))
    return render_to_response('specialfield.html', {'designation2': designation2, 'category': q}, context)


def otallow(request):
    washing = []
    annual_bonus= []
    annual_bonus_total = []
    basic = []
    cal_basic = []
    context = RequestContext(request)

    if 'employee' in request.GET and request.GET['employee']:
        employee = request.GET['employee']  
 
    if 'year' in request.GET and request.GET['year']:
        year = request.GET['year']
        
    if 'month' in request.GET and request.GET['month']:
        month = request.GET['month']
    print employee
    print month
    print year
    year = int(year)
    month = int(month)
    
    no_of_days = monthrange(year,month)[1]
    
    start_date = str(year) + "-" + str(month) + "-" + "01"
    end_date = str(year) + "-" + str(month) + "-" + str(no_of_days)
    print start_date
    sundays = len([1 for i in calendar.monthcalendar(datetime.now().year,
                                  datetime.now().month) if i[6] != 0])
    remaining_days_in_month = no_of_days - sundays
    washing = mymodels.PomeWashings.objects.all().order_by('-id')
    annual_bonus = mymodels.PomeAnnualbonus.objects.all().order_by('-id')
    for ab in annual_bonus:
    	limit_months = ab.limit_months
        month_eligible = ab.month_eligible
        annualbonus_limit_percentage = ab.percentage
    leave_period = mymodels.PomeLeavePeriod.objects.filter(status=1).order_by('-id')
    for lp in leave_period:
    	from_date = lp.from_date
        to_date = lp.to_date
    cursor = connection.cursor()
    permenant_location = "SELECT * FROM `myproject_pomeemployeemovement` WHERE `emp_name_id`='employee' AND `job_status`='Permanent' AND `status`=0"
    cursor.execute(permenant_location)

    fines_qry= "SELECT SUM(amount) FROM myproject_pomefinedeductions WHERE `emp_id_id`='employee' AND `month`='month' AND `year`='year'"
    cursor.execute(fines_qry)
    fines = mymodels.PomeFineDeductions.objects.raw(fines_qry)
    print fines
    designation1 = mymodels.PomeSalaries.objects.filter(Q(pome_emloyees_id_id__exact = employee) | Q(month__exact=month) | Q(year__exact=year))
    #context_dict['employee'] = employee
    
    return render_to_response('otallow.html', {'designation1':designation1, 'month':month, 'year':year}, context)





def trainingform(request):
    training = mymodels.PomeFinalReport.objects.all()
    context_dict = {'training': training}
    return render(request, 'trainingform.html', context_dict)

def trainingreport(request):
    
    context = RequestContext(request)
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    print q
        
    trreport = mymodels.PomeFinalReport.objects.filter(Q(biodata_id_id__exact = q))
    
    return render_to_response('trainingreport.html', {'trreport': trreport, 'category': q}, context)



def empbulksearch(request):
    print "-----------------------    nagas 1 -------------------------------------------"
    print "-" * 20 
    print "-" * 20 
    balancex = []
    datex = []
    locperday = []
    rotax = []
    empdata = []
    context_dict = {}
    if 'loca' in request.GET and request.GET['loca']:
        loca = request.GET['loca']

    if 'to_date' in request.GET and request.GET['to_date']:
        to_date = request.GET['to_date']
    
    locaobj = mymodels.PomeManageClientsLocations.objects.get(name = loca)
    context_dict['locacid'] = locaobj.cid_id
    context_dict['locationsid'] = locaobj.id


    tod = datetime.datetime.strptime(to_date, '%d-%m-%Y')
    diff_days = datetime.timedelta(days=1)
    condition_days = 7
    start_date = (tod - datetime.timedelta(days=5)).strftime('%Y-%m-%d')
    for i in [5,4,3,2,1,0]:
        diff_days = datetime.timedelta(days=i)
        from_date = (tod - diff_days).strftime('%Y-%m-%d')
        cbs = mymodels.PomeClientBilling.objects.filter(work_order_no = locaobj, date__lt=from_date, todate__gt=from_date)
        totalallowch = 0
        datex.append(from_date)
        for cb in cbs:
           totallo = float(cb.hour) * float(cb.noofpersons)
           totalallowch = totallo + totalallowch
           
          # print totallo, " - " , float(cb.hour) , " - ",  float(cb.noofpersons) , " - " , totalallowch

        locperday.append(totalallowch)   

        hrsql  = "SELECT SUM(hours) as hours,date,id,employee_id_id,work_order_id,status,locations_id,month_year,designation_id FROM myproject_pomeemployeeattendence WHERE date = '" + str(from_date) + "' AND work_order_id = " + str(locaobj.id)
        try:
            rh2 = mymodels.PomeEmployeeAttendence.objects.raw(hrsql)
#              rotahours = mymodels.PomeEmployeeAttendence.objects.filter(date= from_date, work_order_id = locaobj.id).aggregate(hours = Sum('hours'))['hours']
       
            for rhh in rh2:
                if rhh.hours != 0 and rhh.hours is not None:
            #            print "rota ius :", rhh.hours
                        balance = totalallowch - float(rhh.hours)
                        rotax.append(rhh.hours)
                        balancex.append(balance)
                else:
                    balance = totalallowch   
                    rotax.append(0)
                    balancex.append(balance)
                       
        except Exception, Argument:
           print Exception, Argument
           print sys.exc_traceback.tb_lineno
    
    
    tops_date = tod.strftime('%Y-%m-%d')
 #   print "todate:", tops_date
 #   print "frmodate:", start_date

    cursor = connection.cursor()
    selemps = "select distinct(emp_name_id), pmm.name, pee.firstname, pee.lastname, pee.employeno, pee.id from myproject_pomeemployeemovement as pem, myproject_pomemanagemasters as pmm, myproject_pomeemloyees as pee where work_order_id = '" + str(locaobj.id) + "' and from_date < '" + str(start_date) + "' and '" + str(tops_date) + "'  and pem.designation_id = pmm.id and pem.emp_name_id = pee.id order by emp_name_id"
    print selemps
    cursor.execute(selemps)
    #selempdata = mymodels.PomeEmployeeMovement.objects.raw(selemps)
    selemprows = cursor.fetchall()
    print "hi vishnu", selemprows
   # selpmsdata = mymodels.PomeEmployeeMovement.objects.filter(work_order= locaobj).values('emp_name_id', 'firstname', 'lastname', 'designationtxt').distinct().order_by('emp_name_id')

    
    #print type(from_date), type(tod)
   # emphrscountsql = " SELECT id, employee_id_id, designation_id, sum(hours) FROM myproject_pomeemployeeattendence  where status = 'Present'  AND work_order_id = " + str(locaobj.id) + " group by employee_id_id"
    
 #   print selemps  
   # print "all locan emps:, ", selemprows    


  #  emphrscountsql = " SELECT pee.employee_id_id, pee.designationtxt as pdsng, group_concat(date), group_concat(hours), pee.firstname, pee.lastname, pee.employeno  FROM kcitsplc_ssms.myproject_pomeemployeeattendence as pee where date between  '" +  str(start_date) + "' and '" + str(tops_date) + "' and work_order_id = '" + str(locaobj.cid_id) + "' group by employee_id_id"

 
    emphrscountsql = "SELECT pee.employee_id_id, pee.employeno, group_concat(date), group_concat(hours), group_concat(work_order_id),  pee.firstname, pee.lastname, pee.designationtxt FROM kcitsplc_ssms.myproject_pomeemployeeattendence as pee where pee.employee_id_id in (select distinct(emp_name_id) from myproject_pomeemployeemovement where work_order_id = '" + str(locaobj.id) + "' and from_date < '" + str(start_date) + "' and '" + str(tops_date) + "' ) and date between  '" +  str(start_date) + "' and '" + str(tops_date) + "' group by employee_id_id"



    #emphrs = mymodels.PomeEmployeeAttendence.objects.raw(emphrscountsql)
    #empdata.append(emphrs)
    print emphrscountsql
    cursor.execute(emphrscountsql)
    emphrs = cursor.fetchall()
    print "vishnu", emphrs
    emphrslist = [list(i) for i in emphrs]	
    zerohrslist = [0,0,0,0,0,0,0]
    conemplist = [i[0] for i in emphrslist]
    conselemplis = [j[0] for j in selemprows]
    temp3 = [item for item in conselemplis if item not in conemplist]



    for i in emphrslist:
        i[3]  =list(i[3].split(','))
        i[2] = [datetime.datetime.strptime(x, '%Y-%m-%d') for x in list(i[2].split(','))]
        i[4] = list(i[4].split(','))   
        hrsum = sum( [int(d) for d in i[3]] )

        ziplist = zip(i[2], i[3], i[4])
        ziplist.sort(key = lambda t: t[0])
        i.append(ziplist)
        i.append(hrsum)
        #print "ziplist is:", ziplist


    pk = []
    for dj in range(6):
        djtuple = (datetime.datetime.strptime(datex[dj], '%Y-%m-%d'), "", "")
        pk.append([djtuple])

    
    print "-" * 20
    print "pk is ", pk   

    #print len(pk)

    print "before: "
    for n in emphrslist:
        print n


    print "-" * 40

    for ae in emphrslist:
        ae.append([[],[],[],[],[],[]])
        print "k"
        for k in ae[8]:
           print "k is ", ae, k[0], pk[0][0][0]
           if k[0] == pk[0][0][0]:
            ae[10][0].append(k)
           if k[0] == pk[1][0][0]:
            print "k is ", ae, k[0], pk[1][0][0]
            ae[10][1].append(k)
           if k[0] == pk[2][0][0]:
            print "k is ", ae, k[0], pk[2][0][0]
            ae[10][2].append(k)
           if k[0] == pk[3][0][0]:
            print "k is ", ae, k[0], pk[3][0][0]
            ae[10][3].append(k)
           if k[0] == pk[4][0][0]:
            print "k is ", ae, k[0], pk[4][0][0]
            ae[10][4].append(k)
           if k[0] == pk[5][0][0]:
            print "k is ", ae, k[0], pk[5][0][0]
            ae[10][5].append(k)

        for pj in range(6):
            if len(ae[10][pj]) == 0:
                ae[10][pj].append(pk[pj])


    if len(temp3) > 0:
       for t in temp3:
	    for se in selemprows:
                    if se[0] == t:
       #                   print se[0], " - ", t
	                  litem = [se[5], se[4], "","","", se[2], se[3], se[1], "","0", pk]
                          emphrslist.append(litem)
                          break 

    print "-" * 40

    print "after "
    for m in emphrslist:
        print m 



  #  djemphrscsql = PomeEmployeeAttendence.objects.values('employeno', 'firstname', 'lastname', 'designationtxt', 'date', 'hours').filter( work_order_id = str(locaobj.id), date__gte = str(start_date), date__lte = tops_date)
   
    
    context_dict['emphrslist'] = emphrslist
    context_dict['start_date'] = start_date
    context_dict['tops_date'] = tops_date
    
 #   context_dict['selpmsdata'] = selemprows
    actual_hours=''
    total_hours=''
    leaves_count=''
    bsent_count='' 
    present_count=''
    fet_dates_now=''
    result_dates=''
    leaves_count=''
    clp_qry_count=''
    gr_employ_qry_total=''
    overtime_hours=''

   # result = 
    
    context_dict['locperday'] = locperday
    context_dict['datex'] = datex
    context_dict['balancex'] = balancex
    context_dict['rotax'] = rotax
    
    
    context_dict['loca'] = loca
    context_dict['to_date'] = to_date
     
    return render(request, 'empbulksearch.html', context_dict) 



def saveatt(request):
    updated = False
    print "--------   nagas 2---------" * 20
    empid = request.POST['empid']
    chattn = request.POST.getlist('chattn[]')
    chadat = request.POST.getlist('chadat[]')
    chahrs = request.POST.getlist('chahrs[]')
    desig = request.POST['desig']
    start_date = request.POST['start_date']
    locationsid = request.POST['locationsid']
    print "start date is ", start_date 
    tops_date = request.POST['tops_date']
    workorder = request.POST['workorder']
    locacid = request.POST['locacid']
    #print "chattn is ", chattn
    #print "chattn is ", chadat
    #print "chattn is ", chahrs
  # filterwarnings('ignore', category = MySQLdb.Warning) 
    cursor = connection.cursor()
    print  "locaid is ", locacid
    print  "workorder is ", workorder
    print  "locatnsid is ", locationsid
    print  "chattn is ", chattn
    print  "chattn is ", chadat
    print  "desig is ", desig

    empdetail = PomeEmloyees.objects.get(id = empid)


    employeno = str(empdetail.employeno).strip()
    empfn = str(empdetail.firstname).strip()
    empln = str(empdetail.lastname).strip()
    empdesig = str(desig).strip()
    
    print "group data is ", employeno, empfn, empln, empdesig
    locperday = []
    balancex = []
    rotax = []
    
    

    for i in range(len(chattn)):
        try:
            insq = "INSERT INTO kcitsplc_ssms.myproject_pomeemployeeattendence (date, hours, status, employee_id_id, work_order_id, locations_id, employeno, firstname, lastname, designationtxt) VALUES ('%s', '%s', 'Present','%s','%s', '%s','%s','%s', '%s', '%s')"  %(chadat[i], chahrs[i], empid, locationsid, locacid, employeno, empfn, empln, empdesig)
            print insq
            cursor.execute(insq)

        except Exception, e:
            print "exece ", e
    retdata = " SELECT pee.employee_id_id, group_concat(date), group_concat(hours), group_concat(work_order_id)  FROM 	kcitsplc_ssms.myproject_pomeemployeeattendence as pee where date between  '" +  str(start_date) + "' and '" + str(tops_date) + "' and employee_id_id = '" + str(empid) + "'"
    print retdata
    cursor.execute(retdata)
    try:

        ae = list(cursor.fetchone())
        ae[2]  = str(ae[2]).split(',')
        ae[1] = [datetime.datetime.strptime(x, '%Y-%m-%d') for x in list(str(ae[1]).split(','))]
        ae[3] = list(ae[3].split(','))  
    #    ziplist = zip(ae[1], ae[2])
    #    ziplist.sort(key = lambda t: t[0])
     #   ae.append(ziplist
        hrsum = sum( [int(d) for d in ae[2]] )
        ziplist = zip(ae[1], ae[2], ae[3])
        ziplist.sort(key = lambda t: t[0])
        ae.append(ziplist)
        ae.append(hrsum)
    except Exception, e:
        print Exception, e        

    datex = []
    try:

	    for i in [5,4,3,2,1,0]:
                diff_days = datetime.timedelta(days=i)
		frtops_date = datetime.datetime.strptime(tops_date, '%Y-%m-%d')
                from_date = (frtops_date - diff_days).strftime('%Y-%m-%d')
		datex.append(from_date)
	    
	    print "datex is ", datex


    except Exception, e:
        print Exception, e

	
    pk = []
    for dj in range(6):
        djtuple = (datetime.datetime.strptime(datex[dj], '%Y-%m-%d'), "", "")
        pk.append([djtuple])


    print pk
    
    print "before ae ", ae
    print "lent is ", len(ae[1])

    response_data = {}


    ae.append([[],[],[],[],[],[]])
    for k in ae[4]:

       if k[0] == pk[0][0][0]:
        print "k is ", k, pk[0][0][0]
        ae[6][0].append(k)
        response_data['hrs0'] = k[1]
        response_data['lcn0name'] = locationsid

       if k[0] == pk[1][0][0]:
        print "k is ", k, pk[1][0][0]
        ae[6][1].append(k)
        response_data['hrs1'] = k[1]
        response_data['lcn1name'] = locationsid

       if k[0] == pk[2][0][0]:
        print "k is ", k, pk[2][0][0]
        ae[6][2].append(k)
        response_data['hrs2'] = k[1]
        response_data['lcn2name'] = locationsid

       if k[0] == pk[3][0][0]:
        print "k is ", k, pk[3][0][0]
        ae[6][3].append(k)
        response_data['hrs3'] = k[1]
        response_data['lcn3name'] = locationsid

       if k[0] == pk[4][0][0]:
        print "k is ", k, pk[4][0][0]
        ae[6][4].append(k)
        response_data['hrs4'] = k[1]
        response_data['lcn4name'] = locationsid

       if k[0] == pk[5][0][0]:
        print "k is ", k, pk[5][0][0]
        ae[6][5].append(k)
        response_data['hrs5'] = k[1]
        response_data['lcn5name'] = locationsid

    for pj in range(6):
        if len(ae[6][pj]) == 0:
            ae[6][pj].append(pk[pj])


    print "afteddr ae ", ae
    connection.commit()

    print "rd is ", response_data




    locaobj = mymodels.PomeManageClientsLocations.objects.get(name = workorder)
    print "locaobj is ", locaobj
    for i in [5,4,3,2,1,0]:
        diff_days = datetime.timedelta(days=i)
        ftopdate = datetime.datetime.strptime(tops_date, '%Y-%m-%d')
        fstart_date = (ftopdate - diff_days).strftime('%Y-%m-%d')
        
        cbs = mymodels.PomeClientBilling.objects.filter(work_order_no = locaobj, date__lt=fstart_date, todate__gt=fstart_date)
        totalallowch = 0
        for cb in cbs:
           totallo = float(cb.hour) * float(cb.noofpersons)
           totalallowch = totallo + totalallowch
           
          # print totallo, " - " , float(cb.hour) , " - ",  float(cb.noofpersons) , " - " , totalallowch

        locperday.append(totalallowch)   

        hrsql  = "SELECT SUM(hours) as hours,date,id FROM myproject_pomeemployeeattendence WHERE date = '" + str(fstart_date) + "' AND work_order_id = " + str(locaobj.id)
        print hrsql
        try:
            rh2 = mymodels.PomeEmployeeAttendence.objects.raw(hrsql)
#              rotahours = mymodels.PomeEmployeeAttendence.objects.filter(date= from_date, work_order_id = locaobj.id).aggregate(hours = Sum('hours'))['hours']
            for rhh in rh2:
                print "rota :", rhh.hours
                if rhh.hours != 0 and rhh.hours is not None:

                        print "rota ius :", rhh.hours , rhh.date
                        balance = totalallowch - float(rhh.hours)
                        rotax.append(rhh.hours)
                        balancex.append(balance)
                else:
                    balance = totalallowch   
                    rotax.append(0)
                    balancex.append(balance)
                       
        except Exception, Argument:
           print Exception, Argument
           print sys.exc_traceback.tb_lineno
    

    print balancex

    print rotax
    print "totalhrs  ", ae[5]

    urotax = [int(y) for y in rotax]


    response_data['ttlhrs'] = ae[5]
    response_data['balancex'] = balancex
    response_data['rotax'] = urotax
     #try:

    #     jsonx = json.dumps({'ttlhrs': ae[5], 'balancex': balancex, 'rotax':urotax})
     #except Exception, jx:
      #   print Exception, jx

    return HttpResponse(json.dumps(response_data), content_type="application/json")
  #  return HttpResponse(jsonx, content_type="application/json")



def salgen1(request):
    return HttpResponseRedirect("http://google.com/salgfden1")

def k1webservices(request):
    return HttpResponseRedirect("http://google.com/salgfden1")

def ssms(request):
    return HttpResponseRedirect("http://google.com/salgfden1")

def tmpls(request, tname):
    context_dict = {}
    return render(request, 'tmpls/' + str(tname), context_dict)


'''def dictfetchall(cursor):
    """Returns all rows from a cursor as a list of dicts"""
    desc = cursor.description
    return [dict(itertools.izip([col[0] for col in desc], row)) 
        for row in cursor.fetchall()]

def getcalevents(request):
    retdata = " SELECT title, url, start, end , class, pe.firstname as pfn, pe.lastname  FROM kcitsplc_ssms.myproject_pometaskmanagement as pt, kcitsplc_ssms.myproject_pomeemloyees as pe where pt.assign_to_id = pe.id order by pt.id desc" 
    cursor = connection.cursor()
    cursor.execute(retdata)
    tasks_unjs  = dictfetchall(cursor)
    tasks = json.dumps(tasks_unjs)
    response_data = {}
    response_data['events'] = tasks
    return HttpResponse(json.dumps(response_data), content_type="application/json")'''


def addevent(request):
    context_dict = {}
    starttime = request.POST['starthidden']
    print "post params: \n "
    for key, value in request.POST.items():
        print(key, value)
    print request.user
    euser = mymodels.PomeEmloyees.objects.get(employeno=request.user).id
    print euser
    start_date = request.POST['start']
    task_summary = request.POST['desc']
    assignto = request.POST['assignto']
    print "start date is ", start_date
    event = PomeTaskManagement.objects.create(task_summery = task_summary, assigned_by_id = euser, status = "warning", start_date =   start_date,   start= starttime, assign_to_id = assignto)
    event.save()
    return HttpResponseRedirect('/')





@login_required
def readysupport(request):
    context = RequestContext(request)
    context_dict = {}

    done = False
    if request.method == 'POST':

        emp = request.user
        comment = request.POST['comment']
        empid =  mymodels.PomeEmloyees.objects.get(id=2)
        ticket = mymodels.PomeSupporticket.objects.create(subject = "test", mail_from = empid, message = comment)
        ticket.save()
        context_dict['done'] = True
        return HttpResponseRedirect('/admin/myproject/pomesupporticket/')



def loginreport(request):
    context_dict = {}
    cursor = connection.cursor()
    loginsql = "SELECT * FROM kcitsplc_ssms.tracking_visitor"
    cursor.execute(loginsql)
    ldata = cursor.fetchall()
    context_dict = {'ldata': ldata}
    print dir(ldata) 
    return render(request, 'logininfo.html', context_dict)


def error404(request):
    response = render_to_response('404.html', {},
        context_instance=RequestContext(request))
    response.status_code = 404
    return response


def police_verification(request):
    context_dict = {}
    police_verification = mymodels.PomeEmloyees.objects.all()
    context_dict = {'police_verification': police_verification}
    return render(request, 'police_verification.html', context_dict)


def police_verification_id(request, id):
    context_dict = {}
    police_verification_id = mymodels.PomeEmloyees.objects.get(id=id)
    context_dict = {'police_verification_id': police_verification_id}
    return render(request, 'police_verification_id.html', context_dict)


def customer_feedback_id(request, id):
    context_dict = {}
    customer_feedback_id = PomeCustomerFeedback.objects.get(id=id)
    context_dict = {'customer_feedback_id': customer_feedback_id}
    return render(request, 'customer_feedback_id.html', context_dict)


def single_patrolling(request, id):
    context_dict = {}
    single_patrolling_id = mymodels.PomePatrolling.objects.get(id=id)
    context_dict = {'single_patrolling_id': single_patrolling_id}
    return render(request, 'print_single_patrolling.html', context_dict)


def mobile_patrolling(request, id):
    context_dict = {}
    mobile_patrolling = mymodels.PomeMobilePatrolling.objects.get(id=id)
    #patrolling = mobile_patrolling.objects.all()
    context_dict = {'mobile_patrolling': mobile_patrolling}
    return render(request, 'print_mobile_patrolling.html', context_dict)


@login_required 
def gencerthome(request):
    context = RequestContext(request)
    context_dict = {}
    emps = PomeEmloyees.objects.all()
    context_dict['emps'] = emps
    return render_to_response('gencert.html', context_dict, context)


@login_required 
def gencert(request):
    context = RequestContext(request)
    context_dict = {}
    empid  = request.GET["empid"]
    e = PomeEmloyees.objects.get(employeno = empid)
    fname = e.firstname
    lname = e.lastname
    fathername = e.father_name
    constring = "python img.py " +  fname  + " " +  lname  + " " + fathername
    print constring
    os.system(constring)
    print "generating ....."
    return render_to_response('gencert.html', context_dict, context)


def my_handler(sender, instance, created, **kwargs):
    recipient = User.objects.get(username="k1@gmail.com")
    notify.send(instance, verb='was saved in Biodata', recipient=recipient)

post_save.connect(my_handler, sender=PomeBiodata)


'''def my_employee(sender, instance, created, **kwargs):
    notify.send(comment.user, recipient=group, verb=u'was saved in Biodata', action_object=comment,
            description=comment.comment, target=comment.content_object)

    notify.send(follow_instance.user, recipient=follow_instance.follow_object, verb=u'was saved in Biodata',
            action_object=instance, description=u'', target=follow_instance.follow_object, level='success')

post_save.connect(my_handler, sender=PomeBiodata)

post_save.connect(my_employee, sender=PomeEmloyees)'''


@login_required 
def genauth(request, id):
    context = RequestContext(request)
    context_dict = {}
    cursor = connection.cursor()
    access_pagesql  = "SELECT permission_id FROM kcitsplc_ssms.auth_user_user_permissions where user_id = " + id
    cursor.execute(access_pagesql)
    accpages = list(cursor.fetchall())
    listacc = []
    for lcp in accpages:
        listacc.append(lcp[0])
    
    if request.method == "POST":
        selpass = []
        selected = request.POST.getlist('main_menu[]')
        for i in selected:
            for x in i.split(' '):
                selpass.append(x)
        print listacc
        print selpass
        newaccesslist = set(selpass) - set(listacc)
        try:

            for new in newaccesslist:
                print new
                accql = "INSERT INTO kcitsplc_ssms.auth_user_user_permissions (user_id, permission_id) VALUES ('%s', '%s')" % (id, new) 
                cursor.execute(accql)
        except Exception, Argument:
            print Exception, Argument


        delaccesslist = set(listacc) - set(selpass)
        try:

            for delacc in delaccesslist:
                print delacc
                delql = "delete from kcitsplc_ssms.auth_user_user_permissions where user_id = %s and permission_id = %s" % (id, delacc) 
                cursor.execute(delql)


        except Exception, Argument:
            print Exception, Argument


        return HttpResponseRedirect('/admin/auth/user/')


    else:
        context_dict['accpages'] = listacc
        return render_to_response('assignauth.html', context_dict, context)
