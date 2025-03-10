# Indicadores de Fluxo de Caixa

# Fluxo de Caixa Livre
def calculate_free_cash_flow(gross_operating_cash_flow, capex, inventory, accounts_receivable, accounts_payable):
    # Calcular o fluxo de caixa operacional líquido usando o gross_operating_cash_flow
    net_operating_cash_flow = calculate_net_operating_cash_flow(gross_operating_cash_flow, inventory, accounts_receivable, accounts_payable)

    if net_operating_cash_flow is not None and capex is not None:
        return net_operating_cash_flow - capex
    return None

# Fluxo de Caixa Operacional Líquido
def calculate_net_operating_cash_flow(gross_operating_cash_flow, inventory, accounts_receivable, accounts_payable):

    # Calcular o fluxo de caixa operacional líquido com base nos dados disponíveis
    if gross_operating_cash_flow is not None and inventory is not None and accounts_receivable is not None and accounts_payable is not None:
        return gross_operating_cash_flow - (inventory + accounts_receivable - accounts_payable)
    return None

# Fluxo de Caixa antes de Nova Dívida
def calculate_free_cash_flow_before_debt(gross_operating_cash_flow, capex, inventory, accounts_receivable, accounts_payable, short_term_loan_payment, short_term_interest_payment):
    
    # Recalcular o fluxo de caixa operacional líquido
    net_operating_cash_flow = calculate_net_operating_cash_flow(gross_operating_cash_flow, inventory, accounts_receivable, accounts_payable)

    if net_operating_cash_flow is not None and capex is not None and short_term_loan_payment is not None and short_term_interest_payment is not None:
        free_cash_flow = net_operating_cash_flow - capex
        return free_cash_flow - short_term_interest_payment - short_term_loan_payment
    return None

# Fluxo de Caixa Livre Líquido 
# Não leva em Consideração a soma de Outras Fontes de Caixa no cálculo para estressar o modelo  
def calculate_net_free_cash_flow(gross_operating_cash_flow, capex, inventory, accounts_receivable, accounts_payable, new_loans, new_debentures, other_financing, financial_leasing, asset_sales, short_term_loan_payment, short_term_interest_payment):
    
    # Recalcular o fluxo de caixa operacional líquido
    net_operating_cash_flow = calculate_net_operating_cash_flow(gross_operating_cash_flow, inventory, accounts_receivable, accounts_payable)

    if net_operating_cash_flow is not None and asset_sales is not None and short_term_loan_payment is not None and short_term_interest_payment is not None:
        free_cash_flow = net_operating_cash_flow - capex
        return free_cash_flow + (new_loans + new_debentures + other_financing + financial_leasing) + asset_sales - short_term_loan_payment - short_term_interest_payment
    return None


