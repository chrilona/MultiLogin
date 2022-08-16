# from re import A
from django.contrib import admin
from .models import User,Employee, Supplier

admin.site.register(Supplier)
admin.site.register(Employee)
admin.site.register(User)
# Register your models here.
