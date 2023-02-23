from django.http import HttpResponse

def home_view(request):
    name = 'jorge'
    HTML = f'<h1>Hello {name}!</h1>'
    return HttpResponse(HTML)