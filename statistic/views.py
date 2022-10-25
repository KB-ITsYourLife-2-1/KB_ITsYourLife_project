import shutil
from django.shortcuts import render
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import os
import requests

today = datetime.now() - timedelta(1)
today = today.year * 10000 + today.month * 100 + today.day

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

    ctx = {
        'price1' : f'../../static/graph/statistic_p1_{today}.png',
        'price2': f'../../static/graph/statistic_p2_{today}.png',
        'price3': f'../../static/graph/statistic_p3_{today}.png',
        'price4': f'../../static/graph/statistic_p4_{today}.png',
        'price5': f'../../static/graph/statistic_p5_{today}.png',
        'price6': f'../../static/graph/statistic_p6_{today}.png',
        'price7': f'../../static/graph/statistic_p7_{today}.png',
        'price8': f'../../static/graph/statistic_p8_{today}.png',
        'price9': f'../../static/graph/statistic_p9_{today}.png',
        'title': title_list, 'link': link_list
    }

    return render(request, 'statistic/total.html', ctx)

def p1(requeast):
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
    ctx = {
        'price': f'../../static/graph/statistic_p1_{today}.png',
        'cnt': f'../../static/graph/statistic_p1_{today}_.png',
        'title': title_list, 'link': link_list
    }
    return render(requeast, 'statistic/p1.html', ctx)
def p2(requeast):
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
    ctx = {
        'price': f'../../static/graph/statistic_p2_{today}.png',
        'cnt': f'../../static/graph/statistic_p2_{today}_.png',
        'title': title_list, 'link': link_list
    }
    return render(requeast, 'statistic/p2.html',ctx)
def p3(requeast):
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
    ctx = {
        'price': f'../../static/graph/statistic_p3_{today}.png',
        'cnt': f'../../static/graph/statistic_p3_{today}_.png',
        'title': title_list, 'link': link_list
    }
    return render(requeast, 'statistic/p3.html', ctx)
def p4(requeast):
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
    ctx = {
        'price': f'../../static/graph/statistic_p4_{today}.png',
        'cnt': f'../../static/graph/statistic_p4_{today}_.png',
        'title': title_list, 'link': link_list
    }
    return render(requeast, 'statistic/p4.html', ctx)
def p5(requeast):
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
    ctx = {
        'price': f'../../static/graph/statistic_p5_{today}.png',
        'cnt': f'../../static/graph/statistic_p5_{today}_.png',
        'title': title_list, 'link': link_list
    }
    return render(requeast, 'statistic/p5.html', ctx)
def p6(requeast):
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
    ctx = {
        'price': f'../../static/graph/statistic_p6_{today}.png',
        'cnt': f'../../static/graph/statistic_p6_{today}_.png',
        'title': title_list, 'link': link_list
    }
    return render(requeast, 'statistic/p6.html', ctx)
def p7(requeast):
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
    ctx = {
        'price': f'../../static/graph/statistic_p7_{today}.png',
        'cnt': f'../../static/graph/statistic_p7_{today}_.png',
        'title': title_list, 'link': link_list
    }
    return render(requeast, 'statistic/p7.html', ctx)
def p8(requeast):
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
    ctx = {
        'price': f'../../static/graph/statistic_p8_{today}.png',
        'cnt': f'../../static/graph/statistic_p8_{today}_.png',
        'title': title_list, 'link': link_list
    }
    return render(requeast, 'statistic/p8.html', ctx)
def p9(requeast):
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
    ctx = {
        'price': f'../../static/graph/statistic_p9_{today}.png',
        'cnt': f'../../static/graph/statistic_p9_{today}_.png',
        'title': title_list, 'link': link_list
    }
    return render(requeast, 'statistic/p9.html', ctx)
