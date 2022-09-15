
from django.shortcuts import render
from katalog.models import CatalogItem

name = "Bimo Priyohutomo"
student_id = "2106708444"


# TODO: Create your views here. 
def index(request):
    response = {
        'name': name,
        'id': student_id,
        'item' : CatalogItem.objects.all(),
    }
    return render(request, 'katalog.html', response)
