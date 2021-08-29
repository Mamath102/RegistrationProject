from django.shortcuts import render,redirect
from .models import Register
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request,'regapp/home.html')

class RegisteredDetails(ListView):
    model=Register

class Create(CreateView):
    model=Register
    fields = ('name','email','mobile_Number')

class Update(UpdateView):
    model=Register
    fields = ('name','email','mobile_Number')

class Delete(DeleteView):
    model=Register
    success_url =reverse_lazy('detail')







