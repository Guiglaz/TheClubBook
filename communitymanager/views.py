from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def first_page(request):
    return render(request, 'first_page.html')


@login_required(login_url='/accounts/login/')
def connecte(request):
    return render(request, 'communitymanager/connecte.html')