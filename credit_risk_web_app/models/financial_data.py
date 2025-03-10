# Importação do módulo models para criar os modelos com suas respectivas classes e funções
from django.db import models
from .company import Company



# Criação do Modelo para a Tabela Dado Financeiro
class FinancialData(models.Model):
    
    # Criação de Listas de Tuplas para restringir as opções dentro de campos específicos do formulário
    # Útil para gerar automaticamente campos drop-down (redução de erros e melhora na usabilidade)

    # O primeiro elemento é armazenado no Banco de Dados e o segundo é o valor legível que será exibido no Django admin ou interfaces do usuário
    QUARTERS = [
        ('1T', '1º Quarter (Trimestre)'),
        ('2T', '2º Quarter (Trimestre)'),
        ('3T', '3º Quarter (Trimestre)'),
        ('4T', '4º Quarter (Trimestre)'),
        ('AT', 'All Year Round (Ano Inteiro)'),
    ]

    MONETARY_TYPE = [
        ('K', 'THOUSANDS'),
        ('MM', 'MILLIONS'),
        ('B', 'BILLIONS'),
    ]

    # Criação dos campos do Modelo que serão transformados em campos da Tabela

    # on_delete define o comportamento dos dados financeiros quando a company é excluída (todos os dados financeiros associados são excluídos)    
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='financial_data')

    year = models.IntegerField()

    # Choices configurado com a lista QUARTES garante que o valor de quarter sempre será um daqueles pré-definidos e presentes na lista
    quarter = models.CharField(max_length=2, choices=QUARTERS)

    # Choices configurado com a lista QUANTITY garante que o valor de quantity sempre será um daqueles pré-definidos e presentes na lista
    monetary_type = models.CharField(max_length=2, choices=MONETARY_TYPE)

    # Demonstração do Resultado do Exercício (DRE)
    net_revenue = models.DecimalField(max_digits=15, decimal_places=2) # Receita Líquida
    cost_of_goods_sold = models.DecimalField(max_digits=15, decimal_places=2) # CGS = CVM ou CPV ou CSV (Custo da Mercadoria, Produto ou Serviço Vendida)
    general_admin_expenses = models.DecimalField(max_digits=15, decimal_places=2) # SGA = DAG (Despesas Administrativas Gerais)
    research_development = models.DecimalField(max_digits=15, decimal_places=2) # R&D = P&D (Pesquisa e Desenvolvimento)
    financial_income = models.DecimalField(max_digits=15, decimal_places=2) # Receitas Financeiras
    financial_expenses = models.DecimalField(max_digits=15, decimal_places=2) # Despesas Financeiras
    ebit = models.DecimalField(max_digits=15, decimal_places=2) # Lucro Operacional
    ebitda = models.DecimalField(max_digits=15, decimal_places=2) # Lucro Antes das Juros, Impostos, Depreciação e Amortização
    interest_expense = models.DecimalField(max_digits=15, decimal_places=2,  null=True) # Despesa com Juros
    corporate_income_tax = models.DecimalField(max_digits=15, decimal_places=2,  null=True) # Taxa do Imposto Corporativo
    investment_income = models.DecimalField(max_digits=15, decimal_places=2,  null=True) # Rendimento de Investimento
    dividends = models.DecimalField(max_digits=15, decimal_places=2,  null=True) # Dividendos
    
    # Balanço Patrimonial (BP)
    working_capital = models.DecimalField(max_digits=15, decimal_places=2) # Capital de Giro
    inventory = models.DecimalField(max_digits=15, decimal_places=2) # Inventário (Estoque)
    accounts_receivable = models.DecimalField(max_digits=15, decimal_places=2) # Recebíveis (À Receber)
    accounts_payable = models.DecimalField(max_digits=15, decimal_places=2) # Pagáveis (Contas a Pagar)
    new_loans = models.DecimalField(max_digits=15, decimal_places=2,  null=True) # Novos Empréstimos
    new_debentures = models.DecimalField(max_digits=15, decimal_places=2,  null=True) # Novas Debêntures
    other_financing = models.DecimalField(max_digits=15, decimal_places=2,  null=True) # Outros Financiamentos
    financial_leasing = models.DecimalField(max_digits=15, decimal_places=2,  null=True) # Arrendamento Financeiro 
    short_term_loan_payment = models.DecimalField(max_digits=15, decimal_places=2,  null=True) # Pagamento de Empréstimos de Curto Prazo
    short_term_interest_payment = models.DecimalField(max_digits=15, decimal_places=2,  null=True) # Pagamento de Juros de Empréstimos de Curto Prazo
    long_term_loan_payment = models.DecimalField(max_digits=15, decimal_places=2,  null=True) # Pagamento de Empréstimo de Longo Prazo
    long_term_interest_payment = models.DecimalField(max_digits=15, decimal_places=2,  null=True) # Pagamento de Juros de Empréstimos de Longo Prazo
    shareholders_equity = models.DecimalField(max_digits=15, decimal_places=2) # Patrimônio Líquido

    # Demonstração do Fluxo de Caixa (DFC)
    gross_operating_cash_flow = models.DecimalField(max_digits=15, decimal_places=2,  null=True) # Fluxo de Caixa Operacional Bruto
    capex = models.DecimalField(max_digits=15, decimal_places=2,  null=True) # CapEx
    investments = models.DecimalField(max_digits=15, decimal_places=2,  null=True) # Investimentos
    asset_sales = models.DecimalField(max_digits=15, decimal_places=2,  null=True) # Venda de Ativos
    
    # Outras Informações
    share_price = models.DecimalField(max_digits=9, decimal_places=2,  null=True) # Preço da Ação
    number_of_shares = models.IntegerField(null=True) # Número de Ações (Total)
    shares_outstanding = models.DecimalField(max_digits=15, decimal_places=2,  null=True) # Número de Ações em Circulação

    # Definição de como a instância do modelo será representada nas impressões e Django shell
    def __str__(self):
        return f"{self.company.commercial_name} - {self.year} - {self.quarter} - {self.monetary_type}"

    
    class Meta:
        db_table = 'financialdata'  # Explicitando o nome da tabela