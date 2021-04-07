from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, PerfilUpdate, GerenciarUsuario, UsuarioList, CadastroView
from django.urls import reverse_lazy

urlpatterns = [
    # path('', view, name=""),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name="login"),

    path('alterar-senha/', auth_views.PasswordChangeView.as_view(
            template_name='usuarios/editar.html',
            extra_context={
                'titulo': 'Alteração de senha',
                'botao': 'Atualizar'
                },
            success_url=reverse_lazy('index')
        ), name="alterar-senha"),

    path('confirmacao/', CadastroView.as_view(), name="confirmacao-cadastro"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
    path('atualizar-dados/', PerfilUpdate.as_view(), name='atualizar-dados'),
    path('gerenciar/<int:pk>/', GerenciarUsuario.as_view(), name='gerenciar-usuario'),
    path('listar/usuarios/', UsuarioList.as_view(), name="listar-usuarios"),
    
]
