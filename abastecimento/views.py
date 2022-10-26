from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Veiculo
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):    
    return render(request, 'index.html')

def veiculos(request):    
    veiculos = Veiculo.objects.order_by('-data_criacao').filter(ativo=True)

    dados = {
        'veiculos': veiculos
    }
    if request.user.is_authenticated: 
        return render(request, 'veiculos.html', dados)
    else: 
        return redirect('index')

def veiculo(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, pk=veiculo_id)

    veiculo_a_exibir = {
        'veiculo' : veiculo
    }

    return render(request, 'receita.html', veiculo_a_exibir)

def buscar(request):
    lista_veiculos = Veiculo.objects.order_by('-data_criacao').filter(ativo=True)

    if 'buscar' in request.GET:
        placa_a_buscar = request.GET['buscar']
        if buscar:
            lista_veiculos = lista_veiculos.filter(placa__icontains=placa_a_buscar)

    dados = {
        'veiculos': lista_veiculos
    }

    return render(request, 'buscar.html', dados)

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        matricula = request.POST['matricula']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']

        if not nome.strip():
            
            return redirect('cadastro')
        if not email.strip():
            return redirect('cadastro')
        if senha != senha2:
            return redirect('cadastro')
        if User.objects.filter(username=matricula).exists():
            return redirect('cadastro')
        user = User.objects.create_user(username=matricula, first_name = nome, email = email, password=senha)
        user.save()
        print('usuario cadastrado com sucesso')
        return redirect('index')
    else:
        return render(request, 'cadastro.html')

def login(request):  
    if request.method == 'POST':
        matricula = request.POST['matricula']
        senha = request.POST['senha']
        if matricula == '' or senha == '':
            return redirect('index')
        print(matricula, senha)
        user = auth.authenticate(request, username=matricula, password=senha)
        if user is not None:
            auth.login(request, user)
            print('login realizado com sucesso')
            return redirect('veiculos')
    return render(request,'index.html' )

def logout(request):
    auth.logout(request)
    return redirect('index')

