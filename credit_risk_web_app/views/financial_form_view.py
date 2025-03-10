from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

from ..forms.financial_form import FinancialDataForm
from ..models.financial_data import FinancialData

def financial_form_view(request):
    
    if request.method == "POST":

        form = FinancialDataForm(request.POST)

        if form.is_valid():

            try:
            
                with transaction.atomic():

                    # Criando uma instância do modelo FinancialData com os dados do formulário
                    financial_data = FinancialData(

                        company=form.cleaned_data['company'],
                        year=form.cleaned_data['year'],
                        quarter=form.cleaned_data['quarter'],
                        monetary_type=form.cleaned_data['monetary_type'],
                        net_revenue=form.cleaned_data['net_revenue'],
                        cost_of_goods_sold=form.cleaned_data['cost_of_goods_sold'],
                        general_admin_expenses=form.cleaned_data['general_admin_expenses'],
                        research_development=form.cleaned_data['research_development'],
                        financial_income=form.cleaned_data['financial_income'],
                        financial_expenses=form.cleaned_data['financial_expenses'],
                        ebit=form.cleaned_data['ebit'],
                        ebitda=form.cleaned_data['ebitda'],
                        interest_expense=form.cleaned_data['interest_expense'],
                        corporate_income_tax=form.cleaned_data['corporate_income_tax'],
                        investment_income=form.cleaned_data['investment_income'],
                        dividends=form.cleaned_data['dividends'],

                        working_capital=form.cleaned_data['working_capital'],
                        inventory=form.cleaned_data['inventory'],
                        accounts_receivable=form.cleaned_data['accounts_receivable'],
                        accounts_payable=form.cleaned_data['accounts_payable'],
                        shareholders_equity=form.cleaned_data['shareholders_equity'],

                        new_loans=form.cleaned_data['new_loans'],
                        new_debentures=form.cleaned_data['new_debentures'],
                        other_financing=form.cleaned_data['other_financing'],
                        financial_leasing=form.cleaned_data['financial_leasing'],
                        short_term_loan_payment=form.cleaned_data['short_term_loan_payment'],
                        short_term_interest_payment=form.cleaned_data['short_term_interest_payment'],
                        long_term_loan_payment=form.cleaned_data['long_term_loan_payment'],
                        long_term_interest_payment=form.cleaned_data['long_term_interest_payment'],

                        gross_operating_cash_flow=form.cleaned_data['gross_operating_cash_flow'],
                        capex=form.cleaned_data['capex'],
                        investments=form.cleaned_data['investments'],
                        asset_sales=form.cleaned_data['asset_sales'],

                        share_price=form.cleaned_data['share_price'],
                        number_of_shares=form.cleaned_data['number_of_shares'],
                        shares_outstanding=form.cleaned_data['shares_outstanding'],
                    )
                    financial_data.save()  # Salvando no banco de dados

                    messages.success(request, 'Dados salvos com sucesso!')
                    return redirect('success-form')  # Redirecionando para a página de sucesso

            except IntegrityError:
           
                messages.error(request, 'Erro de integridade no banco de dados.')
            except ValidationError as e:
           
                messages.error(request, f'Erro de validação: {e}')
            except Exception as e:
           
                messages.error(request, f'Ocorreu um erro inesperado: {str(e)}')

            # Caso ocorra qualquer erro, redireciona para uma página de erro
            return redirect('error-form')

        else:
        
            messages.error(request, 'Por favor, corrija os erros abaixo.')
            return render(request, 'pages/financial_form.html', {'form': form})

    else:
    
        form = FinancialDataForm()  # Formulário será vazio para requisições GET

    return render(request, 'pages/financial_form.html', {'form': form})
