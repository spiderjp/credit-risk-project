# Indicadores de Margem e Lucratividade

def calculate_cost_of_goods_sold_net_revenue(cost_of_goods_sold, net_revenue):

    if net_revenue is not None and net_revenue != 0 and cost_of_goods_sold is not None:
        return cost_of_goods_sold / net_revenue
    return None

def calculate_general_admin_expenses_net_revenue(general_admin_expenses, net_revenue):

    if net_revenue is not None and net_revenue != 0 and general_admin_expenses is not None:
        return general_admin_expenses / net_revenue
    return None

def calculate_research_development_net_revenue(research_development, net_revenue): 

    if net_revenue is not None and net_revenue != 0 and research_development is not None:
        return research_development / net_revenue
    return None

def calculate_ebit_net_revenue(ebit, net_revenue):

    if net_revenue is not None and net_revenue != 0 and ebit is not None:
        return ebit / net_revenue
    return None

def calculate_ebitda_net_revenue(ebitda, net_revenue):

    if net_revenue is not None and net_revenue != 0 and ebitda is not None:
        return ebitda / net_revenue
    return None



