from django.urls import path
from doce.views import *

urlpatterns = [
    path('', index),
    path('novo-doce/', doce1),
    path('leite-com-goiaba/', doce2 ),
    path('ainda-tem-doce/', doce3),
    path('membro/', doce4),
]