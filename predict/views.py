import shutil

from django.shortcuts import render
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pandas as pd
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

    today = datetime.now() - timedelta(2)
    today = today.year * 10000 + today.month * 100 + today.day

    pred_p = pd.read_csv(f'./predict/static/images/predict_{today}.csv')
    price_vege = pd.read_csv(f'./statistic/static/graph/base_data_{today}.csv')
    vege = ['깻잎', '대파', '마늘', '무', '배추', '상추', '양파', '시금치', '양상추']
    price = []
    for i in vege:
        price.append(pred_p[i])

    ctx = {
        'list': all_list,
        'vege' : vege,
        'price':price
    }
    return render(
        request,
        'predict/total.html',
        ctx
    )

