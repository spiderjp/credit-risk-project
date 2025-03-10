from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from ..models.company import Company
from ..models.financial_data import FinancialData
from ..indicators_and_metrics import calculator

def get_company_data(request):
    company_id = request.GET.get('company_id')

    if not company_id:
        return JsonResponse({'error': 'Nenhuma empresa selecionada. Escolha uma empresa para exibir seus dados!'}, status=400)

    company = get_object_or_404(Company, id=company_id)
    financial_data = FinancialData.objects.filter(company=company)

    if not financial_data.exists():
        return JsonResponse({'error': 'Essa empresa não possui dados financeiros disponíveis.'}, status=404)

    # Chamando a função que calcula todos os indicadores e métricas financeiras
    try:
        results = calculator.calculate_indicators(financial_data)
        
    except Exception as e:
        return JsonResponse({'error': f'Erro ao calcular os indicadores: {str(e)}'}, status=500)

    return JsonResponse({'success': True, 'data': results})
