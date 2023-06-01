from django.shortcuts import render , HttpResponseRedirect
from .forms import InscriptionForm
from .models import Inscription
from . import models

def index(request):
    liste = models.Inscription.objects.all()
    return render(request, 'projet/index.html', {"liste":liste})


def confirmation(request):
    lform = InscriptionForm(request.POST)
    if lform.is_valid():
        Inscription = lform.save()
        return HttpResponseRedirect ('/projet/')
    else:
        return render(request,'projet/create.html',{"form": lform})

def create(request):
    if request.method == "POST":
        form = InscriptionForm(request)
        if form.is_valid():
            Inscription = form.save()
            return render(request,'projet/confirmation.html',{"Insrciption" : Inscription})
        else:
            return render(request,'projet/create.html',{"form": form})
    else :
        form = InscriptionForm()
        return render(request,'projet/create.html',{"form" : form})

def read(request, id):
    Inscription = models.Inscription.objects.get (pk= id)
    return render(request,'projet/read.html',{"Inscription": Inscription})

def update(request,id):
    Inscription = models.Inscription.objects.get(pk=id)
    form = InscriptionForm(Inscription.dico())
    return render(request, "projet/create.html" ,{"form":form, "id": id})

def traitementupdate(request, id):
    lform = InscriptionForm(request.POST)
    if lform.is_valid():
        Inscription = lform.save(commit=False)
        Inscription.id = id;
        Inscription.save()
        return HttpResponseRedirect('/projet/')
    else:
        return render(request, 'projet/update.html', {"form": lform, "id": id})

def delete(request, id):
    Inscription = models.Inscription.objects.get(pk=id)
    Inscription.delete()
    return HttpResponseRedirect('/projet/')
