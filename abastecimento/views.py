from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Abastecimento, Veiculo, Manutencao
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

def abastecimentos(request):    
    abastecimentos = Abastecimento.objects.order_by('-data_abastecimento')
    veiculos = Veiculo.objects.filter(id=abastecimentos.placa_id)

    dados = {
        'abastecimentos': abastecimentos,
        'veiculos': veiculos
    }
    if request.user.is_authenticated: 
        return render(request, 'abastecimentos.html', dados)
    else: 
        return redirect('index')

def abastecimento(request, abastecimento_id):
    abastecimento = get_object_or_404(Abastecimento, pk=abastecimento_id)

    abastecimento_a_exibir = {
        'abastecimento' : abastecimento
    }

    return render(request, 'receita.html', abastecimento_a_exibir)

def manutencoes(request):    
    manutencoes = Manutencao.objects.order_by('-data')

    dados = {
        'manutencoes': manutencoes
    }
    if request.user.is_authenticated: 
        return render(request, 'manutencao.html', dados)
    else: 
        return redirect('index')

def manutencao(request, manutencao_id):
    manutencao = get_object_or_404(Manutencao, pk=manutencao_id)

    manutencao_a_exibir = {
        'manutencao' : manutencao
    }

    return render(request, 'receita.html', manutencao_a_exibir)

def adiciona_abastecimento(request):
    veiculos = Veiculo.objects.order_by('-data_criacao').filter(ativo=True)

    dados = {
        'veiculos': veiculos
    }
    if request.method == 'POST':
        km = request.POST['km']
        litros = request.POST['litros']
        valor = request.POST['valor']
        posto = request.POST['posto']        
        motorista = request.POST['motorista']  
        combustivel= request.POST['combustivel']
        placa= request.POST['placa']
        data_abastecimento = request.POST['data_abastecimento']
        veiculo = get_object_or_404(Veiculo, placa=placa)
        user = get_object_or_404(User, pk=request.user.id)        
        abastecimento = Abastecimento.objects.create(usuario_de_criacao= user, km=km, litros=litros, valor=valor, posto=posto, motorista=motorista, combustivel=combustivel, placa_id=veiculo.id, data_abastecimento=data_abastecimento)     
        abastecimento.save()        
        return redirect('abastecimento')
    else :
        return render(request, 'abastecimento.html', dados)

def busca_abastecimentos(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, pk=veiculo_id)
    abastecimentos = Abastecimento.objects.order_by('-data_abastecimento').filter(placa_id=veiculo.id)

    dados = {
        'abastecimentos': abastecimentos
    }
    if request.user.is_authenticated: 
        return render(request, 'abastecimentos.html', dados)
    else: 
        return redirect('index')




def adiciona_manutencao(request):
    veiculos = Veiculo.objects.order_by('-data_criacao').filter(ativo=True)

    dados = {
        'veiculos': veiculos
    }
    # if request.method == 'POST':
    #     km = request.POST['km']
    #     litros = request.POST['litros']
    #     valor = request.POST['valor']
    #     posto = request.POST['posto']        
    #     motorista = request.POST['motorista']  
    #     combustivel= request.POST['combustivel']
    #     placa= request.POST['placa']
    #     veiculo = get_object_or_404(Veiculo, placa=placa)
    #     user = get_object_or_404(User, pk=request.user.id)        
    #     # abastecimento = Abastecimento.objects.create(usuario_de_criacao= user, km=km, litros=litros, valor=valor, posto=posto, motorista=motorista, combustivel=combustivel, placa_id=veiculo.id)     
    #     # abastecimento.save()
    #     return redirect('manutencao')
    # else :
    #     return redirect('manutencao')
    return render(request, 'manutencao.html')

# def busca_manutencao(request, veiculo_id):
#     veiculo = get_object_or_404(Veiculo, pk=veiculo_id)
#     manutencao = Manutencao.objects.order_by('-data_abastecimento').filter(placa_id=veiculo.id)

#     dados = {
#         'manutencoes': manutencoes
#     }
#     if request.user.is_authenticated: 
#         return render(request, 'manutencoes.html', dados)
#     else: 
#         return redirect('index')





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

