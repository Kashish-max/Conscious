from django.shortcuts import render
from django.http import HttpResponse, Http404


def index(request):
    return render(request, 'consciousApp/index.html')

def ocr(request):
    return render(request, 'consciousApp/ocr.html')

def braille(request):
    print(request.POST) 
    data=request.POST.get('your_name')
    print(data)
    return render(request,'consciousApp/braille.html')

def triggers(request):
        return render(request, 'consciousApp/triggers.html')

def dyslexicsol(request):
    return render(request,'consciousApp/open-dyslexic.html')


