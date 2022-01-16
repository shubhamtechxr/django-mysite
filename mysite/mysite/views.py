from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1>TechXR</h1> <a href="https://www.techxr.co/">mysite</a>''')

def about(request):
    return HttpResponse("about shubham")    