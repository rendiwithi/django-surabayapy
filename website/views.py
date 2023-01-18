from django.shortcuts import render
from api import models
# Create your views here.

def test(request):
    return render(request, 'redirect_page.html', {'page':{
        'title':'surabaya.py',
        'link_url':'https://t.me/surabayadotpy',
        "raw_url":'https://t.me/surabayadotpy',
    }})

def telegram(request):
    return render(request, 'redirect_page.html', {'page':{
        'title':'surabaya.py',
        'link_url':'https://t.me/surabayadotpy',
        "raw_url":'https://t.me/surabayadotpy',
    }})

def discord(request):
    return render(request, 'redirect_page.html', {'page':{
        'title':'surabaya.py',
        'link_url':'https://t.me/surabayadotpy',
        "raw_url":'https://t.me/surabayadotpy',
    }})
def twitter(request):
    return render(request, 'redirect_page.html', {'page':{
        'title':'surabaya.py',
        'link_url':'https://t.me/surabayadotpy',
        "raw_url":'https://t.me/surabayadotpy',
    }})
def instagram(request):
    return render(request, 'redirect_page.html', {'page':{
        'title':'surabaya.py',
        'link_url':'https://www.instagram.com/surabaya.py/?hl=id',
        "raw_url":'https://www.instagram.com/surabaya.py/?hl=id',
    }})

def youtube(request):
    return render(request, 'redirect_page.html', {'page':{
        'title':'surabaya.py',
        'link_url':'https://www.youtube.com/@pythonsurabaya5848',
        "raw_url":'https://www.youtube.com/@pythonsurabaya5848',
    }})

def index(request):
    content = models.Event.objects.all()
    return render(request, 'index.html', {'SITENAME': 'surabaya.py', 'content' :content})

def eventdetail(request, idevent):
    content = models.Event.objects.get(id=idevent)
    return render(request, 'event_page.html', {'SITENAME': 'surabaya.py', 'content' :content})
