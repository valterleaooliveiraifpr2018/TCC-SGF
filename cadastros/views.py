from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Estado, EmailSuport 
from django.urls import reverse_lazy

# Create your views here.

class EstadoCreate(CreateView):
    model = Estado
    fields = ["nome","sigla"]
    template_name = "cadastros/form.html"
    # login_url = reverse_lazy("estado")


class EmailSuportCreate(CreateView):
    model = EmailSuport
    fields = ["nome","email", "telefoneFixo", "telefoneCelular", "descricao"]
    template_name = "cadastros/form.html"
    # login_url = reverse_lazy("estado")
    



