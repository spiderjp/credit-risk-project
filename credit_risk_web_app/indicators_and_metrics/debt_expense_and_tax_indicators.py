# Função para calcular a Dívida Total
def calculate_total_debt(short_term_loan_payment, long_term_loan_payment):

    if short_term_loan_payment is not None and short_term_loan_payment != 0 and long_term_loan_payment is not None and long_term_loan_payment != 0:
        return short_term_loan_payment + long_term_loan_payment
    return None



# Função para calcular a Despesa Financeira Líquida
def calculate_net_financial_expense(financial_expenses, financial_income):

    if financial_expenses is not None and financial_income is not None:
        return financial_expenses - financial_income
    return None



# Função para calcular a Taxa Efetiva de Imposto
def calculate_effective_corporate_tax_rate (ebit, corporate_income_tax):

    if ebit is not None and ebit != 0 and corporate_income_tax is not None:
        return corporate_income_tax / ebit
    return None

