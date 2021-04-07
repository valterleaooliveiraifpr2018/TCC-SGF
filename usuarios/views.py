from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from .models import Perfil
from django.views.generic import TemplateView



# Create your views here.
class CadastroView(TemplateView):
    template_name = "usuarios/confirmacao.html"


class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    # Vai para a página com mensagem personalizada
    success_url = reverse_lazy('confirmacao-cadastro')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="funcionarios")

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        # Não vai ativar o usuário, o Admin vai aprovar o usuário
        self.object.is_active = False
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"

        return context


class PerfilUpdate(UpdateView):
    template_name = "cadastros/form.html"
    model = Perfil
    fields = ["nome_completo", "cpf", "telefone"]
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["titulo"] = "Meus dados pessoais"
        context["botao"] = "Atualizar"

        return context

  

# CRiar uma ListView de User que só o administrador pode acessar


class UsuarioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = User
    template_name = 'usuarios/List/gerenciar_aprovacao.html'
    


# Colocar só para o administrador fazer isso


class GerenciarUsuario(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    template_name = "usuarios/editar.html"
    model = User
    fields = ["is_active"]
    # Vai para a lista de usuários
    success_url = reverse_lazy("listar-usuarios")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["titulo"] = "Ativar ou desativar usuários"
        context["botao"] = "Salvar"

        return context
