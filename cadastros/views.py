from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Estado, Fornecedor, Funcionario, Cidade, Maquina, Produto
from django.urls import reverse_lazy

# Create your views here.
############################CREATE###########################################
class FornecedorCreate(CreateView):
    model = Fornecedor
    fields = ["cnpj", "nomedocontribuinte", "nome",
              "email", "telefoneCelular", "telefoneFixo", "site"]
    template_name = "cadastros/form.html"
    
    # Tem que ter em todos inserir, alterar e excluir
    success_url = reverse_lazy("nome_da_url_no_urls.py")


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ["nome", "dataNascimento", "setor",
              "telefoneCelular", "telefoneFixo", "cpf", "rg", "email", "cnh", "cargo"]
    template_name = "cadastros/form.html"


class CidadeCreate(CreateView):
    model = Cidade
    fields = ["nome"]
    template_name = "cadastros/form.html"


class EstadoCreate(CreateView):
    model = Estado
    fields = ["nome","sigla"]
    template_name = "cadastros/form.html"


class MaquinaCreate(CreateView):
    model = Maquina
    fields = ["nome", "tipo", "ano", "horimetro", "prefixoMaquina"]
    template_name = "cadastros/form.html"


class ProdutoCreate(CreateView):
    model = Produto
    fields = ["nome", "qtdeatual", "qtdemin", "precoProduto"]
    template_name = "cadastros/form.html"

    

"""
class EmailSuportCreate(CreateView):
    model = EmailSuport
    fields = ["nome","email", "telefoneFixo", "telefoneCelular", "descricao"]
    template_name = "cadastros/form.html"
"""
