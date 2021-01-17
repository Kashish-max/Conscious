from django.shortcuts import render
from django.http import HttpResponse, Http404
import os

def index(request):
    return render(request, 'consciousApp/index.html')

def ocr(request):
    return render(request, 'consciousApp/ocr.html')

def braille(request):
    print(request.POST) 
    #data=request.POST.get('text_data')
    data=dict(request.POST)
    text_data=data['text_data']
    text_file = open('./consciousApp/static/consciousApp/input/data.txt', 'w+') 
    text_file.write(str(text_data[0])) 
    text_file.close() 
    os.system("./consciousApp/static/consciousApp/file2brl/file2brl ./consciousApp/static/consciousApp/input/data.txt ./consciousApp/static/consciousApp/output/data.brf")
    return render(request,'consciousApp/braille.html')

def triggers(request):
        if request.method=='POST':
            return render(request, 'consciousApp/triggers.html', {'text': request.POST['some_text']})
        else:
            return render(request, 'consciousApp/triggers.html')

def dyslexicsol(request):
    return render(request,'consciousApp/open-dyslexic.html')


