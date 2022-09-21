# TODO: Implement Routings Here

from django.urls import path
from mywatchlist.views import indexJson, indexXml, indexHtml

app_name = 'mywatchlist'

urlpatterns = [
    path('json/', indexJson, name='indexJson'),
    path('xml/', indexXml, name='indexXml'),
    path('html/', indexHtml, name='indexHtml')

]