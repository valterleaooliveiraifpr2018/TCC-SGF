from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Fornecedor, Funcionario, Cidade, Maquina, Produto, Entrada, Saida, Produtos_Entrada, Produtos_Saida, Controle_Maquina
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
    success_url = reverse_lazy("listar-fornecedor")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Registrar um novo fornecedor"
        context["botao"] = "Cadastrar"
        context["url"] = "http://"
        return context


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ["nome", "data_nascimento", "setor",
              "telefone_celular", "telefone_fixo", "cpf", "rg", "email", "cnh", "cargo", "cidade"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Registrar um novo funcionario"
        context["botao"] = "Cadastrar"
        return context


class CidadeCreate(CreateView):
    model = Cidade
    fields = ["nome","estado"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cidade")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Registrar uma nova cidade"
        context["botao"] = "Cadastrar"
        return context



class MaquinaCreate(CreateView):
    model = Maquina
    fields = ["descricao", "ano", "horimetro", "prefixo", "cidade"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-maquina")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Registrar uma nova máquina"
        context["botao"] = "Cadastrar"
        return context

class ProdutoCreate(CreateView):
    model = Produto
    fields = ["nome", "quantidade_atual", "quantidade_minima"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-produto")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Registrar um novo produto"
        context["botao"] = "Cadastrar"
        return context


class EntradaCreate(CreateView):    
    model= Entrada
    fields = ["detalhes", "data", "fornecedor", "valor_total"]
    template_name ="cadastros/form.html"
    success_url = reverse_lazy("listar-entrada")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Registrar uma nova fornecedor"
        context["botao"] = "Cadastrar"
        return context

class Produtos_EntradaCreate(CreateView): 
    model = Produtos_Entrada
    fields = ["entrada", "produto", "quantidade", "preco_unitario"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-produtos_entrada")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Entrada de Produtos"
        context["botao"] = "Inserir nessa entrada"
        return context


class SaidaCreate(CreateView):    
    model= Saida
    fields = ["detalhes", "maquina", "funcionario"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-saida")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Registrar uma nova saida"
        context["botao"] = "Cadastrar"
        return context

class Produtos_SaidaCreate(CreateView):    
    model= Produtos_Saida
    fields= ["saida", "produto", "quantidade"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-saida")

    def form_valid(self, form):
        
        # Se a quantidade digitada no form for maior que a quanttidade atual do produto selecionado
        if(form.instance.quantidade > form.instance.produto.quantidade_atual):
            # Adicionar um erro no formulário/cadastro
            form.add_error(None, 'A quantidade desejada é maior do que a presente no estoque!')
            return self.form_invalid(form) 
                
        # Aqui que cria objeto e salva no banco
        url = super().form_valid(form)

        # Já que a quantidade está ok, vamos diminuir do estoque e salvar a alteração no banco também
        # Objeto que acabou de ser criado do tipo que está no Model ali em cima
        self.object.produto.quantidade_atual = self.object.produto.quantidade_atual - self.object.quantidade
        # Salvar o produto
        self.object.produto.save()

        # Fim do método
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Saída de Produtos"
        context["botao"] = "Registrar saída"
        return context

class Controle_MaquinaCreate(CreateView):    
    model= Controle_Maquina
    fields= ["maquina", "ultimo_horimetro"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-controle_maquina")

############################  UPDATE  ############################


class FornecedorUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Fornecedor
    fields = ["cnpj", "razao_social", "nome_fantasia",
              "vendedor", "email", "telefone", "site"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Atualizar o fornecedor"
        context["botao"] = "Atualizar"
        return context


class FuncionarioUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Funcionario
    fields = ["nome", "data_Nascimento", "setor",
              "telefone_Celular", "telefone_Fixo", "cpf", "rg", "email", "cnh", "cargo"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Atualizar o funcionário"
        context["botao"] = "Atualizar"
        return context

class CidadeUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Cidade
    fields = ["nome", "estado"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Atualizar a cidade"
        context["botao"] = "Atualizar"
        return context

class MaquinaUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Maquina
    fields = ["descricao", "ano", "horimetro", "prefixo", "cidade"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-maquina')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Atualizar a máquina"
        context["botao"] = "Atualizar"
        return context

class ProdutoUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Produto
    fields = ["nome", "quantidade_atual", "quantidade_minima"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Atualizar o produto"
        context["botao"] = "Atualizar"
        return context

class EntradaUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Entrada
    fields = ["detalhes", "data", "fornecedor", "valor_total"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-entrada')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Atualizar a entrada"
        context["botao"] = "Atualizar"
        return context

class Produtos_EntradaUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Produtos_Entrada
    fields = ["entrada", "produto", "quantidade", "preco_unitario"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos_entrada')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Entrada de Produtos"
        context["botao"] = "Atualizar entrada"
        return context


class SaidaUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Saida
    fields = ["detalhes", "maquina", "funcionario"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-saida')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Atualizar dados da Saída"
        context["botao"] = "Atualizar saída"
        return context
    
class Produtos_SaidaUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Produtos_Saida
    fields = ["saida", "produto", "quantidade"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-saida')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Saída de Produtos"
        context["botao"] = "Atualizar saída"
        return context

class Controle_MaquinaUpdate(UpdateView):
    # login_url = reverse_lazy('login')
    model = Controle_Maquina
    fields = ["maquina", "ultimo_horimetro"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-controle_maquina')
############################  DELETE  ############################


class FornecedorDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Fornecedor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-fornecedor')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Deletar o fornecedor"
        context["botao"] = "Excluir"
        return context

class FuncionarioDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Funcionario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-funcionario')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Deletar o funcionário"
        context["botao"] = "Excluir"
        return context

class CidadeDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Cidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Deletar a cidade"
        context["botao"] = "Excluir"
        return context

class MaquinaDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Maquina
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-maquina')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Deletar a máquina"
        context["botao"] = "Excluir"
        return context

class ProdutoDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Produto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Deletar o produto"
        context["botao"] = "Excluir"
        return context

class EntradaDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Entrada
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-entrada')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Deletar a entrada"
        context["botao"] = "Excluir"
        return context

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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Deletar a saida"
        context["botao"] = "Excluir"
        return context

class Produtos_SaidaDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Produtos_Saida
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-saida')

    def delete(self, *args, **kwargs):
        # Busca o objeto atual a ser excluído
        self.object = self.get_object()
        # Volta a quantidade atual do PRODUTO somando o que vai ser excluído
        self.object.produto.quantidade_atual = self.object.produto.quantidade_atual + self.object.quantidade
        # Salva o produto
        self.object.produto.save()
        # Exclui essa baixa registrada como saída
        return super().delete(*args, **kwargs)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Excluir Produto de uma Saída"
        context["botao"] = "Excluir"
        return context

class Controle_MaquinaDelete(DeleteView):
    # login_url = reverse_lazy('login')
    model = Controle_Maquina
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-controle_maquina')


############################  LISTA  ############################


class FornecedorList(ListView):
    # login_url = reverse_lazy('login')
    model = Fornecedor
    template_name = 'cadastros/listas/fornecedor.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Apresentar os fornecedores"
        return context
        

class FuncionarioList(ListView):
    # login_url = reverse_lazy('login')
    model = Funcionario
    template_name = 'cadastros/listas/funcionario.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Apresentar os funcionários"
        return context

class CidadeList(ListView):
    # login_url = reverse_lazy('login')
    model = Cidade
    template_name = 'cadastros/listas/Cidade.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Apresentar as cidades"
        return context

class EntradaList(ListView):
    # login_url = reverse_lazy('login')
    model = Entrada
    template_name = 'cadastros/listas/entrada.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Apresentar as entradas"
        return context

class MaquinaList(ListView):
    # login_url = reverse_lazy('login')
    model = Maquina
    template_name = 'cadastros/listas/maquina.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Apresentar as máquinas"
        return context

class Produtos_EntradaList(ListView):
    # login_url = reverse_lazy('login')
    model = Produtos_Entrada
    template_name = 'cadastros/listas/produtos_entrada.html'


class SaidaList(ListView):
    # login_url = reverse_lazy('login')
    model = Saida
    template_name = 'cadastros/listas/saida.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Apresentar as saidas"
        return context

class ProdutoList(ListView):
    # login_url = reverse_lazy('login')
    model = Produto
    template_name = 'cadastros/listas/produto.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Apresentar os produtos"
        return context


        
class Produtos_SaidaList(ListView):
    # login_url = reverse_lazy('login')
    model = Produtos_Saida
    template_name = 'cadastros/listas/produtos_saida.html'

class Controle_MaquinaList(ListView):
    # login_url = reverse_lazy('login')
    model = Controle_Maquina
    template_name = 'cadastros/listas/controle_maquina.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Apresentar os controle_maquina"
        return context


############################  DetailView  ############################


class FornecedorDetalhes(DetailView):
    model = Fornecedor
    template_name = 'cadastros/detalhes/fornecedor.html'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context["titulo"] = "Apresentação Detalhada do fornecedor"
        return context


class FuncionarioDetalhes(DetailView):
    model = Funcionario
    template_name = 'cadastros/detalhes/funcionario.html'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context["titulo"] = "Apresentação Detalhada do funcionário"
        return context
       

class SaidaDetalhes(DetailView):
    model = Saida
    template_name = 'cadastros/detalhes/saida.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Enviando uma lista de Produtos_Saide conforme o objeto de Saída que está neste detailview
        context['produtos'] = Produtos_Saida.objects.filter(saida=self.object)

        return context
