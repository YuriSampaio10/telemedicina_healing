from django.contrib import admin
from .models import Especialidades, DadosMedico


# registra no site, na area administrative a model especialidade
admin.site.register(Especialidades)
admin.site.register(DadosMedico)
