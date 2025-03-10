# Criação do Formulário para registrar os valores contábeis e financeiros de qualquer companhia

# Importando o Formulário do Django e os Dados Financeiros do Modelo FinancialData
from django import forms
from ..models.company import Company
from ..models.financial_data import FinancialData

# Criando o formulário
class FinancialDataForm(forms.ModelForm):

    company = forms.ModelChoiceField(
    
        queryset=Company.objects.all(),
        label="Empresa",
        empty_label="Selecione uma empresa"
    
    )

    class Meta:
    
        model = FinancialData
        fields = '__all__'  # Isso inclui todos os campos do modelo automaticamente
        labels = {
            "company": "Empresa",
            "year": "Ano",
            "quarter": "Trimestre",
            "monetary_type": "Tipo de Valor Monetário",
            "net_revenue": "Receita Líquida",
            "cost_of_goods_sold": "Custo da Mercadoria/Produto/Serviço Vendido (CMV)",
            "general_admin_expenses": "Despesas Administrativas Gerais (SGA)",
            "research_development": "Pesquisa e Desenvolvimento (P&D)",
            "financial_income": "Receitas Financeiras",
            "financial_expenses": "Despesas Financeiras",
            "ebit": "Lucro Operacional (EBIT)",
            "ebitda":" Lucro antes dos Juros, Impostos, Depreciação e Amortização (EBITDA)",
            "interest_expense":"Despesas com Juros",
            "corporate_income_tax":"Valor do Imposto Corporativo",
            "investment_income":"Rendimento de Investimentos",
            "dividends":"Dividendos",
            
            "working_capital":"Capital de Giro",
            "inventory":"Inventário (Estoque)",
            "accounts_receivable":" Contas a Receber",
            "accounts_payable":"Contas a Pagar",
            "new_loans":"Novos Empréstimos",
            "new_debentures":"Novas Debêntures",
            "other_financing":"Outros Financiamentos",
            "financial_leasing":"Arrendamento Financeiro",
            "short_term_loan_payment":"Pagamento dos Empréstimos de Curto Prazo (CP)",
            "short_term_interest_payment":"Pagamento de Juros dos Empréstimos de Curto Prazo (CP)",
            "long_term_loan_payment":"Pagamento dos Empréstimos de Longo Prazo (LP)",
            "long_term_interest_payment":"Pagamento de Juros dos Empréstimos de Longo Prazo (LP)",
            "shareholders_equity":"Patrimônio Líquido",
            
            "gross_operating_cash_flow":"Fluxo de Caixa Operacional Bruto (FCO)",
            "capex":"CapEx",
            "investments":"Investimentos",
            "asset_sales":"Venda de Ativos",
            
            "share_price":"Preço da Ação (opcional)",
            "number_of_shares":"Número de Ações (opcional)",
            "shares_outstanding":"Número de Ações em Circulação (opcional)",
        }
    





