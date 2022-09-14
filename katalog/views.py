from django.shortcuts import render
from katalog.models import CatalogItem

name = "Bimo Priyohutomo"
student_id = "2106708444"
item = CatalogItem(item_name="komputer", item_price=10000000, item_stock=4, description="komputer keren", rating=7, item_url="https://www.tokopedia.com/")

# TODO: Create your views here. 
def index(request):
    response = {
        'name': name,
        'id': student_id,
        'item' : [item],
    }
    return render(request, 'katalog.html', response)
