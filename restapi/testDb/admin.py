from django.contrib import admin
from .models import Employee
from .models import Role


# Register your models here.
admin.site.register(Employee)
admin.site.register(Role)