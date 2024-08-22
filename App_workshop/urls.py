from django.urls import path
from .views import PessoaFormViews
urlpatterns = [
    path('pessoa/', PessoaFormViews.as_view(), name='pessoa' )
]