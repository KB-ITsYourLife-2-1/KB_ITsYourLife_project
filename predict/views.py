from django.shortcuts import render
from bs4 import BeautifulSoup
import os
import requests
# Create your views here.

def total(request):
    if os.path.isfile('media/yolo5'):
        shutil.rmtree('media/yolo5')
    url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%86%8D%EC%82%B0%EB%AC%BC"

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    news_lis = soup.select('#main_pack > section > div > div.group_news > ul > li')
    title_list = []
    link_list = []
    for li in news_lis:
        title = li.find('a', class_='news_tit')['title']
        a_href = li.find('a', class_='news_tit')['href']
        title_list.append(title)
        link_list.append(a_href)
    return render(
        request,
        'predict/total.html',
        {'title': title_list, 'link': link_list}
    )

