from .models import Post
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request,'home.html')


def sigup(request):

    if request.method == 'GET':

        return render(request,'sigup.html', {
            'form' : UserCreationForm
        } )   

    else: 
        if request.POST['password1'] == request.POST['password2']:

            try: 
                
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                
                login(request, user)
               
                return redirect('home')
                
            except:
                return render (request,'sigup.html', { 
                    'form' : UserCreationForm ,
                    "error": 'Usuário já existe'
                    
                    } ) 
           
        return render (request,'sigup.html', { 
                    'form' : UserCreationForm ,
                    "error": 'senhas são diferentes'
                    
                    } ) 

def sigin(request):

    if request.method == 'GET':
        return render(request,'sigin.html', {
        'form': AuthenticationForm
        })

    else:
        user = authenticate(

            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'sigin.html', {
                    'form' : AuthenticationForm,
                    'error': 'Usuário ou senha está incorreto'
                })

        else:
                login(request, user)
                return redirect('home')   
                
@login_required   
def sair(request):
    logout (request)
    return redirect('home')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class DetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'   