#    company = forms.ModelChoiceField(
#        queryset=Company.objects.all(),
#        label="Compania",
#        empty_label="Selecione uma empresa",
#        # Se necessário, defina um método para customizar o rótulo:
#        # widget=forms.Select(),
#    )
#
#    YEARS = [(year, year) for year in range(2020, 2101)]
#    year = forms.ChoiceField(
#        choices=YEARS,
#        label="Ano"
#    )
#
#    QUARTERS = [
#        ('1T', '1º Quarter (Trimestre)'),
#        ('2T', '2º Quarter (Trimestre)'),
#        ('3T', '3º Quarter (Trimestre)'),
#        ('4T', '4º Quarter (Trimestre)'),
#        ('AT', 'All Year Round (Ano Inteiro)'),
#    ]
#    quarter = forms.ChoiceField(
#        choices=QUARTERS,
#        label="Trimestre"
#    )
#
#    MONETARY_TYPE = [
#        ('K', 'THOUSANDS'),
#        ('MM', 'MILLIONS'),
#        ('B', 'BILLIONS'),
#    ]
#    monetary_type = forms.ChoiceField(
#        choices=MONETARY_TYPE,
#        label="Valor Monetário"
#    )
#
#
#    # Demonstração do Resultado do Exercício (DRE)
#    revenues = forms.DecimalField(label="Receita Líquida", max_digits=15, decimal_places=2)
#    cgs = forms.DecimalField(label="Custo da Mercadoria/Produto/Serviço Vendida", max_digits=15, decimal_places=2)
#    sga = forms.DecimalField(label="Despesas Administrativas Gerais", max_digits=15, decimal_places=2)
#    rd = forms.DecimalField(label="Pesquisa e Desenvolvimento", max_digits=15, decimal_places=2)
#    financial_income = forms.DecimalField(label="Receitas Financeiras", max_digits=15, decimal_places=2)
#    financial_expenses = forms.DecimalField(label="Despesas Financeiras", max_digits=15, decimal_places=2)
#    ebit = forms.DecimalField(label="Lucro Operacional", max_digits=15, decimal_places=2)
#    ebitda = forms.DecimalField(label="Lucro Antes de Juros, Impostos, Depreciação e Amortização", max_digits=15, decimal_places=2)
#    interest_expense = forms.DecimalField(label="Despesa com Juros", max_digits=15, decimal_places=2)
#    corporate_income_tax = forms.DecimalField(label="Taxa do Imposto Corporativo", max_digits=15, decimal_places=2)
#    investment_income = forms.DecimalField(label="Rendimento de Investimento", max_digits=15, decimal_places=2)
#    dividends = forms.DecimalField(label="Dividendos", max_digits=15, decimal_places=2)
#
#    # Balanço Patrimonial (BP)
#    working_capital = forms.DecimalField(label="Capital de Giro", max_digits=15, decimal_places=2)
#    inventory = forms.DecimalField(label="Inventário (Estoque)", max_digits=15, decimal_places=2)
#    receivables = forms.DecimalField(label="Recebíveis (À Receber)", max_digits=15, decimal_places=2)
#    payables = forms.DecimalField(label="Pagáveis (Contas a Pagar)", max_digits=15, decimal_places=2)
#    new_loans = forms.DecimalField(label="Novos Empréstimos", max_digits=15, decimal_places=2)
#    new_debentures = forms.DecimalField(label="Novas Debêntures", max_digits=15, decimal_places=2)
#    other_financing = forms.DecimalField(label="Outros Financiamentos", max_digits=15, decimal_places=2)
#    financial_leasing = forms.DecimalField(label="Arrendamento Financeiro", max_digits=15, decimal_places=2)
#    short_term_loan_payment = forms.DecimalField(label="Pagamento de Empréstimos de Curto Prazo", max_digits=15, decimal_places=2)
#    short_term_interest_payment = forms.DecimalField(label="Pagamento de Juros de Empréstimos de Curto Prazo", max_digits=15, decimal_places=2)
#    long_term_loan_payment = forms.DecimalField(label="Pagamento de Empréstimo de Longo Prazo", max_digits=15, decimal_places=2)
#    long_term_interest_payment = forms.DecimalField(label="Pagamento de Juros de Empréstimos de Longo Prazo", max_digits=15, decimal_places=2)
#    equity = forms.DecimalField(label="Patrimônio Líquido", max_digits=15, decimal_places=2)
#
#    share_price = forms.DecimalField(label="Preço da Ação", max_digits=9, decimal_places=2)
#    number_of_shares = forms.IntegerField(label="Número de Ações (Total)")
#    shares_outstanding = forms.DecimalField(label="Número de Ações em Circulação", max_digits=15, decimal_places=2)
#
#    # Demonstração do Fluxo de Caixa (DFC)
#    gross_operating_cash_flow = forms.DecimalField(label="Fluxo de Caixa Operacional Bruto", max_digits=15, decimal_places=2)
#    capex = forms.DecimalField(label="CapEx", max_digits=15, decimal_places=2)
#    investments = forms.DecimalField(label="Investimentos", max_digits=15, decimal_places=2)
#    asset_sales = forms.DecimalField(label="Venda de Ativos", max_digits=15, decimal_places=2)