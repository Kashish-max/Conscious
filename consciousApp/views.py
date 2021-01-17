from django.shortcuts import render
from django.http import HttpResponse, Http404
import os

def home(request):
    return render(request, 'consciousApp/home.html')

def ocr(request):
    return render(request, 'consciousApp/ocr.html')

def braille(request):
    # print(request.POST) 
    # #data=request.POST.get('text_data')
    # data=dict(request.POST)
    # text_data=data['text_data']
    # text_file = open('./consciousApp/static/consciousApp/input/data.txt', 'w+') 
    # text_file.write(str(text_data[0])) 
    # text_file.close() 
    # os.system("./consciousApp/static/consciousApp/file2brl/file2brl ./consciousApp/static/consciousApp/input/data.txt ./consciousApp/static/consciousApp/output/data.brf")
    return render(request,'consciousApp/braille.html')


def triggers(request):
        if request.method=='POST':
            text = request.POST['some_text'].lower()
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


