from django.shortcuts import render

def error_page_view(request):
    return render(request, 'pages/error_form.html')
