from django.shortcuts import render
from django.http import HttpResponse, Http404
import os
from os import path

import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from newspaper import Article
import nltk
nltk.download('punkt') 
import re, pprint
from nltk import word_tokenize
from hatesonar import Sonar

def checkKey(dict, key): 
      
    if key in dict.keys(): 
        return True
        print("Present, ", end =" ") 
        print("value =", dict[key]) 
    else: 
        return False
        print("Not present") 
  
 

def home(request):
    return render(request, 'consciousApp/home.html')

def ocr(request):
    return render(request, 'consciousApp/ocr.html')

def texttobrf(request):
    print(request.POST) 
    #data=request.POST.get('text_data')
    data=dict(request.POST)
    text_data=data['text_data']
    text_file = open('./consciousApp/static/consciousApp/input/data.txt', 'w+') 
    text_file.write(str(text_data[0])) 
    text_file.close() 
    os.system("./consciousApp/static/consciousApp/file2brl/file2brl ./consciousApp/static/consciousApp/input/data.txt ./consciousApp/static/consciousApp/output/data.brf")
    return render(request,'consciousApp/braille.html')

def braille(request):
   val = 'I am reading Braille'
   if request.method=='POST':
        val = request.POST['some_text']
   return render(request,'consciousApp/braille.html', {'val': val})

def triggers(request):
        if request.method=='POST':
            print(request.POST)
            data=dict(request.POST)
            # Driver Code  
            key = 'show_details'
            one=checkKey(data, key);
            key = 'check_triggers'
            two=checkKey(data, key)
            key = 'show_wordcloud'
            three=checkKey(data, key)
            key = 'hate_speech'
            four=checkKey(data, key)
            print(one,two,three)
            #URL Link case
            if(one==True):
                url=data['Link'][0]
                print(url)
                article = Article(url)
                article.download()
                article.parse()
                authors=article.authors
                publishdate=article.publish_date
                #article.text
                article.nlp()
                keywords=article.keywords
                articlesummary=article.summary
                return render(request, 'consciousApp/triggers.html', {'authors':authors , 'publishdate': publishdate,'keywords':keywords,'articlesummary':articlesummary})
            #Show triggers
            elif(two==True):
                text = request.POST['input_text'].lower()
                triggers = ["9 11", "9-11", "9/11", "ableism", "abusive", "ageism", "alcoholism", "animal abuse", "animal death", "animal violence", "bestiality", "gore", "corpse", "bully", "cannibal", "car accident", "child abuse", "childbirth", "classism", "death", "decapitation", "abuse", "drug", "heroin", "cocaine", "eating disorder", "anorexia", "binge eating", "bulimia", "fatphobia", "forced captivity", "holocaust", "hitler", "homophobia", "hostage", "incest", "kidnap", "murder", "nazi", "overdose", "pedophilia", "prostitution", "PTSD", "racism", "racist", "rape", "raping", "scarification", "self-harm", "self harm", "cutting", "sexism", "slavery", "slurs", "suicide", "suicidal", "swearing", "terminal illness", "terrorism", "torture", "transphobia", "violence", "warfare"]
                tw = []
                text_file = open('./consciousApp/static/consciousApp/input/triggercheckdata.txt', 'w+') 
                text_file.write(str(text)) 
                text_file.close() 
                for trigger in triggers:
                    if text.find(trigger) > -1: tw.append(trigger)
                if tw == []: tw.append('No Triggers Found')
                return render(request, 'consciousApp/triggers.html', {'text': text, 'triggers': tw,'data':data})
            #Show_cloud           
            elif(three==True):
                text = request.POST['input_text'].lower()
                tokens = word_tokenize(text)
                textdata = nltk.Text(tokens)
                stopwords = set(STOPWORDS)
                wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white").generate(text)
                wordcloud.to_file("./consciousApp/static/consciousApp/output/word-cloud.png")
                data="./../../static/consciousApp/output/word-cloud.png"
                return render(request, 'consciousApp/triggers.html', {'data': data} )    

            elif(four==True):
                sonar = Sonar();
                text = request.POST['input_text'].lower();
                url=data['Link'][0];
                data=sonar.ping(text=text)["classes"]; 
                hate_speech=data[0];
                hate_speech_confidence=hate_speech["confidence"]*100;
                offensive_language=data[1];
                offensive_language_confidence=offensive_language["confidence"]*100;
                neither=data[2]; 
                neither_confidence=neither["confidence"]*100;  
                print(type(data))
                print(offensive_language_confidence*100,hate_speech_confidence*100,neither_confidence*100)
                return render(request, 'consciousApp/triggers.html',{'hate_speech_confidence':hate_speech_confidence,'offensive_language_confidence':offensive_language_confidence,'neither_confidence':neither_confidence})    
        else:
            
            return render(request, 'consciousApp/triggers.html')

def dyslexicsol(request):
    val = 'Hello! Convert your text into dyslexic readable form.'
    if request.method == 'POST':
        val = request.POST['some_text']
    return render(request,'consciousApp/open-dyslexic.html', {'val':val})
