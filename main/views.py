from django.shortcuts import render
from django.views import View
from .models import *

class HomeView(View):
    def get(self, request):
        data = {
            'bolimlar' : Bolim.objects.all()[:7],
            'discount' : Mahsulot.objects.filter(chegirma__gt=0).order_by('chegirma')[:5]
        }
        return render(request, 'page-index.html', data)

class Home2View(View):
    def get(self, request):
        data = {
            'discount' : Mahsulot.objects.filter(chegirma__gt=0).order_by('chegirma')[:5]
        }
        return render(request, 'page-index-2.html')