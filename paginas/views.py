from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = "paginas/index.html"

class IndexAdmView(TemplateView):
    template_name = "paginas/indexAdm.html"

class SobreView(TemplateView):
    template_name = "paginas/sobre.html"

class AjudaView(TemplateView):
    template_name = "paginas/ajuda.html"

class CardsView(TemplateView):
    template_name = "paginas/cards.html"