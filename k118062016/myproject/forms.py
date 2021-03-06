from django import forms
from myproject.models import *
from django.core.exceptions import ValidationError
#from djangular.styling.bootstrap3.forms import Bootstrap3Form
from django.forms.extras.widgets import SelectDateWidget
from django.forms import widgets
from django.forms import extras
import datetime
from dal import autocomplete


class StafftypeForm(forms.ModelForm):
	employee_id = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))



class OjtForm(forms.ModelForm):
        ojt_employees = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))


class FineForm(forms.ModelForm):
        emp_id = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
        pot = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))


class PomePatrollingForm(forms.ModelForm):

	patrolling_officer = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	patrolling_officer2 = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	name = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))


class WashingForm(forms.ModelForm):
        washing_emp = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))



class PayrollForm(forms.ModelForm):
	employee_id = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	designation = forms.ModelChoiceField(queryset=PomeManageMasters.objects.all(), widget=autocomplete.ModelSelect2(url='designation-autocomplete'))

class ManageitemsForm(forms.ModelForm):
	threshold_to1 = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))

class PatrollingForm(forms.ModelForm):
	patrolling_person = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	employeeid = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))

class PomeGatepassForm(forms.ModelForm):

	emp_name = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
        issuedby = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
        #designation = forms.ModelChoiceField(queryset=PomeManageMasters.objects.all(), widget=autocomplete.ModelSelect2(url='designation-autocomplete'))


class PomeIncentiveForm(forms.ModelForm):
	designation = forms.ModelChoiceField(queryset=PomeManageMasters.objects.all(), widget=autocomplete.ModelSelect2(url='designation-autocomplete'))


class PomeDesignationIncentiveForm(forms.ModelForm):
	designation_id = forms.ModelChoiceField(queryset=PomeManageMasters.objects.all(), widget=autocomplete.ModelSelect2(url='designation-autocomplete'))
	items_id = forms.ModelChoiceField(queryset=PomeManageItems.objects.all(),widget=autocomplete.ModelSelect2(url='items-autocomplete'))


class LocationinchargeForm(forms.ModelForm):

	employee_id = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))

class PomeEmployeeMovementForm(forms.ModelForm):

	emp_name = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	#designation = forms.ModelChoiceField(queryset=PomeManageMasters.objects.all(), widget=autocomplete.ModelSelect2(url='designation-autocomplete'))
	def clean(self):
    		from_date = self.cleaned_data.get("from_date")
    		to_date = self.cleaned_data.get("to_date")
    		if to_date < from_date:
        		msg = u"To date should be greater than From date."
        		self._errors["to_date"] = self.error_class([msg])
		#if from_date < datetime.date.today() - datetime.timedelta(days = 31):
		#	msg = u"From Date cant be less than a Week."
		#	self._errors["from_date"] = self.error_class([msg])



class PomeInwardForm(forms.ModelForm):

	items = forms.ModelChoiceField(queryset=PomeManageItems.objects.all(),widget=autocomplete.ModelSelect2(url='items-autocomplete'))
        received_by = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	to = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	invoice_no = forms.ModelChoiceField(queryset=PomeClientInvoice.objects.all(), widget=autocomplete.ModelSelect2(url='invoice-autocomplete'))


class PomeOutwardForm(forms.ModelForm):

	invoice_no = forms.ModelChoiceField(queryset=PomeClientInvoice.objects.all(), widget=autocomplete.ModelSelect2(url='invoice-autocomplete'))
	per_name = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	approver = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	items = forms.ModelChoiceField(queryset=PomeManageItems.objects.all(),widget=autocomplete.ModelSelect2(url='items-autocomplete'))	
	stock_to = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))

class PomeVisitorForm(forms.ModelForm):

	staff_guid = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	
class LoanadvanceForm(forms.ModelForm):
	designation = forms.ModelChoiceField(queryset=PomeManageMasters.objects.all(), widget=autocomplete.ModelSelect2(url='designation-autocomplete'))


