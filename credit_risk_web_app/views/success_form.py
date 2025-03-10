from django.shortcuts import render

def success_page_view(request):
    return render(request, 'pages/success_form.html')
