from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

# Create your views here.


def cadastro(request):
    print(request.method)
    if request.method == "GET":
        return render(request, "cadastro.html")
    elif request.method == "POST":
        # pega os dados do dicionario post do campo username la do cadastro.html
        username = request.POST.get("username")
        # pega os dados do dicionario post do campo email la do cadastro.html
        email = request.POST.get("email")
        # pega os dados do dicionario post do campo senha la do cadastro.html
        senha = request.POST.get("senha")
        # pega os dados do dicionario post do campo confirmar_senha la do cadastro.html
        confirmar_senha = request.POST.get("confirmar_senha")

        # confirmar se a senha e a confirmar_senha são iguais
        if senha != confirmar_senha:
            messages.add_message(
                request, constants.ERROR, "A senha e o Confirmar senha devem ser iguais"
            )
            return redirect("/usuarios/cadastro")

        # verifica se o endereço de email possui um @
        if "@" not in email:
            messages.add_message(
                request, constants.ERROR, "O endereço de e-mail deve conter '@'."
            )
            return redirect("/usuarios/cadastro")

        # verifica se a senha tem menos de 6 digitos
        if len(senha) < 6:
            messages.add_message(
                request, constants.ERROR, "A senha deve ter mais de 6 digitos"
            )
            return redirect("/usuarios/cadastro")

        # verifica e filtra se o campo username ja existe no banco de dados, caso exista, redireiona navamente para cadastro.html
        users = User.objects.filter(username=username)
        if users.exists():
            messages.add_message(
                request, constants.ERROR, "Ja existe um usuario com esse nome"
            )
            return redirect("/usuarios/cadastro")

        # pega os dados username, email e senha digitados no cadastro.html e coloca na tabela criada pelo django
        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha,
        )


def login_view(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        # pega os dados do dicionario post do campo username la do cadastro.html
        username = request.POST.get("username")
        # pega os dados do dicionario post do campo senha la do cadastro.html
        senha = request.POST.get("senha")

        # verifica no banco de dados se as credenciais username e senha existem nele, se exister ele retorna uma instancia do usuario para a variavel user, caso não, vai retornar none
        user = auth.authenticate(request, username=username, password=senha)

        # pega o usuario e atrela a reuisição login e redireciona a home dos pacientes
        if user:
            auth.login(request, user)
            return redirect("pacientes/home")
        messages.add_message(request, constants.ERROR, "Usuario ou Senha inválidos")
        return redirect("/usuarios/login")