class CleintAttendanceForm(forms.ModelForm):

	employee_id = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))


class PomeBiodataForm(forms.ModelForm):

	post_applied = forms.ModelChoiceField(queryset=PomeManageMasters.objects.all(), widget=autocomplete.ModelSelect2(url='designation-autocomplete'))
	#reference_by = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))


class PomeFinalreportForm(forms.ModelForm):

	biodata_id = forms.ModelChoiceField(queryset=PomeBiodata.objects.all(),widget=autocomplete.ModelSelect2(url='biodata-autocomplete'))


class PomeTraineeAttendenceForm(forms.ModelForm):

	trainee_id = forms.ModelChoiceField(queryset=PomeBiodata.objects.all(),widget=autocomplete.ModelSelect2(url='biodata-autocomplete'))


class PomeAcknowledgeForm(forms.ModelForm):

	emp_id = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	#designation = forms.ModelChoiceField(queryset=PomeManageMasters.objects.all(), widget=autocomplete.ModelSelect2(url='designation-autocomplete'))

class PomeCutSalaryForm(forms.ModelForm):

	employee = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	

class PomeDisciplineForm(forms.ModelForm):

	initiated_by = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	send_to = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))


class PomeAttendenceForm(forms.ModelForm):

	employee_id = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	entered = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	designation = forms.ModelChoiceField(queryset=PomeManageMasters.objects.all(), widget=autocomplete.ModelSelect2(url='designation-autocomplete'))
	

	def clean_date(self):
        	date = self.cleaned_data['date']
        	if date > datetime.date.today():
            		raise forms.ValidationError("The date cannot be in the future!")
        	return date



class PomeLeavesForm(forms.ModelForm):

	name = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	

class NoticeBoardForm(forms.ModelForm):
	
	post_count = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	def clean(self):
    		from_date = self.cleaned_data.get("from_date")
    		to_date = self.cleaned_data.get("to_date")
    		if to_date < from_date:
        		msg = u"To date should be greater than From date."
        		self._errors["to_date"] = self.error_class([msg])

class ManageClientsLocationsForm(forms.ModelForm):
	
	cid = forms.ModelChoiceField(queryset=PomeManageClients.objects.all(),widget=autocomplete.ModelSelect2(url='client-autocomplete'))
	designation1 = forms.ModelChoiceField(queryset=PomeManageMasters.objects.all(), widget=autocomplete.ModelSelect2(url='designation-autocomplete'))

	def clean(self):
    		from_date = self.cleaned_data.get("from_date")
    		to_date = self.cleaned_data.get("to_date")
    		if to_date < from_date:
        		msg = u"To date should be greater than From date."
        		self._errors["to_date"] = self.error_class([msg])


class ManageClientsForm(forms.ModelForm):
	
	designation = forms.ModelChoiceField(queryset=PomeManageMasters.objects.all(), widget=autocomplete.ModelSelect2(url='designation-autocomplete'))
	def clean(self):
    		from_date = self.cleaned_data.get("from_date")
    		to_date = self.cleaned_data.get("to_date")
    		if to_date < from_date:
        		msg = u"To date should be greater than From date."
        		self._errors["to_date"] = self.error_class([msg])


class LeaveperiodForm(forms.ModelForm):
	
	def clean(self):
    		from_date = self.cleaned_data.get("from_date")
    		to_date = self.cleaned_data.get("to_date")
    		if to_date < from_date:
        		msg = u"To date should be greater than From date."
        		self._errors["to_date"] = self.error_class([msg])



class QuotationForm(forms.ModelForm):
	
	designation = forms.ModelChoiceField(queryset=PomeManageMasters.objects.all(), widget=autocomplete.ModelSelect2(url='designation-autocomplete'))


class SupportticketForm(forms.ModelForm):
	
	name = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	mail_from = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))


