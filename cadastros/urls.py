from django.urls import path
from .views import EstadoCreate, CidadeCreate, FornecedorCreate, FuncionarioCreate, MaquinaCreate, ProdutoCreate, EntradaCreate, Produtos_EntradaCreate, SaidaCreate, Produtos_SaidaCreate
from .views import EstadoUpdate, CidadeUpdate, FornecedorUpdate, FuncionarioUpdate, MaquinaUpdate, ProdutoUpdate, EntradaUpdate, Produtos_EntradaUpdate, SaidaUpdate, Produtos_SaidaUpdate   
from .views import EstadoDelete, CidadeDelete, FornecedorDelete, FuncionarioDelete, MaquinaDelete, ProdutoDelete, EntradaDelete, Produtos_EntradaDelete, SaidaDelete, Produtos_SaidaDelete
from .views import EstadoList  , CidadeList  , FornecedorList  , FuncionarioList  , MaquinaList  , ProdutoList  , EntradaList  , Produtos_EntradaList  , SaidaList  , Produtos_SaidaList

# from .views import IndexView, SobreView, AjudaView, IndexAdmView


urlpatterns = [

    ############################  CREATE  ############################


    path('cadastrar/fornecedor', FornecedorCreate.as_view(), name='cadastrar-fornecedor'),
    path('cadastrar/funcionario', FuncionarioCreate.as_view(), name='cadastrar-funcionario'),
    path('cadastrar/cidade', CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('cadastrar/estados', EstadoCreate.as_view(), name='cadastrar-estado'),
    path('cadastrar/maquina', MaquinaCreate.as_view(), name='cadastrar-maquina'),
    path('cadastrar/produto', ProdutoCreate.as_view(), name='cadastrar-produto'),
    # path('cadastrar/cargo', CargoCreate.as_view(), name='cadastrar-cargo'),
    path('cadastrar/entrada', EntradaCreate.as_view(), name='cadastrar-entrada'),
    path('cadastrar/produtos_entrada', Produtos_EntradaCreate.as_view(), name='cadastrar-produtos_entrada'),
    path('cadastrar/saida', SaidaCreate.as_view(), name='cadastrar-saida'),
    path('cadastrar/produtos_saida', Produtos_SaidaCreate.as_view(), name='cadastrar-produtos_saida'),
    ############################  UPDATE  ############################
    

    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name="editar-estado"),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name="editar-cidade"),
    path('editar/fornecedor/<int:pk>/', FornecedorUpdate.as_view(), name="editar-fornecedor"),
    path('editar/funcionario/<int:pk>/', FuncionarioUpdate.as_view(), name="editar-funcionario"),
    path('editar/maquina/<int:pk>/', MaquinaUpdate.as_view(), name="editar-maquina"),
    path('editar/produto/<int:pk>/', ProdutoUpdate.as_view(), name="editar-produto"),
    # path('editar/cargo/<int:pk>/', CargoUpdate.as_view(), name="editar-cargo"),
    path('editar/entrada/<int:pk>/', EntradaUpdate.as_view(), name="editar-entrada"),
    path('editar/produtos_entrada/<int:pk>/', Produtos_EntradaUpdate.as_view(), name="editar-produtos_entrada"),
    path('editar/saida/<int:pk>/', SaidaUpdate.as_view(), name="editar-saida"),
    path('editar/produtos_saida/<int:pk>/', Produtos_SaidaUpdate.as_view(), name="editar-produtos_saida"),
    ############################  DELETE  ############################
        

    path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name="excluir-estado"),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name="excluir-cidade"),
    path('excluir/fornecedor/<int:pk>/', FornecedorDelete.as_view(), name="excluir-fornecedor"),
    path('excluir/funcionario/<int:pk>/', FuncionarioDelete.as_view(), name="excluir-funcionario"),
    path('excluir/maquina/<int:pk>/', MaquinaDelete.as_view(), name="excluir-maquina"),
    path('excluir/produto/<int:pk>/', ProdutoDelete.as_view(), name="excluir-produto"),
    # path('excluir/cargo/<int:pk>/', CargoDelete.as_view(), name="excluir-cargo"),
    path('excluir/entrada/<int:pk>/', EntradaDelete.as_view(), name="excluir-entrada"),
    path('excluir/produtos_entrada/<int:pk>/', Produtos_EntradaDelete.as_view(), name="excluir-produtos_entrada"),
    path('excluir/saida/<int:pk>/', SaidaDelete.as_view(), name="excluir-saida"),
    path('excluir/produtos_saida/<int:pk>/', Produtos_SaidaDelete.as_view(), name="excluir-produtos_saida"),
    ############################  LIST  ############################
    

    path('listar/fornecedor', FornecedorList.as_view(), name="listar-fornecedor"),
    path('listar/funcionario', FuncionarioList.as_view(), name="listar-funcionario"),
    path('listar/cidade', CidadeList.as_view(), name="listar-cidade"),
    path('listar/estado', EstadoList.as_view(), name="listar-estado"),
    path('listar/entrada', EntradaList.as_view(), name="listar-entrada"),
    path('listar/maquina',MaquinaList.as_view(), name="listar-maquina"),
    path('listar/produto', ProdutoList.as_view(), name="listar-produto"),
    path('listar/produtos_entrada', Produtos_EntradaList.as_view(), name="listar-produtos_entrada"),
    path('listar/saida', SaidaList.as_view(), name="listar-saida"),
    path('listar/produtos_saida', Produtos_SaidaList.as_view(), name="listar-produtos_saida"),
   
    
    


]
