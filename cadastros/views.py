from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Estado, Fornecedor, Funcionario, Cidade, Maquina, Produto, Entrada, Saida, Produtos_Entrada, Produtos_Saida
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404


# Create your views here.
############################  CREATE  ############################
class FornecedorCreate(CreateView):
    model = Fornecedor
    fields = ["cnpj", "razao_social", "nome_fantasia",
              "vendedor","email", "telefone", "site", "cidade"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("cadastrar-fornecedor")


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ["nome", "data_nascimento", "setor",
              "telefone_celular", "telefone_fixo", "cpf", "rg", "email", "cnh", "cargo", "cidade"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("cadastrar-funcionario")


class CidadeCreate(CreateView):
    model = Cidade
    fields = ["nome","estado"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("cadastrar-cidade")


class EstadoCreate(CreateView):
    model = Estado
    fields = ["nome","sigla"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("cadastrar-estado")


class MaquinaCreate(CreateView):
    model = Maquina
    fields = ["descricao", "ano", "horimetro", "prefixo", "cidade"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("cadastrar-maquina")


class ProdutoCreate(CreateView):
    model = Produto
    fields = ["nome", "quantidade_atual", "quantidade_minima"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("cadastrar-produto")


# class CargoCreate(CreateView):
#     model = Cargo
#     fields = ["nome"]
#     template_name = "cadastros/form.html"
#     success_url = reverse_lazy("cadastrar-cargo")


class EntradaCreate(CreateView):    
    model= Entrada
    fields = ["detalhes", "data", "fornecedor", "valor_total"]
    template_name ="cadastros/form.html"
    success_url = reverse_lazy("cadastrar-entrada")


class Produtos_EntradaCreate(CreateView): 
    model = Produtos_Entrada
    fields = ["entrada", "produto", "quantidade", "preco_unitario"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("cadastrar-produtos_entrada")


class SaidaCreate(CreateView):    
    model= Saida
    fields = ["detalhes", "maquina", "funcionario"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("cadastrar-saida")


class Produtos_SaidaCreate(CreateView):    
    model= Produtos_Saida
    fields= ["saida", "produto", "quantidade"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("cadastrar-produtos_saida")


"""
class EmailSuportCreate(CreateView):
    model = EmailSuport
    fields = ["nome","email", "telefoneFixo", "telefoneCelular", "descricao"]
    template_name = "cadastros/form.html"
"""
############################  UPDATE  ############################


class FornecedorUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Fornecedor
    fields = ["cnpj", "razao_social", "nome_fantasia",
              "vendedor", "email", "telefone", "site"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')


class FuncionarioUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Funcionario
    fields = ["nome", "data_Nascimento", "setor",
              "telefone_Celular", "telefone_Fixo", "cpf", "rg", "email", "cnh", "cargo"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')


class CidadeUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Cidade
    fields = ["nome", "estado"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')


class EstadoUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Estado
    fields = ["nome", "sigla"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')


class MaquinaUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Maquina
    fields = ["descricao", "ano", "horimetro", "prefixo", "cidade"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-maquina')


class ProdutoUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Produto
    fields = ["nome", "quantidade_atual", "quantidade_minima"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')


# class CargoUpdate(UpdateView):
#     # login_url = reverse_lazy('login')
#     model = Cargo
#     fields = ["nome"]
#     template_name = 'cadastros/form.html'
#     success_url = reverse_lazy('listar-cargo')


class EntradaUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Entrada
    fields = ["detalhes", "data", "fornecedor", "valor_total"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-entrada')


class Produtos_EntradaUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Produtos_Entrada
    fields = ["entrada", "produto", "quantidade", "preco_unitario"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos_entrada')


class SaidaUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Saida
    fields = ["detalhes", "maquina", "funcionario"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-Saida')

    
class Produtos_SaidaUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Produtos_Saida
    fields = ["saida", "produto", "quantidade"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos_saida')
############################  DELETE  ############################


class FornecedorDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Fornecedor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-fornecedor')


class FuncionarioDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Funcionario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-funcionario')


class CidadeDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Cidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidade')


class EstadoDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Estado
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-estado')


class MaquinaDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Maquina
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-maquina')


class ProdutoDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Produto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produto')


# class CargoDelete(DeleteView):
#     # login_url = reverse_lazy('login')
#     model = Cargo
#     template_name = 'cadastros/form-excluir.html'
#     success_url = reverse_lazy('listar-cargo')

    
class EntradaDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Entrada
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-entrada')


class Produtos_EntradaDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Produtos_Entrada
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produtos_entrada')


class SaidaDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Saida
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-saida')


class Produtos_SaidaDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Produtos_Saida
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produtos_saida')


############################  LISTA  ############################


class FornecedorList(ListView):
    # login_url = reverse_lazy('login')
    model = Fornecedor
    template_name = 'cadastros/listas/fornecedor.html'


class FuncionarioList(ListView):
    # login_url = reverse_lazy('login')
    model = Funcionario
    template_name = 'cadastros/listas/funcionario.html'


class CidadeList(ListView):
    # login_url = reverse_lazy('login')
    model = Cidade
    template_name = 'cadastros/listas/Cidade.html'


class EstadoList(ListView):
    # login_url = reverse_lazy('login')
    model = Estado
    template_name = 'cadastros/listas/estado.html'


class EntradaList(ListView):
    # login_url = reverse_lazy('login')
    model = Entrada
    template_name = 'cadastros/listas/entrada.html'


class MaquinaList(ListView):
    # login_url = reverse_lazy('login')
    model = Maquina
    template_name = 'cadastros/listas/maquina.html'


class Produtos_EntradaList(ListView):
    # login_url = reverse_lazy('login')
    model = Produtos_Entrada
    template_name = 'cadastros/listas/produtos_entrada.html'


class SaidaList(ListView):
    # login_url = reverse_lazy('login')
    model = Saida
    template_name = 'cadastros/listas/saida.html'


class ProdutoList(ListView):
    # login_url = reverse_lazy('login')
    model = Produto
    template_name = 'cadastros/listas/produto.html'

class Produtos_SaidaList(ListView):
    # login_url = reverse_lazy('login')
    model = Produtos_Saida
    template_name = 'cadastros/listas/produtos_saida.html'


############################  DetailView  ############################
class FornecedorDetalhes(DetailView):
    model = Fornecedor
    template_name = 'cadastros/detalhes/fornecedor.html'


class SaidaDetalhes(DetailView):
    model = Saida
    template_name = 'cadastros/detalhes/saida.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Enviando uma lista de Produtos_Saide conforme o objeto de Saída que está neste detailview
        context['produtos'] = Produtos_Saida.objects.filter(saida=self.object)

        return context
