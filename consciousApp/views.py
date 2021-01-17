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
    # print(request.POST) 
    # #data=request.POST.get('text_data')
    # data=dict(request.POST)
    # text_data=data['text_data']
    # text_file = open('./consciousApp/static/consciousApp/input/data.txt', 'w+') 
    # text_file.write(str(text_data[0])) 
    # text_file.close() 
    # os.system("./consciousApp/static/consciousApp/file2brl/file2brl ./consciousApp/static/consciousApp/input/data.txt ./consciousApp/static/consciousApp/output/data.brf")
    val = 'I am reading Braille'
    if request.method=='POST':
        val = request.POST['some_text']
    print(type(val))
    return render(request,'consciousApp/braille.html', {'val': val})

def triggers(request):
        if request.method=='POST':
            text = request.POST['some_text'].lower()
            triggers = ["9 11", "9-11", "9/11", "ableism", "abusive", "ageism", "alcoholism", "animal abuse", "animal death", "animal violence", "bestiality", "gore", "corpse", "bully", "cannibal", "car accident", "child abuse", "childbirth", "classism", "death", "decapitation", "abuse", "drug", "heroin", "cocaine", "eating disorder", "anorexia", "binge eating", "bulimia", "fatphobia", "forced captivity", "holocaust", "hitler", "homophobia", "hostage", "incest", "kidnap", "murder", "nazi", "overdose", "pedophilia", "prostitution", "PTSD", "racism", "racist", "rape", "raping", "scarification", "self-harm", "self harm", "cutting", "sexism", "slavery", "slurs", "suicide", "suicidal", "swearing", "terminal illness", "terrorism", "torture", "transphobia", "violence", "warfare"]
            tw = []
            text_file = open('./consciousApp/static/consciousApp/input/triggercheckdata.txt', 'w+') 
            text_file.write(str(text)) 
            text_file.close() 
            for trigger in triggers:
                if text.find(trigger) > -1: tw.append(trigger)
            if tw == []: tw.append('No Triggers Found')
            return render(request, 'consciousApp/triggers.html', {'text': text, 'triggers': tw})
        else:
            return render(request, 'consciousApp/triggers.html')

def dyslexicsol(request):
    return render(request,'consciousApp/open-dyslexic.html')

def urldata(request):
    print(request.POST)
    link=request.POST['Link'][0]
    print(link)
    url = 'https://www.bbc.com/culture/article/20210111-the-ancient-roots-of-wonder-woman'
    article = Article(url)
    article.download()
    article.parse()
    print("Article Authors: ",article.authors)
    print("Article Publish Date: ",article.publish_date)
    #print("Article Text: ", article.text)
    data=article.text
    tokens = word_tokenize(data)
    text = nltk.Text(tokens)
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white").generate(str(text))
    wordcloud.to_file("./consciousApp/static/consciousApp/output/word-cloud-url.png")
    #print(article.top_image)
    #print(article.movies)
    article.nlp()
    print("Article Keywords:",article.keywords)
    print("Article Summary: ",article.summary)
    return render(request, 'consciousApp/triggers.html')
