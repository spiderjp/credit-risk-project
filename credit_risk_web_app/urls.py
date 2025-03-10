from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect

# GET
from .views.home_view import home
from .views.financial_form_view import financial_form_view
#from .views.search_view import search
from .views.report_view import report

# POST
from .views.success_form import success_page_view
from .views.error_form import error_page_view

# AJAX
#from .views.ajax.search_company_ajax import search_company_ajax
from .views.indicators_and_metrics_view import get_company_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('financial-form/', financial_form_view, name='financial_form'),
    #path('search-company/', search, name='company'),
    path('generate-report/', report, name='report'),

    path('success-form/', success_page_view, name='success-form'),
    path('error-form/', error_page_view, name='error-form'),

    # AJAX + JSON (Requisições assíncronas)
    #path('ajax/pesquisar/', search_company_ajax, name='search_company_ajax'),
    path('get_company_data/', get_company_data, name='get_company_data'),
]
