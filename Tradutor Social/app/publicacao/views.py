from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from .form import *
from .models import *

def home(request):    
    return render(request, 'publicacoes/home.html')

def feed(request):
    data = {}
    prof = Profile.objects.all()
    data['publicacoes'] = Publication.objects.all()
    data['account'] = prof
    data['plubication'] = Correction.objects.all()
    return render(request, 'publicacoes/feed.html', data)

@login_required
def publicar(request, pk):
    data = {}
    form = PublicationForm(request.POST or None)
    data['form'] = form
    data['username'] = request.user.pk
    if form.is_valid():
        form.save()
        return redirect('url_feed')
    return render(request, 'publicacoes/publicar.html', data)

def profile(request, pk):
    data = {}
    profile = Profile.objects.get(pk=pk)
    coment = Correction.objects.filter(publications=pk)
    data['coment'] = coment
    data['publicacoes'] = Publication.objects.filter(account=pk)
    data['dados'] = Profile.objects.filter(id=pk)
    data['profile'] = profile
    data['username'] = request.user.pk
    return render(request, 'publicacoes/profile.html', data)


def delete(request, pk):
    publicacao = Publication.objects.get(pk=pk)
    publicacao.delete()
    return redirect('url_feed')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


class RegisterView(FormView):
    def get(self, request):
        data = {}
        data['form'] = RegisterForm
        return render(request, 'publicacoes/cadastro.html', data)

    def post(self, request):
        content = {}
        form = RegisterForm(request.POST, request.FILES or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.is_staff = True
            user.is_superuser = True
            user.save()
            login(request, user)
            return redirect('home')
        content['form'] = form
        template = 'publicacoes/cadastro.html'
        return render(request, template, content)

@login_required
def comentar(request, pk):
    data = {}
    form = ComentForm(request.POST or None)
    pub_id = Publication.objects.filter(id=pk).values_list('id')[0][0]
    data['form'] = form
    data['username'] = request.user.pk
    data['pub_id'] = pub_id
    if form.is_valid():
        form.save()
        return redirect('url_feed')
    return render(request, 'publicacoes/comentario.html', data)

def comentarios(request, pk):
    data = {}
    coment = Correction.objects.filter(publications=pk)
    data['coment'] = coment
    data['username'] = request.user.pk

    return render(request, 'publicacoes/comentarios.html', data)

 



