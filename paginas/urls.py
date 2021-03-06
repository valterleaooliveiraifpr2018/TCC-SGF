from django.urls import path
from .views import IndexView, SobreView, AjudaView, IndexAdmView, CardsView


urlpatterns = [

    path('', IndexView.as_view(), name= "index"),
    path('Admin/', IndexAdmView.as_view(), name= "indexAdm"),
    path('sobre/',SobreView.as_view(), name= "sobre"),
    path('ajuda/',AjudaView.as_view(), name= "ajuda"),
    path('cards/',CardsView.as_view(), name= "cards"),
]
