from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/accounts/login/")
def homepage(request):
    buses = Article.objects.all().order_by('date')
    return render(request, 'main/homepage.html', {'articles': buses})


@login_required(login_url="/accounts/login/")
def bus_details(request, slug):
    # return HttpResponse(slug)
    buses = Article.objects.get(slug=slug)
    return render(request, 'main/bus_details.html', {'article': buses})





