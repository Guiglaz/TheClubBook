from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from communitymanager.models import *
from django.http import Http404

# Create your views here.
def first_page(request):
    if request.user.is_authenticated:
        return redirect(communautes)

    return render(request, 'first_page.html')


@login_required(login_url='/accounts/login/')
def communautes(request):

    return render(request, 'communitymanager/communautes.html', locals())


@login_required(login_url='/accounts/login/')
def communaute(request, id_commu, nom_commu):
    try:
        commu = get_object_or_404(Communaute, id=id_commu, nom=nom_commu)
    except Http404:
        return redirect(communautes)

    return render(request, 'communitymanager/communaute.html', locals())


@login_required(login_url='/accounts/login/')
def post(request, id_post, slug_post):
    try:
        p = get_object_or_404(Post, id=id_post, slug=slug_post)
    except Http404:
        return redirect(communautes)

    return render(request, 'communitymanager/post.html', locals())


@login_required(login_url='/accounts/login/')
def nouveau_post(request):

    return render(request, 'communitymanager/nouveau_post.html', locals())


@login_required(login_url='/accounts/login/')
def modif_post(request):

    return render(request, 'communitymanager/modif_post.html', locals())


@login_required(login_url='/accounts/login/')
def news_feed(request):

    return render(request, 'communitymanager/news_feed.html', locals())
