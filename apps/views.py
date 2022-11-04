from django.shortcuts import render
from .models import About, Offer, Project
from django.views.generic import UpdateView, CreateView, ListView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

# Create your views here.

def header():
    logo = About.objects.get(pk=1)
    phone = About.objects.get(pk=1)
    about = About.objects.get(pk=1)
    context = {
        'logo':logo,
        'phone':phone,
        'about':about
        }
    return context

def index(request):
    offers = Offer.objects.all().order_by('-pk')
    projects = Project.objects.all().order_by('-pk')[:3]
    logo = About.objects.get(pk=1)
    phone = About.objects.get(pk=1)
    context = {
        'offers':offers,
        'projects':projects,
        'logo':logo,
        'phone':phone
        }
    return render(request,'apps/index.html',context)

def about(request):
    
    return render(request,'apps/about.html',header())
def contact(request):
    return render(request,'apps/contact.html',header())
@login_required
def panel(request):
    return render(request,'apps/panel.html')

class AboutModel(CreateView):
    model = About
    fields = "__all__"


class UpdateLogo(LoginRequiredMixin,UpdateView):
    model = About
    fields= ['logo']
    success_url = reverse_lazy('thank_you')
class UpdatePhone(LoginRequiredMixin,UpdateView):
    model = About
    fields = ['phone']
    success_url = reverse_lazy('thank_you')
class UpdateAbout(LoginRequiredMixin,UpdateView):
    model = About
    fields = ['text']
    success_url = reverse_lazy('thank_you')
class PhotoAdd(LoginRequiredMixin,CreateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy('thank_you')
class OfferAdd(LoginRequiredMixin,CreateView):
    model = Offer
    fields = "__all__"
    success_url = reverse_lazy('thank_you')

def thank_you(request):
    return render(request,'apps/thank_you.html')

class ListOffersView(LoginRequiredMixin,ListView):
    model = Offer

class DeleteOffer(LoginRequiredMixin,DeleteView):
    model = Offer
    success_url= '/list_offer'

class ListPhotoes(LoginRequiredMixin,ListView):
    model = Project

class DeletePhotoes(LoginRequiredMixin,DeleteView):
    model = Project
    success_url = '/photo_list'

class UpdatePhoto(LoginRequiredMixin,UpdateView):
    model =Project
    fields = "__all__"
    success_url = '/photo_list'



