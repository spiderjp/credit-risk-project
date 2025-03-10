# Importação de todas as funções para calcular métricas e indicadores financeiros de uma empresa
from .capital_efficiency_and_liquidity_indicators import (
    calculate_working_capital_net_revenue,
    calculate_working_investment_net_revenue,
    calculate_working_investment
)

from .cash_flow_indicators import (
    calculate_free_cash_flow,
    calculate_net_operating_cash_flow,
    calculate_free_cash_flow_before_debt,
    calculate_net_free_cash_flow
)

from .debt_and_leverage_indicators import (
    calculate_debt_ebitda,
    calculate_debt_capital_struct,
    calculate_shareholders_equity_capital_struct
)

from .debt_expense_and_tax_indicators import (
    calculate_total_debt,
    calculate_net_financial_expense,
    calculate_effective_corporate_tax_rate

)

from .margin_and_profitability_indicators  import (
    calculate_cost_of_goods_sold_net_revenue,
    calculate_general_admin_expenses_net_revenue,
    calculate_research_development_net_revenue,
    calculate_ebit_net_revenue,
    calculate_ebitda_net_revenue
)


# Função que chama todas as outras e organiza os dados para retornar
def calculate_indicators(financial_data):
    
    results = {}

    for data in financial_data:

        results[data.year] = {}

        try:
        
            # capital_efficiency_and_liquidity_indicators.py
            results[data.year]["Receitas de Capital de Giro"] = calculate_working_capital_net_revenue(data.working_capital, data.net_revenue) or 'N/A'
            results[data.year]["Receitas de Investimento de Capital de Giro"] = calculate_working_investment_net_revenue(data.inventory, data.accounts_receivable, data.accounts_payable, data.net_revenue) or 'N/A'
            results[data.year]["Investimento de Capital de Giro"] = calculate_working_investment(data.inventory, data.accounts_receivable, data.accounts_payable) or 'N/A'


            # cash_flow_indicators.py  
            results[data.year]["Fluxo de Caixa Livre"] = calculate_free_cash_flow(data.gross_operating_cash_flow, data.capex, data.inventory, data.accounts_receivable, data.accounts_payable) or 'N/A'
            results[data.year]["Fluxo de Caixa Operacional Líquido"] = calculate_net_operating_cash_flow(data.gross_operating_cash_flow, data.inventory, data.accounts_receivable, data.accounts_payable) or 'N/A'
            results[data.year]["Fluxo de Caixa Livre Antes da Dívida"] = calculate_free_cash_flow_before_debt(data.gross_operating_cash_flow, data.capex, data.inventory, data.accounts_receivable, data.accounts_payable, data.short_term_loan_payment, data.short_term_interest_payment) or 'N/A'
            results[data.year]["Fluxo de Caixa Livre Líquido"] = calculate_net_free_cash_flow(data.gross_operating_cash_flow, data.capex, data.inventory, data.accounts_receivable, data.accounts_payable, data.new_loans, data.new_debentures, data.other_financing, data.financial_leasing, data.asset_sales, data.short_term_loan_payment, data.short_term_interest_payment) or 'N/A'


            # debt_and_leverage_indicators.py
            results[data.year]["Dívida/EBITDA"] = calculate_debt_ebitda(data.short_term_loan_payment, data.long_term_loan_payment, data.ebitda) or 'N/A'
            results[data.year]["Dívida/Capital Estrutural"] = calculate_debt_capital_struct(data.short_term_loan_payment, data.long_term_loan_payment, data.shareholders_equity) or 'N/A'
            results[data.year]["Equidade/Capital Estrutural"] = calculate_shareholders_equity_capital_struct(data.shareholders_equity, data.short_term_loan_payment, data.long_term_loan_payment) or 'N/A'


            # debt_expense_and_tax_indicators.py
            results[data.year]["Dívida Total"] = calculate_total_debt(data.short_term_loan_payment, data.long_term_loan_payment) or 'N/A'
            results[data.year]["Despesas Financeiras Líquidas"] = calculate_net_financial_expense(data.financial_expenses, data.financial_income) or 'N/A'
            results[data.year]["Imposto Corporativo Efetivo"] = calculate_effective_corporate_tax_rate(data.ebit, data.corporate_income_tax) or 'N/A'


            # margin_and_profitability_indicators.py
            results[data.year]["CMV/Receitas"] = calculate_cost_of_goods_sold_net_revenue(data.cost_of_goods_sold, data.net_revenue) or 'N/A'
            results[data.year]["SGA/Receitas"] = calculate_general_admin_expenses_net_revenue(data.general_admin_expenses, data.net_revenue) or 'N/A'
            results[data.year]["P&D/Receitas"] = calculate_research_development_net_revenue(data.research_development, data.net_revenue) or 'N/A'
            results[data.year]["EBIT/Receitas"] = calculate_ebit_net_revenue(data.ebit, data.net_revenue) or 'N/A'
            results[data.year]["EBTIDA/Receitas"] = calculate_ebitda_net_revenue(data.ebitda, data.net_revenue) or 'N/A'
            
        except Exception as e:
            # Em caso de erro durante o cálculo, registramos o erro
            results[data.year] = {'error': f"Erro ao calcular indicadores: {str(e)}"}
        

    return results
