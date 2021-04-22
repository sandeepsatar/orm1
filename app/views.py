from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert(request):
    if request.method=='POST':
        #print(request.POST['topic'])
        #return HttpResponse(request.POST.get('topic'))
        topic_name=request.POST['topic']
        t=Topic.objects.get_or_create(topic_name=topic_name)[0]
        t.save()
        return HttpResponse('data is inserted successfuly')
    return render(request,'insert.html')

def webpage(request):
    if request.method=='POST':
        topicname=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        t=Topic.objects.get_or_create(topic_name=topicname)[0]
        t.save()
        w=Webpage.objects.get_or_create(topic_name=t,name=name,url=url)[0]
        w.save()
        return HttpResponse('data is inserted into webpage')        
    return render(request,'webpage.html')    
def acess(request):
    if request.method=='POST': 
        topicname=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        date=request.POST['date']
        t=Topic.objects.get_or_create(topic_name=topicname)[0]
        t.save()
        w=Webpage.objects.get_or_create(topic_name=t,name=name,url=url)[0]
        w.save()
        a=Access_Records.objects.get_or_create(name=w,date=date)[0]
        a.save()
        return HttpResponse('data is inserted into webpage')        
    
    return render(request,'acess.html')


def select(request):
    topics=Topic.objects.all()
    if request.method=='POST':
        topicname=request.POST['topic']
        t=Topic.objects.get_or_create(topic_name=topicname)[0]
        t.save()
        webpages=Webpage.objects.filter(topic_name=t)
        
        d={'webpages':webpages}
        return render(request,'display.html',d)
    return render(request,'select.html',context={'topics':topics})

def delete(request):
    topics=Topic.objects.all()
    if request.method=='POST':
        topicname=request.POST['topic']
        Webpage.objects.filter(topic_name=topicname).delete()
        webpages=Webpage.objects.all()
        d={'webpages':webpages}
        return render(request,'display.html',d)
    return render(request,'drop.html',context={'topics':topics})
    
      


            
