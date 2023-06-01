from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from .decorators import OrganizerAndLoginRequiredDecorator



class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    def get_success_url(self):
        return reverse("login")


def landing_page(request):
    return render(request, "landing.html")



def lead_list(request):

    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request, "leads/lead_list.html", context)



def lead_detail(request, pk):
    
    lead = Lead.objects.get(id=pk)
    context = {
        'lead': lead
    }
    return render(request, 'leads/lead_detail.html', context)


@OrganizerAndLoginRequiredDecorator
def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        'form': form
    }
    return render(request, "leads/lead_create.html", context)


@OrganizerAndLoginRequiredDecorator
def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)

    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
        
    context = {
       "form": form,
        "lead": lead
        }
    return render(request, "leads/lead_update.html", context)


@OrganizerAndLoginRequiredDecorator
def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
