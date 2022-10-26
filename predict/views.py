import shutil

from django.shortcuts import render
from bs4 import BeautifulSoup
import os
import requests
# Create your views here.

def total(request):
    url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%86%8D%EC%82%B0%EB%AC%BC"

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    news_lis = soup.select('#main_pack > section > div > div.group_news > ul > li')
    all_list = []
    for li in news_lis:
        news_list = []
        title = li.find('a', class_='news_tit')['title']
        a_href = li.find('a', class_='news_tit')['href']
        news_list.append(title)
        news_list.append(a_href)
        all_list.append(news_list)
    ctx = {
        'list': all_list
    }
    return render(
        request,
        'predict/total.html',
        ctx
    )

