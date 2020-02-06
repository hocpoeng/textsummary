# Wikipedia scraper
from django.shortcuts import render

import bs4 as bs  
import urllib.request  
import re
import nltk
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from summa import summarizer
from summa import keywords

def viewSumma(request):
  url_topull = request.GET.get('url', 'https://en.wikipedia.org/wiki/Machine_learning')

  scraped_data = urllib.request.urlopen(url_topull)  
  article = scraped_data.read()

  parsed_article = bs.BeautifulSoup(article,'lxml')

  paragraphs = parsed_article.find_all('p')

  article_text = ""

  for p in paragraphs:  
      article_text += p.text

  summary = summarizer.summarize(article_text,ratio=0.05)

  print("Data pull done")

  print("==================================SUMMARY===================================")
  print (summary)

  print("==================================KEYWORDS===================================")
  print (keywords.keywords(article_text,ratio=0.5))

  context = {
      'title': 'Summa',
      'summary': [summary],
  }
  return render(request, 'home.html', context)