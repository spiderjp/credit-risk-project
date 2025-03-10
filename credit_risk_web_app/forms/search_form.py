from django import forms
from ..models.company import Company

class SearchCompanyForm(forms.Form):
    
    company = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        label="Escolha a Companhia",
        empty_label="Selecione uma empresa"
    )
