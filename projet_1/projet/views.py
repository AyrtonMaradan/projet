from django.shortcuts import render , HttpResponseRedirect
from .forms import InscriptionForm, ParcForm
from .models import Inscription, Parc
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
        Inscription.id = id
        Inscription.save()
        return HttpResponseRedirect('/projet/')
    else:
        return render(request, 'projet/update.html', {"form": lform, "id": id})

def delete(request, id):
    Inscription = models.Inscription.objects.get(pk=id)
    Inscription.delete()
    return HttpResponseRedirect('/projet/')

#########################################################

#PARC :


def confirmationparc(request):
    pform = ParcForm(request.POST)
    if pform.is_valid():
        Parc = pform.save()
        return HttpResponseRedirect ('/projet/')
    else:
        return render(request,'projet/parc/createparc.html',{"form": pform})

def createparc(request):
    if request.method == "POST":
        pform = ParcForm(request)
        if pform.is_valid():
            Parc = pform.save()
            return render(request,'parc/confirmationparc.html',{"Parc" : Parc})
        else:
            return render(request,'parc/createparc.html',{"form": pform})
    else :
        pform = ParcForm()
        return render(request,'parc/createparc.html',{"form" : pform})

def readparc(request, id):
    Parc = models.Parc.objects.get (pk= id)
    return render(request,'parc/readparc.html',{"Parc": Parc})

def updateparc(request,id):
    Parc = models.Parc.objects.get(pk=id)
    form = ParcForm(Parc.dico())
    return render(request, "parc/createparc.html" ,{"form":form, "id": id})

def traitementupdateparc(request, id):
    pform = ParcForm(request.POST)
    if pform.is_valid():
        Parc = pform.save(commit=False)
        Parc.id = id;
        Parc.save()
        return HttpResponseRedirect('/projet/')
    else:
        return render(request, 'parc/updateparc.html', {"form": pform, "id": id})

def deleteparc(request, id):
    Parc = models.Parc.objects.get(pk=id)
    Parc.delete()
    return HttpResponseRedirect('/projet/')