from django.shortcuts import render
from ..forms.report_form import SearchCompanyForm

def report(request):
    
    form = SearchCompanyForm(request.GET or None)
    
    company = None
    
    if request.GET and form.is_valid():
        company = form.cleaned_data.get('company')

    context = {
        'form': form,
        'company': company,
    }
    
    return render(request, 'pages/report.html', context)