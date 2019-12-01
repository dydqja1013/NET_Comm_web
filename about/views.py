from django.shortcuts import render
from .models import Portfolio
# Create your views here.
def about(request):
    portfolios = Portfolio.objects
    return render(request, 'about.html', {'portfolios': portfolios})