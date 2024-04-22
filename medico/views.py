from django.shortcuts import render
from .models import Especialidades, DadosMedico

# Create your views here.


def cadastro_medico(request):
    if request.method == "GET":
        # acessa os dados da tablea Especialidades do banco de dados e devolve todos os dados para a variavel especialidade, fazendo assim que possamos usar esse dados no template
        especialidades = Especialidades.objects.all()
        return render(
            request, "cadastro_medico.html", {"especialidades": especialidades}
        )
    elif request.method == "POST":
        # pega os dados do dicionario post do campo crm la do cadastro_medico.html
        crm = request.POST.get("crm")
        # pega os dados do dicionario post do campo nome la do cadastro_medico.html
        nome = request.POST.get("nome")
        # pega os dados do dicionario post do campo cep la do cadastro_medico.html
        cep = request.POST.get("cep")
        # pega os dados do dicionario post do campo rua la do cadastro_medico.html
        rua = request.POST.get("rua")
        # pega os dados do dicionario post do campo bairro la do cadastro_medico.html
        bairro = request.POST.get("bairro")
        # pega os dados do dicionario post do campo numero la do cadastro_medico.html
        numero = request.POST.get("numero")
        # pega os dados do dicionario post do campo cim la do cadastro_medico.html
        cim = request.FILES.get("cim")
        # pega os dados do dicionario post do campo rg la do cadastro_medico.html
        rg = request.FILES.get("rg")
        # pega os dados do dicionario post do campo foto la do cadastro_medico.html
        foto = request.FILES.get("foto")
        # pega os dados do dicionario post do campo especialidade la do cadastro_medico.html
        especialidade = request.POST.get("especialidade")
        # pega os dados do dicionario post do campo descricao la do cadastro_medico.html
        descricao = request.POST.get("descricao")
        # pega os dados do dicionario post do campo valor_consulta la do cadastro_medico.html
        valor_consulta = request.POST.get("valor_consulta")

        # pega esses dados do cadastro_medico da view que puxamos do cadastro_medico.html e adiciona eles aos campos que estão no DadosMedicos la do models.py do app medicos atraves desse impoert
        dados_medico = DadosMedico(
            crm=crm,
            nome=nome,
            cep=cep,
            rua=rua,
            bairro=bairro,
            numero=numero,
            cim=cim,
            rg=rg,
            foto=foto,
            especialidade_id=especialidade,
            descricao=descricao,
            valor_consulta=valor_consulta,
        )

        # salva tudo no banco de dados
        dados_medico.save()
