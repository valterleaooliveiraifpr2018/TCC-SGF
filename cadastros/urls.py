from django.urls import path
from .views import EstadoCreate, EmailSuportCreate
# from .views import NomeCreate
# from .views import NomeUpdate   
# from .views import NomeDelete
# from .views import NomeList
# from .views import IndexView, SobreView, AjudaView, IndexAdmView


urlpatterns = [

    ####################### Adicionar ###################################

    path('cadastrar/estados', EstadoCreate.as_view(), name='cadastrar-estado'),
    path('cadastrar/EmailSuport', EmailSuportCreate.as_view(),
         name='cadastrar-EmailSuport'),
    












]
