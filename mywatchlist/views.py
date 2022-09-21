from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from mywatchlist.models import MyWatchList

# Create your views here.
def indexJson(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def indexXml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def indexHtml(request):
    data = MyWatchList.objects.all()
    response = {
        'mywatchlist': data,
    }
    return render(request, 'mywatchlist.html', response)