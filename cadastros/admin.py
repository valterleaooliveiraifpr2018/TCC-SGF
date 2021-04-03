from django.contrib import admin
from .models import Produtos_Saida, Produtos_Entrada, Revisao
# Register your models here.

admin.site.register(Produtos_Entrada)
admin.site.register(Produtos_Saida)
admin.site.register(Revisao)