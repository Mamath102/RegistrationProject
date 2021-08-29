from django.contrib import admin
from regapp.models import Register
# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','mobile_Number']

admin.site.register(Register,RegisterAdmin)