from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Especialidades(models.Model):
    especialidade = models.CharField(max_length=50)

    # Pesquisar
    def __str__(self):
        return self.especialidade


class DadosMedico(models.Model):
    crm = models.CharField(max_length=30)
    nome = models.CharField(max_length=100)
    cep = models.CharField(max_length=15)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField()
    # o rg, cim e foto de perfil sao imagens que o campo vai receber, upload_to vai para a pasta /media/ que a gente ja configurou no settings.py no core do projeto e em cada pasta tera uma outra pasta com nome diferente
    rg = models.ImageField(upload_to="rgs")
    cedula_identidade_medica = models.ImageField(upload_to="cim")
    foto = models.ImageField(upload_to="fotos_perfil")
    # pega da chave estrangeira para a relação do usuario do banco de dados que esta no auth.user com dados medicos
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    descricao = models.TextField(null=True, blank=True)
    especialidade = models.ForeignKey(
        Especialidades, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    valor_consulta = models.FloatField(default=100)

    # Pesquisar
    def __str__(self):
        return self.user.username
