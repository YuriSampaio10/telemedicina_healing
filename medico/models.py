from django.db import models

# Create your models here.


class Especialidades(models.Model):
    especialidade = models.CharField(max_length=50)

    # Pesquisar
    def __str__(self):
        return self.especialidade


class DadosMedico(models.Model):
    CRM = models.CharField(max_length=30)
    nome = models.CharField(max_length=100)
    cep = models.CharField(max_length=15)
    rua = models.CharField(max_length=15)
    bairro = models.CharField(max_length=15)
    numero = models.IntegerField()
    rg = models.ImageField(upload_to="rgs")
    cedulas_identidade_medica= models.ImageField(upload_to="cim")
    foto = models.ImageField(upload_to="fotos_perfil")
    descricao = models.TextField()
    valor_consulta = models.FloatField(default=100)
