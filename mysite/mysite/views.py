from django.http import HttpResponse

# def index(request):
#     return HttpResponse('''<h1>TechXR</h1> <a href="https://www.techxr.co/">mysite</a>''')

# def about(request):
#     return HttpResponse("about shubham")    

def index(request):
    return HttpResponse("Home")

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("capitalize first")


def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("charcount ")