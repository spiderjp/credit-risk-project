# Indicadores de Eficiẽncia no Uso de Capital e Liquidez

def calculate_working_capital_net_revenue(working_capital, net_revenue):

    if net_revenue is not None and net_revenue != 0 and working_capital is not None:
        return working_capital / net_revenue
    return None

def calculate_working_investment_net_revenue(inventory, accounts_receivable, accounts_payable, net_revenue):
    
    # Calcular o working capital (invólucro de estoque, contas a receber e a pagar)
    working_capital = inventory + accounts_receivable - accounts_payable
    
    # Chama a função com o working capital calculado e o net_revenue
    working_investment = calculate_working_capital_net_revenue(working_capital, net_revenue)  

    if working_investment is not None and net_revenue is not None and net_revenue != 0:
        return working_investment
    return None


def calculate_working_investment(inventory, accounts_receivable, accounts_payable):

    if inventory is not None and accounts_receivable is not None and accounts_payable is not None:
        return (inventory + accounts_receivable - accounts_payable)
    return None  

#def calculate_other_asset_changes(cgs, net_revenue):