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
    title_list = []
    link_list = []
    for li in news_lis:
        title = li.find('a', class_='news_tit')['title']
        a_href = li.find('a', class_='news_tit')['href']
        title_list.append(title)
        link_list.append(a_href)
    return render(
        request,
        "about/about.html",
        {'title': title_list, 'link': link_list}
    )
def p1(request):
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
        "about/p1.html",
        {'title': title_list, 'link': link_list}
    )
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
    return render(
        requeast,
        'about/p2.html',
        {'title': title_list, 'link': link_list}
    )
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
    return render(
        requeast,
        'about/p3.html',
        {'title': title_list, 'link': link_list}
    )
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
    return render(
        requeast,
        'about/p4.html',
        {'title': title_list, 'link': link_list}
    )
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
    return render(
        requeast,
        'about/p5.html',
        {'title': title_list, 'link': link_list}
    )
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
    return render(
        requeast,
        'about/p6.html',
        {'title': title_list, 'link': link_list}
    )
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
    return render(
        requeast,
        'about/p7.html',
        {'title': title_list, 'link': link_list}
    )
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
    return render(
        requeast,
        'about/p8.html',
        {'title': title_list, 'link': link_list}
    )

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
    return render(
        requeast,
        'about/p9.html',
        {'title': title_list, 'link': link_list}
    )