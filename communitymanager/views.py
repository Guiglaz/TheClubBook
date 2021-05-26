from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from communitymanager.models import *
from django.http import Http404
from communitymanager.forms import *

# Create your views here.
def first_page(request):
    if request.user.is_authenticated:
        return redirect(communautes)

    return render(request, 'first_page.html')


@login_required(login_url='/accounts/login/')
def communautes(request):
    date_now=timezone.now()
    list_com = Communaute.objects.all()
    nb_commu = len(list_com)
    return render(request, 'communitymanager/communautes.html', locals())


@login_required(login_url='/accounts/login/')
def communaute(request, id_commu, nom_commu):
    try:
        commu = get_object_or_404(Communaute, id=id_commu, nom=nom_commu)
    except Http404:
        return redirect(communautes)

    date_now=timezone.now()
    nb_abonnes=len(commu.abonnes.all())
    list_post = commu.posts.all()
    nb_post = len(list_post)
    return render(request, 'communitymanager/communaute.html', locals())


@login_required(login_url='/accounts/login/')
def post(request, id_post, slug_post):
    try:
        post = get_object_or_404(Post, id=id_post, slug=slug_post)
    except Http404:
        return redirect(communautes)

    form = CommentaireForm(request.POST or None)
    if form.is_valid():
        Commentaire.objects.create(post=post,auteur=request.user, contenu=form.cleaned_data.get('commenter'))
        form = CommentaireForm()
#        return redirect(post, id=id_post, slug=slug_post)


    date_now=timezone.now()
    list_com = post.commentaires.all()
    nb_com = len(list_com)
    nb_likes = len(post.likes.all())

    return render(request, 'communitymanager/post.html', locals())


@login_required(login_url='/accounts/login/')
def nouveau_post(request):
    form = MyPostForm(request.POST or None)
    if form.is_valid():
        print('ok')
    return render(request, 'communitymanager/nouveau_post.html', locals())


@login_required(login_url='/accounts/login/')
def modif_post(request):

    return render(request, 'communitymanager/modif_post.html', locals())


@login_required(login_url='/accounts/login/')
def news_feed(request):
    date_now=timezone.now()

    return render(request, 'communitymanager/news_feed.html', locals())
