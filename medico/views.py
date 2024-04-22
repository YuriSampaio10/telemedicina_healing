from django.shortcuts import render
from .models import Especialidades

# Create your views here.


def cadastro_medico(request):
    if request.method == "GET":
        # acessa os dados da tablea Especialidades do banco de dados e devolve todos os dados para a variavel especialidade, fazendo assim que possamos usar esse dados no template
        especialidades = Especialidades.objects.all()
        return render(
            request, "cadastro_medico.html", {"especialidades": especialidades}
        )
