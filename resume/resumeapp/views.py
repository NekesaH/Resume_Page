from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

from resume import settings

from .forms import ContactForm


# Create your views here.
def  resumePage(request):
     if request.method == "GET":
          form = ContactForm()
     elif request.method == "POST":
          form = ContactForm(request.POST)
          if form.is_valid():
               name = form.cleaned_data['name']
               email = form.cleaned_data['email']
               message = form.cleaned_data['message']
               send_mail(f"{name} sent an email", message, email, ["settings.DEFAULT_FROM_EMAIL"])
               return render(request,'resumeapp/index.html', {"form":form, "success": True} )
     else:
          raise NotImplementedError
               
          

     return render(request, 'resumeapp/index.html', {"form":form})



