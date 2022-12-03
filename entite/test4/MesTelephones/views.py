from MesTelephones.models import Type
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from MesTelephones.models import Telephone
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import FormUser
from django.shortcuts import render
from .forms import FormConnexion
from django.contrib.auth import authenticate, login, logout

def index(request):
    prod = Telephone.objects.all().values()
    type=Type.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'prod': prod,
        'type':type
    }
    return HttpResponse(template.render(context, request))

def del_typ(request, id):
    produits = Telephone.objects.get(id=id)
    produits.delete()
    return HttpResponseRedirect(reverse('MesTelephones'))

def list_typ(request):
    typ = Type.objects.all().values()
    template = loader.get_template('type.html')
    context = {
    'typ':typ,
    }
    return HttpResponse(template.render(context, request))

def update_typ(request, id):
    art = Telephone.objects.get(id=id)
    cat = Type.objects.all().values()
    template = loader.get_template('update.html')
    context = {
    'art': art,
    'cat':cat, }
    return HttpResponse(template.render(context, request))

def update_typ_action(request, id):
    n = request.POST['nom']
    p = request.POST['prix']
    r = request.POST['realisateur']
    nty = request.POST['nomtype']
    typ = Type.objects.get(id=nty)
    article = Telephone.objects.get(id=id)
    article.nom = n
    article.prix = p
    article.realisateur = r
    article.type = typ
    article.save()
    return HttpResponseRedirect(reverse('MesTelephones'))

def add(request):
    cat = Type.objects.all().values()
    template = loader.get_template('add.html')
    context = {
    'cat': cat,
}
    return HttpResponse(template.render(context, request))

def add_tele(request):
    n=request.POST['nom']
    p =request.POST['prix']
    r =request.POST['realisateur']
    da =request.POST['datedecreation']
    typ =request.POST['nomtype']
    cat = Type.objects.get(id=typ)
    article = Telephone(nom=n, realisateur=r, prix=p, datedecreation=da,
    type=cat)
    article.save()
    return HttpResponseRedirect(reverse('MesTelephones'))

def list_users(request):
    users = User.objects.all().values()
    template = loader.get_template('users.html')
    context = {
    'users':users,
    }
    return HttpResponse(template.render(context, request))

def del_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('users'))

def create_compte(request):
    user_form = FormUser ()
    return render(request, 'createUser.html', {'user_form' :user_form})

def create_user_action(request):
    adrEmail = request.POST['email']
    username = request.POST['login']
    password = request.POST['mot2pass']
    confirm = request.POST['confirm']
    prenom = request.POST['prenom']
    nom = request.POST['nom']
    if (password==confirm):
        user = User.objects.create_user(username, adrEmail,password)
        user.first_name = prenom
        user.last_name = nom
        user.save()
        return HttpResponseRedirect(reverse('users'))
    else:
        print ("Mot de passe et confirmation mot de passe ne sont pas identiques")
        return HttpResponseRedirect(reverse('create_compte'))

def connect (request):
    connect_form = FormConnexion ()
    return render(request, 'connexion.html', {'connect_form' :connect_form})

def signIn(request):
    username = request.POST['login']
    password = request.POST['mot2pass']
    user = authenticate(request, username=username,password=password)
    if user is not None:
        login(request, user)
        request.session['username'] = username
        return HttpResponseRedirect(reverse('MesTelephones'))

    else:
        print("Login et/ou mot de passe incorrect")
        return render(request,'connexion.html')
        #return HttpResponseRedirect(reverse('connect'))
def signOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('connect'))


