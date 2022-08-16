from django.shortcuts import render , redirect
from email import message
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import CreateView
from .models import User
from .forms import SupplierSignUpForm, EmployeeSignUpForm

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

class supplier_register(CreateView):
    model = User  
    form_class = SupplierSignUpForm
    template_name= 'supplier_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/home')

class employee_register(CreateView):
    model = User  
    form_class = EmployeeSignUpForm
    template_name= 'employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/home')

def login_user(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/accounts/home')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, 'login.html',context={'form':AuthenticationForm()})

def logout_user(request):
    logout(request)
# Create your views here.
