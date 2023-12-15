from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.

# RETRIVING DATA FROM DATABASE

def display_topics(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)

def webpage(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'webpage.html',d)

def access_record(request):
    QLAO=AccessRecord.objects.all()
    d={'accessrecord':QLAO}
    return render(request,'access_record.html',d)


# BOTH INSERTION AND RETRIVING FROM DATABASE

def insert_topics(request):
    tn=input('enter tn')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()

    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)

def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')

    TO=Topic.objects.get(topic_name=tn)
    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    NWO.save()

    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'webpage.html',d)


def insert_accessrecord(request):
    # pkv=int(input('enter pk value'))
    # a=input('enter author')
    # WO=Webpage.objects.get(pk=pkv)
    # NAO=AccessRecord.objects.get_or_create(name=WO,author=a)[0]
    # NAO.save()

    QLAO=AccessRecord.objects.all()
    d={'accessrecord':QLAO}
    return render(request,'access_record.html',d)