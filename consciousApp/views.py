from django.shortcuts import render
from django.http import HttpResponse, Http404


def index(request):
    return render(request, 'consciousApp/index.html')

def ocr(request):
    return render(request, 'consciousApp/ocr.html')

def braille(request):
    print(request.POST) 
    data=request.POST.get('text_data')
    print(data)
    text_file = open('data.txt', 'w') 
    text_file.write(data) 
    text_file.close() 
    text_file = open('data.txt', 'r') 
    print(text_file.read()) 
    text_file.close() 
    return render(request,'consciousApp/braille.html')

def triggers(request):
        if request.method=='POST':
            return render(request, 'consciousApp/triggers.html', {'text': request.POST['some_text']})
        else:
            return render(request, 'consciousApp/triggers.html')

def dyslexicsol(request):
    return render(request,'consciousApp/open-dyslexic.html')


