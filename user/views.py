from django.shortcuts import render, redirect
from django.views.generic import View, CreateView

from django.contrib.auth import logout, login
from django.contrib.auth import authenticate

from .forms import CreateUserForm

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render (request, 'home.html', context)


class CreateUserView(CreateView):
    def get(self, request, *args, **kwargs):
        form = CreateUserForm()
        context = {
            'form': form
        }
        return render(request, 'user/create_user.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = CreateUserForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('user:home')
        else:
            form = CreateUserForm()
        return render(request, 'user/create_user.html', {'form': form})
    

class LoginUserView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render (request, 'user/login_user.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(username, password)
            print(user)
            if user is not None:
                login(request, user) 
                return redirect('user:home')
            else:
                context = {'error': 'Usuario o contraseña incorrecta'}
        else:
            context = {'error': 'Método no permitido'}

        return render(request, 'user/login_user.html', context)

def logout_view(request):
    logout(request)
    return redirect('user:home')