from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='summary-home'),
    path('nltk/', views.nltk_summarizer, name='summary-nltk'),
    path('stemmer/', views.porterStemmer, name='summary-stemmer'),
    path('summa/', views.viewSumma, name='summary-summa'),
]
