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
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    countchar=request.GET.get('countchar','off')


    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose': 'Remove Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()

        params= {'purpose':'Changed to uppercase','analyzed_text':analyzed}
        return render(request,'analyze.html',params)    

    elif(newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char!='\n':
                analyzed+=char

        params= {'purpose':'Removed newlines','analyzed_text':analyzed}
        return render(request,'analyze.html',params)   

    elif(extraspaceremover=='on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" "and djtext[index+1]==" "):
                analyzed+=char

        params= {'purpose':'Removed extraspace','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif(countchar=='on'):
        count=0
        for char in djtext:
            count=count+1

        params= {'purpose':'Count total char','analyzed_text':count}
        return render(request,'analyze.html',params)   
                       

    else:
        return HttpResponse('Error')        