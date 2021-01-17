from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('braille',views.braille ,name='braille'),
    path('ocr', views.ocr, name='ocr'),
    path('triggers', views.triggers, name='triggers'),
    path('open-dyslexic',views.dyslexicsol,name='opendyslexic'),
    path('texttobrf',views.texttobrf,name='ttb')
]
