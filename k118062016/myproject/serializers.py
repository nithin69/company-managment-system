from rest_framework import serializers
from myproject.models import *

class OutwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomeOutward

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomeEmloyees

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomeDisciplineCompliance

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomeManageClients

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomeVendorWorkshop

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomeVisitor

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomeTaskManagement

class BiodataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomeBiodata

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomeEmployeeAttendence

class NoticeBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomeNoticeboard

class FinalReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomeFinalReport

class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomeSupporticket

class CustomerFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomeCustomerFeedback

class GatepassSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomeGatepass

