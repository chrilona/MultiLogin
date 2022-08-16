from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('home/', views.home, name='home'),
    path('supplier_register/', views.supplier_register.as_view(), name='supplier_register'),
    path('employee_register/', views.employee_register.as_view(), name='employee_register')
]