class ClientbillingForm(forms.ModelForm):
	
	designation = forms.ModelChoiceField(queryset=PomeManageMasters.objects.all(), widget=autocomplete.ModelSelect2(url='designation-autocomplete'))


	def clean(self):
    		from_date = self.cleaned_data.get("date")
    		to_date = self.cleaned_data.get("todate")
    		if to_date < from_date:
        		msg = u"To date should be greater than From date."
        		self._errors["todate"] = self.error_class([msg])



class EmployeesettlementForm(forms.ModelForm):
	emp_id = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	designation = forms.ModelChoiceField(queryset=PomeManageMasters.objects.all(), widget=autocomplete.ModelSelect2(url='designation-autocomplete'))


class ReferencepaymentForm(forms.ModelForm):
	reference_id = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))
	emp_id = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))


class EODManagementForm(forms.ModelForm):
	eod_by = forms.ModelChoiceField(queryset=PomeEmloyees.objects.all(),widget=autocomplete.ModelSelect2(url='bd-autocomplete'))



'''class PomeClientAttendanceForm(forms.ModelForm):

 	class Meta:
 		model = PomeClientAttendance

class PomeManageItemsForm(forms.ModelForm):
	class Meta:
  		model = PomeManageItems
  		fields = ['id', 'item_name', 'item_code', 'itemtype', 'category', 'measurement', 'unit_price','charge_price','threshold_limit']
  
  

class PomeManageStoresForm(forms.ModelForm):
	class Meta:
   		model = PomeManageStores
  		fields = ['store_name', 'address', 'contact_no', 'name', 'designation', 'mobile', 'email', 'status']

class PomeNoticeBoardForm(forms.ModelForm):

 	class Meta:
 		model = PomeNoticeboard
		fields = ['date', 'date_time', 'subject', 'message', 'post_to', 'priority', 'from_date', 'to_date', 'notice_type']

class PomeGatepassForm(forms.ModelForm):

 	class Meta:
 		model = PomeGatepass
		fields = ['emp_name', 'designation', 'department', 'gateno', 'gatepass_no', 'out_date', 'out_time', 'purpose', 'splinstruction']


class PomeDisciplineComplianceForm(forms.ModelForm):

 	class Meta:
 		model = PomeDisciplineCompliance
		fields = ['send_date', 'send_time', 'initiated_by', 'subject', 'description', 'send_to', 'priority']


class PomeManageClientsForm(forms.ModelForm):

 	class Meta:
 		model = PomeManageClients
		fields = ['entry_date', 'client_name', 'username', 'password', 'guard_deployement', 'from_date', 'to_date', 'propreitor', 'authorised_person', 'auth_designation', 'panno', 'tanno', 'email', 'telephone', 'mobile', 'address', 'city', 'state', 'zipcode','stax' ]

class PomeManageVendorWorkshopForm(forms.ModelForm):

 	class Meta:
 		model = PomeVendorWorkshop
		fields = ['type', 'company_vendor_name', 'username', 'password', 'company_type', 'registration_no', 'pan_no', 'regd_office_addr', 'pin_code', 'company_email', 'company_telephone', 'fax', 'tin_tan', 'city', 'district', 'state','country', 'name', 'designation', 'contact_no', 'mobile', 'email', 'bank_details', 'bank', 'ac_no', 'ifsc_no', 'branch', 'bank_type']


class PomeSupporticketForm(forms.ModelForm):

 	class Meta:
 		model = PomeSupporticket
                fields = ['subject','message']

class PomeVisitorForm(forms.ModelForm):

 	class Meta:
 		model = PomeVisitor
                fields = ['date','time','visitor_name', 'from_company', 'from_address', 'contact_number', 'emailid', 'staff_guid', 'avaliability', 'alternate_person', 'purpose']




class PomeTaskManagementForm(forms.ModelForm):

 	class Meta:
 		model = PomeTaskManagement


class PomeTrainerForm(forms.ModelForm):

 	class Meta:
 		model = PomeTrainer
                fields = ['id', 'trainer_name','phone','location']

class PomeReferenceIncentiveForm(forms.ModelForm):

 	class Meta:
 		model = PomeReferenceIncentive
                fields = ['id', 'date','amount']


class PomeMastersForm(forms.ModelForm):

 	class Meta:
 		model = PomeMasters
                fields = ['id', 'master_name','master_desc']

class PomeIncentiveLocForm(forms.ModelForm):

 	class Meta:
 		model = PomeIncentiveLoc
                fields = ['id', 'location','amount', 'totamount', 'purpose', 'date']

class PomeLoyalityBonusForm(forms.ModelForm):

 	class Meta:
 		model = PomeLoyalityBonous
                fields = ['id', 'loyality_bonous','loyality_period', 'description', 'date']

class PomeConsultancyForm(forms.ModelForm):

 	class Meta:
 		model = PomeConsultancies
                fields = ['id', 'consultancy_name','consultancy_phoneno','consultancy_address','consultancy_emailid',
			'contactperson_name', 'contactperson_phoneno', 'contactperson_emailid']

class PomeLocationIncentiveForm(forms.ModelForm):

 	class Meta:
 		model = PomeLocationIncentive
                fields = ['id', 'location']

class PomeLoanAdvancesForm(forms.ModelForm):

 	class Meta:
 		model = PomeLoansAdvances
                fields = ['id', 'designation', 'loan_limit']

class PomeLoanTypesForm(forms.ModelForm):

 	class Meta:
 		model = PomeLoanTypes
                fields = ['id', 'loan_type', 'description']

class PomeEmloyeesForm(forms.ModelForm):

 	class Meta:
 		model = PomeEmloyees
                fields = ['id', 'joining_date', 'firstname', 'middlename', 'lastname', 'shortname', 'work_email', 'gender', 'designation', 'reference_by', 'father_name', 'father_age', 'mother_name', 'mother_age', 'chest_expanded', 'chest_unexpanded', 'height', 'weight', 'identification_mark', 'photo', 'home_address1', 'home_address2', 'district', 'policestation', 'state', 'zipcode', 'dob', 'caste', 'religian', 'home_phone', 'mobile', 'years', 'school_college', 'exam_passed',  'division', 'bike', 'brother_no', 'brother', 'sister_no', 'sister']




class AcknowledgementForm(forms.ModelForm):

 	class Meta:
 		model = Acknowledgement
		


class AcknowledgementDocumentsForm(forms.ModelForm):

 	class Meta:
 		model = AcknowledgementDocuments


class ActionsForm(forms.ModelForm):

 	class Meta:
 		model = Actions


class AdvancesTypesForm(forms.ModelForm):

 	class Meta:
 		model = AdvancesTypes


class AllowanceMasterForm(forms.ModelForm):

 	class Meta:
 		model = AllowanceMaster


class AnnualbonusForm(forms.ModelForm):

 	class Meta:
 		model = Annualbonus


class BillingTaxForm(forms.ModelForm):

 	class Meta:
 		model = BillingTax




class CalendarForm(forms.ModelForm):

 	class Meta:
 		model = Calendar





class ClientBillingForm(forms.ModelForm):

 	class Meta:
 		model = ClientBilling


class ClientBranchesForm(forms.ModelForm):

 	class Meta:
 		model = ClientBranches


class ClientInvoiceForm(forms.ModelForm):

 	class Meta:
 		model = ClientInvoice


class ClientInvoiceTransactionsForm(forms.ModelForm):

 	class Meta:
 		model = ClientInvoiceTransactions


class ClientPatrollingForm(forms.ModelForm):

 	class Meta:
 		model = ClientPatrolling


class ClientPaymentTransactionsForm(forms.ModelForm):

 	class Meta:
 		model = ClientPaymentTransactions


class ConsultanciesForm(forms.ModelForm):

 	class Meta:
 		model = Consultancies


class CustomerFeedbackForm(forms.ModelForm):

 	class Meta:
 		model = CustomerFeedback


class DefaultAccessForm(forms.ModelForm):

 	class Meta:
 		model = DefaultAccess


class DefaultAdvancesForm(forms.ModelForm):

 	class Meta:
 		model = DefaultAdvances


class DisciplineComplianceForm(forms.ModelForm):

 	class Meta:
 		model = DisciplineCompliance


class DonationForm(forms.ModelForm):

 	class Meta:
 		model = Donation




class EmpAdvancesForm(forms.ModelForm):

 	class Meta:
 		model = EmpAdvances


class EmpLoansForm(forms.ModelForm):

 	class Meta:
 		model = EmpLoans


class EmpLoansTransactionsForm(forms.ModelForm):

 	class Meta:
 		model = EmpLoansTransactions


class EmployeeAttendenceForm(forms.ModelForm):

 	class Meta:
 		model = EmployeeAttendence


class EmployeeCtcForm(forms.ModelForm):

 	class Meta:
 		model = EmployeeCtc


class EmployeeExpenditureForm(forms.ModelForm):

 	class Meta:
 		model = EmployeeExpenditure


class EmployeeMovementForm(forms.ModelForm):

 	class Meta:
 		model = EmployeeMovement


class EmployeePostingForm(forms.ModelForm):

 	class Meta:
 		model = EmployeePosting


class EmployeeSeparationsForm(forms.ModelForm):

 	class Meta:
 		model = EmployeeSeparations


class EmployeeSettlementForm(forms.ModelForm):

 	class Meta:
 		model = EmployeeSettlement


class EodForwardForm(forms.ModelForm):

 	class Meta:
 		model = EodForward


class EodManagementForm(forms.ModelForm):

 	class Meta:
 		model = EodManagement


class ExcessAttendanceForm(forms.ModelForm):

 	class Meta:
 		model = ExcessAttendance


class ExcessLocAttendanceForm(forms.ModelForm):

 	class Meta:
 		model = ExcessLocAttendance


class FinalReportForm(forms.ModelForm):

 	class Meta:
 		model = FinalReport


class FineForm(forms.ModelForm):

 	class Meta:
 		model = Fine


class FineDeductionsForm(forms.ModelForm):

 	class Meta:
 		model = FineDeductions


class GalleryForm(forms.ModelForm):

 	class Meta:
 		model = Gallery





class GraderateSettingForm(forms.ModelForm):

 	class Meta:
 		model = GraderateSetting


class GuardPlacementForm(forms.ModelForm):

 	class Meta:
 		model = GuardPlacement


class HolidaysForm(forms.ModelForm):

 	class Meta:
 		model = Holidays


class IncentiveForm(forms.ModelForm):

 	class Meta:
 		model = Incentive


class IncentiveLocForm(forms.ModelForm):

 	class Meta:
 		model = IncentiveLoc


class InnermenusForm(forms.ModelForm):

 	class Meta:
 		model = Innermenus


class InvoicePaymentDeleteForm(forms.ModelForm):

 	class Meta:
 		model = InvoicePaymentDelete


class InwardForm(forms.ModelForm):

 	class Meta:
 		model = Inward


class InwardDocumentsForm(forms.ModelForm):

 	class Meta:
 		model = InwardDocuments


class InwardInvoiceForm(forms.ModelForm):

 	class Meta:
 		model = InwardInvoice


class InwardOutwardCourierForm(forms.ModelForm):

 	class Meta:
 		model = InwardOutwardCourier


class InwardOutwardFixedAssetsForm(forms.ModelForm):

 	class Meta:
 		model = InwardOutwardFixedAssets


class InwardOutwardMaterialForm(forms.ModelForm):

 	class Meta:
 		model = InwardOutwardMaterial


class IssuanceForm(forms.ModelForm):

 	class Meta:
 		model = Issuance


class ItemDesignationwiseForm(forms.ModelForm):

 	class Meta:
 		model = ItemDesignationwise


class ItemRequisitionForm(forms.ModelForm):

 	class Meta:
 		model = ItemRequisition


class K1DetailsForm(forms.ModelForm):

 	class Meta:
 		model = K1Details


class LeaveManagementForm(forms.ModelForm):

 	class Meta:
 		model = LeaveManagement


class LeavePeriodForm(forms.ModelForm):

 	class Meta:
 		model = LeavePeriod


class LeavesAbsentsForm(forms.ModelForm):

 	class Meta:
 		model = LeavesAbsents


class LoanTypesForm(forms.ModelForm):

 	class Meta:
 		model = LoanTypes


class LoansAdvancesForm(forms.ModelForm):

 	class Meta:
 		model = LoansAdvances


class LoansCalculationForm(forms.ModelForm):

 	class Meta:
 		model = LoansCalculation


class LocDesgMasterForm(forms.ModelForm):

 	class Meta:
 		model = LocDesgMaster


class LocationIncentiveForm(forms.ModelForm):

 	class Meta:
 		model = LocationIncentive


class LocationInchargeForm(forms.ModelForm):

 	class Meta:
 		model = LocationIncharge


class LocationInchargeSalariesForm(forms.ModelForm):

 	class Meta:
 		model = LocationInchargeSalaries


class LocationsalarySettingsForm(forms.ModelForm):

 	class Meta:
 		model = LocationsalarySettings


class LocdesgForm(forms.ModelForm):

 	class Meta:
 		model = Locdesg


class LocpayIncentiveForm(forms.ModelForm):

 	class Meta:
 		model = LocpayIncentive


class LoginDetailsForm(forms.ModelForm):

 	class Meta:
 		model = LoginDetails


class LoginsForm(forms.ModelForm):

 	class Meta:
 		model = Logins


class LoyalityBonousForm(forms.ModelForm):

 	class Meta:
 		model = LoyalityBonous


class ManageClientsForm(forms.ModelForm):

 	class Meta:
 		model = ManageClients


class ManageClientsLocationsForm(forms.ModelForm):

 	class Meta:
 		model = ManageClientsLocations


class ManageDepartmentsForm(forms.ModelForm):

 	class Meta:
 		model = ManageDepartments


class ManageItemsForm(forms.ModelForm):

 	class Meta:
 		model = ManageItems


class ManageMastersForm(forms.ModelForm):

 	class Meta:
 		model = ManageMasters


class ManageQuotationForm(forms.ModelForm):

 	class Meta:
 		model = ManageQuotation


class ManageStoresForm(forms.ModelForm):

 	class Meta:
 		model = ManageStores


class MastersForm(forms.ModelForm):

 	class Meta:
 		model = Masters


class MenusForm(forms.ModelForm):

 	class Meta:
 		model = Menus


class MobilePatrollingForm(forms.ModelForm):

 	class Meta:
 		model = MobilePatrolling


class MoneytransferPettycashForm(forms.ModelForm):

 	class Meta:
 		model = MoneytransferPettycash


class NoticeboardForm(forms.ModelForm):

 	class Meta:
 		model = Noticeboard


class NotificationsForm(forms.ModelForm):

 	class Meta:
 		model = Notifications


class OtherBenefitsForm(forms.ModelForm):

 	class Meta:
 		model = OtherBenefits


class OutwardForm(forms.ModelForm):

 	class Meta:
 		model = Outward


class OvertimeForm(forms.ModelForm):

 	class Meta:
 		model = Overtime


class OvertimeGeneratedForm(forms.ModelForm):

 	class Meta:
 		model = OvertimeGenerated


class OvertimePaymentForm(forms.ModelForm):

 	class Meta:
 		model = OvertimePayment


class PatrollingForm(forms.ModelForm):

 	class Meta:
 		model = Patrolling


class PattycashAccountsForm(forms.ModelForm):

 	class Meta:
 		model = PattycashAccounts


class PaymentForm(forms.ModelForm):

 	class Meta:
 		model = Payment


class PaymentCollectionForm(forms.ModelForm):

 	class Meta:
 		model = PaymentCollection


class PaymentReceiptInchargeForm(forms.ModelForm):

 	class Meta:
 		model = PaymentReceiptIncharge


class PaymentsTransfersForm(forms.ModelForm):

 	class Meta:
 		model = PaymentsTransfers


class PayscaleSettingForm(forms.ModelForm):

 	class Meta:
 		model = PayscaleSetting


class PoliceVerificationFormForm(forms.ModelForm):

 	class Meta:
 		model = PoliceVerificationForm


class PurchaseOrderForm(forms.ModelForm):

 	class Meta:
 		model = PurchaseOrder


class PurchaseRequisitionForm(forms.ModelForm):

 	class Meta:
 		model = PurchaseRequisition


class ReferenceIncentiveForm(forms.ModelForm):

 	class Meta:
 		model = ReferenceIncentive


class ReferencePaymentForm(forms.ModelForm):

 	class Meta:
 		model = ReferencePayment


class ReturnStockForm(forms.ModelForm):

 	class Meta:
 		model = ReturnStock


class ReturnStockVendorForm(forms.ModelForm):

 	class Meta:
 		model = ReturnStockVendor


class SalAssignmentForm(forms.ModelForm):

 	class Meta:
 		model = SalAssignment


class SalAssignmentEmpsForm(forms.ModelForm):

 	class Meta:
 		model = SalAssignmentEmps


class SalariesForm(forms.ModelForm):

 	class Meta:
 		model = Salaries


class SalariesGeneratedForm(forms.ModelForm):

 	class Meta:
 		model = SalariesGenerated


class SalaryDisbursementForm(forms.ModelForm):

 	class Meta:
 		model = SalaryDisbursement


class SalaryFixedForm(forms.ModelForm):

 	class Meta:
 		model = SalaryFixed


class SalaryPaymentTransactionsForm(forms.ModelForm):

 	class Meta:
 		model = SalaryPaymentTransactions


class ScaleDifferenceForm(forms.ModelForm):

 	class Meta:
 		model = ScaleDifference


class SendsmsForm(forms.ModelForm):

 	class Meta:
 		model = Sendsms


class ShiftsForm(forms.ModelForm):

 	class Meta:
 		model = Shifts


class StipendDisbursementForm(forms.ModelForm):

 	class Meta:
 		model = StipendDisbursement


class StipendTraineeForm(forms.ModelForm):

 	class Meta:
 		model = StipendTrainee


class StockUpdateForm(forms.ModelForm):

 	class Meta:
 		model = StockUpdate


class StocksForm(forms.ModelForm):

 	class Meta:
 		model = Stocks


class StocksTransactionsForm(forms.ModelForm):

 	class Meta:
 		model = StocksTransactions


class SubmenusForm(forms.ModelForm):

 	class Meta:
 		model = Submenus


class SuperAdminForm(forms.ModelForm):

 	class Meta:
 		model = SuperAdmin


class SupporticketForm(forms.ModelForm):
     
    supportfile = forms.ImageField(label="Upload File ", required=False)

    class Meta:
 		model = Supporticket
 		fields = ('id','category', 'priority', 'message', 'supportfile')


class TaskManagementForm(forms.ModelForm):

 	class Meta:
 		model = TaskManagement


class TraineeAttendenceForm(forms.ModelForm):

 	class Meta:
 		model = TraineeAttendence




class TrainingSessionForm(forms.ModelForm):

 	class Meta:
 		model = TrainingSession


class UploadWorkorderForm(forms.ModelForm):

 	class Meta:
 		model = UploadWorkorder


class UserAccessForm(forms.ModelForm):

 	class Meta:
 		model = UserAccess


class UserPermissionForm(forms.ModelForm):

 	class Meta:
 		model = UserPermission


class UsersLogForm(forms.ModelForm):

 	class Meta:
 		model = UsersLog


class VendorWorkshopForm(forms.ModelForm):

 	class Meta:
 		model = VendorWorkshop


class VisitorForm(forms.ModelForm):

 	class Meta:
 		model = Visitor


class WashingsForm(forms.ModelForm):

 	class Meta:
 		model = Washings'''

