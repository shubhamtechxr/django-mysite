from django.http import HttpResponse

def index(request):
    return HttpResponse("hello shubham")

def about(request):
    return HttpResponse("about shubham")    