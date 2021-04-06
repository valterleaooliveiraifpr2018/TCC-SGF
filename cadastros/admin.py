from django.contrib import admin
from .models import Cidade, Entrada, Fornecedor, Funcionario, Maquina, Produto, Produtos_Saida, Produtos_Entrada, Revisao, Saida
# Register your models here.

admin.site.register(Produtos_Entrada)
admin.site.register(Produtos_Saida)
admin.site.register(Cidade)
admin.site.register(Entrada)
admin.site.register(Fornecedor)
admin.site.register(Funcionario)
admin.site.register(Maquina)
admin.site.register(Produto)
admin.site.register(Saida)
admin.site.register(Revisao)