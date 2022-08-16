from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from .models import  Employee, Supplier, User

class SupplierSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    product_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
       
    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.is_supplier = True
        user.save()
        supplier = Supplier.objects.create(user=user)
        supplier.product_name = self.cleaned_data.get('product_name')
        supplier.phone_number = self.cleaned_data.get('phone_number')
        supplier.save()
        return user    

class EmployeeSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    department = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.is_employee = True
        user.save()
        employee = Employee.objects.create(user=user)
        employee.phone_number = self.cleaned_data.get('phone_number')
        employee.department = self.cleaned_data.get('department')
        employee.save()
        return user
    
   
