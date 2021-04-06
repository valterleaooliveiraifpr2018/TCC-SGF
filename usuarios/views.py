from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Perfil

# Create your views here.


class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login') # Vai para a página com mensagem personalizada

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

# Colocar só para o administrador fazer isso
class GerenciarUsuario(UpdateView):
    template_name = "usuarios/editar.html"
    model = User
    fields = ["is_active"]
    success_url = reverse_lazy("index") # Vai para a lista de usuários

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["titulo"] = "Ativar ou desativar usuários"
        context["botao"] = "Salvar"

        return context
