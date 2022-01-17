from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse('''<h1>TechXR</h1> <a href="https://www.techxr.co/">mysite</a>''')

# def about(request):
#     return HttpResponse("about shubham")    

def index(request):
    return render(request, 'index.html')
  

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    countchar=request.POST.get('countchar','off')


    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose': 'Remove Punctuations','analyzed_text':analyzed}
        djtext=analyzed

    if fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()

        params= {'purpose':'Changed to uppercase','analyzed_text':analyzed}
        djtext=analyzed   

    if newlineremover=='on':
        analyzed=""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed+=char

        params= {'purpose':'Removed newlines','analyzed_text':analyzed}
        djtext=analyzed  

    if extraspaceremover=='on':
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" "and djtext[index+1]==" "):
                analyzed+=char

        params= {'purpose':'Removed extraspace','analyzed_text':analyzed}
        
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")  

    return render(request,'analyze.html',params)   
                       
       