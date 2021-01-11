from django.urls import path
from .views import index, output

urlpatterns = [
    path('', index, name='index'),
    path('output/', output, name='output')
]
