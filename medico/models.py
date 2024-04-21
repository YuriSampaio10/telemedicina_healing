from django.db import models

# Create your models here.


class Especialidades(models.Model):
    especialidade = models.CharField(max_length=50)

    # Pesquisar
    def __str__(self):
        return self.especialidade
