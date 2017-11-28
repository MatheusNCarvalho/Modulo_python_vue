# coding: utf-8
from django.conf.urls import url
from portfolios.views import PortfolioListView, PortfolioView, FuncionarioView

helper_patterns = [
    url(r'^portfolios/$', PortfolioListView.as_view(), name='portfolios'),
    url(r'^portfolios/(?P<pk>[0-9]+)/$', PortfolioView.as_view(), name='get_portfolio'),
    url(r'^funcionario/$', FuncionarioView.as_view(), name='get_funcionario')


]

urlpatterns = helper_patterns
