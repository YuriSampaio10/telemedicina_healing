from django.shortcuts import render, redirect
from django.http import HttpResponse

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
            print("erro, senhas diferentes")
            return redirect("/usuarios/cadastro")

        return HttpResponse(f"{username}- {email}- {senha}- {confirmar_senha}")
