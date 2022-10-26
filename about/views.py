from django.shortcuts import render
from bs4 import BeautifulSoup
import os
import requests
# Create your views here.

def about(request):
    # make()
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
        "about/about.html",ctx
    )
def p1(request):
    if os.path.isfile('media/yolo5'):
        shutil.rmtree('media/yolo5')
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
        "about/p1.html",
        ctx
    )
def p2(requeast):
    if os.path.isfile('media/yolo5'):
        shutil.rmtree('media/yolo5')
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
        requeast,
        'about/p2.html',
        ctx
    )
def p3(requeast):
    if os.path.isfile('media/yolo5'):
        shutil.rmtree('media/yolo5')
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
        requeast,
        'about/p3.html',
        ctx
    )
def p4(requeast):
    if os.path.isfile('media/yolo5'):
        shutil.rmtree('media/yolo5')
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
        requeast,
        'about/p4.html',
        ctx
    )
def p5(requeast):
    if os.path.isfile('media/yolo5'):
        shutil.rmtree('media/yolo5')
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
        requeast,
        'about/p5.html',
        ctx
    )
def p6(requeast):
    if os.path.isfile('media/yolo5'):
        shutil.rmtree('media/yolo5')
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
        requeast,
        'about/p6.html',
        ctx
    )
def p7(requeast):
    if os.path.isfile('media/yolo5'):
        shutil.rmtree('media/yolo5')
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
        requeast,
        'about/p7.html',
        ctx
    )
def p8(requeast):
    if os.path.isfile('media/yolo5'):
        shutil.rmtree('media/yolo5')
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
        requeast,
        'about/p8.html',
        ctx
    )

def p9(requeast):
    if os.path.isfile('media/yolo5'):
        shutil.rmtree('media/yolo5')
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
        requeast,
        'about/p9.html',
        ctx
    )