import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render

from scrap.models import links
from bs4 import BeautifulSoup
def index(request):
    if request.method=='POST':
        url=request.POST.get('url','')
        urls=requests.get(url)
        si=BeautifulSoup(urls.text,'html.parser')
        for li in si.find_all('a'):
            adres=(li.get('href'))
            linkname=li.string
            links.objects.create(address=adres,stringname=linkname)
        return HttpResponseRedirect('/')
    else:
        details=links.objects.all()
        return render(request,'home.html',{'adress':details})