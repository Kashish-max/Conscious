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
            text = request.POST['some_text']
            triggers = ["9 11", "9-11", "9/11", "ableism", "abusive", "ageism", "alcoholism", "animal abuse", "animal death", "animal violence", "bestiality", "gore", "corpse", "bully", "cannibal", "car accident", "child abuse", "childbirth", "classism", "death", "decapitation", "abuse", "drug", "heroin", "cocaine", "eating disorder", "anorexia", "binge eating", "bulimia", "fatphobia", "forced captivity", "holocaust", "hitler", "homophobia", "hostage", "incest", "kidnap", "murder", "nazi", "overdose", "pedophilia", "prostitution", "PTSD", "racism", "racist", "rape", "raping", "scarification", "self-harm", "self harm", "cutting", "sexism", "slavery", "slurs", "suicide", "suicidal", "swearing", "terminal illness", "terrorism", "torture", "transphobia", "violence", "warfare"]
            tw = []
            for trigger in triggers:
                if text.find(trigger) > -1: tw.append(trigger)
            if tw == []: tw.append('No Triggers Found')
            return render(request, 'consciousApp/triggers.html', {'text': text, 'triggers': tw})
        else:
            return render(request, 'consciousApp/triggers.html')

def dyslexicsol(request):
    return render(request,'consciousApp/open-dyslexic.html')


