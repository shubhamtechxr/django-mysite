from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse('''<h1>TechXR</h1> <a href="https://www.techxr.co/">mysite</a>''')

# def about(request):
#     return HttpResponse("about shubham")    

def index(request):
    return render(request, 'index.html')
  

def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose': 'Remove Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse('Error')        