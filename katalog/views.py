from dataclasses import field
import os
from django.shortcuts import render
from katalog.models import CatalogItem
import json

name = "Bimo Priyohutomo"
student_id = "2106708444"
item = []

f = open('katalog/fixtures/initial_catalog_data.json', 'r')

item_data = json.loads(f.read())

for i in item_data:
    item.append(CatalogItem(item_name=i['fields']['item_name'], item_price=i['fields']['item_price'], item_stock=i['fields']['item_stock'], description=i['fields']['description'], rating=i['fields']['rating'], item_url=i['fields']['item_url']))

# TODO: Create your views here. 
def index(request):
    response = {
        'name': name,
        'id': student_id,
        'item' : item,
    }
    return render(request, 'katalog.html', response)
