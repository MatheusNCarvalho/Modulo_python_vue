# coding: utf-8
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from portfolios.views import PortfolioListView, PortfolioView, FuncionarioView, CargoListAndPost, CargoById

helper_patterns = [
    url(r'^portfolios/$', PortfolioListView.as_view()),
    url(r'^portfolios/(?P<pk>[0-9]+)/$', PortfolioView.as_view()),
    url(r'^funcionario/$', FuncionarioView.as_view()),

    url(r'^cargos/$', CargoListAndPost.as_view()),
    url(r'^cargos/(?P<pk>[0-9]+)/$', CargoById.as_view())




]

urlpatterns = format_suffix_patterns(helper_patterns)
