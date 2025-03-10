from .debt_expense_and_tax_indicators import calculate_total_debt


# Indicadores de Endividamento e Alavancagem

def calculate_debt_ebitda(short_term_loan_payment, long_term_loan_payment, ebitda):

    total_debt = calculate_total_debt(short_term_loan_payment, long_term_loan_payment)

    if total_debt is not None and ebitda is not None and ebitda != 0:
        return total_debt / ebitda
    return None

def calculate_debt_capital_struct(short_term_loan_payment, long_term_loan_payment, shareholders_equity):

    total_debt = calculate_total_debt(short_term_loan_payment, long_term_loan_payment)

    if total_debt is not None and total_debt != 0 and shareholders_equity is not None and shareholders_equity != 0:
        return total_debt / (total_debt + shareholders_equity)
    return None

def calculate_shareholders_equity_capital_struct(shareholders_equity, short_term_loan_payment, long_term_loan_payment):

    total_debt = calculate_total_debt(short_term_loan_payment, long_term_loan_payment)

    if total_debt is not None and total_debt != 0 and shareholders_equity is not None and shareholders_equity != 0:
        return shareholders_equity / (total_debt + shareholders_equity)
    return None
