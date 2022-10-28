from django.views.generic.edit import CreateView
from django.shortcuts import render
from .forms import ImageUploadForm
from .models import ImageModel
from bs4 import BeautifulSoup
from PIL import Image as im
import shutil
import requests
import torch
import os
import io
from datetime import datetime, timedelta

today = datetime.now() - timedelta(1)
today = today.year * 10000 + today.month* 100 + today.day

def landing(request):
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
        'price1': f'../../static/graph/main_p1_{today}.png',
        'price2': f'../../static/graph/main_p2_{today}.png',
        'price3': f'../../static/graph/main_p3_{today}.png',
        'price4': f'../../static/graph/main_p4_{today}.png',
        'list': all_list
    }
    return render(
        request,
        'single_pages/landing.html',
        ctx
    )


class UploadImage(CreateView):
    model = ImageModel
    template_name = 'single_pages/find.html'
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = request.FILES.get('image')
            img_instance = ImageModel(
                image=img
            )
            img_instance.save()

            uploaded_img_qs = ImageModel.objects.filter().last()
            img_bytes = uploaded_img_qs.image.read()
            img = im.open(io.BytesIO(img_bytes))
            img_size = img.size

            path_hubconfig = "yolov5"
            path_weightfile = "single_pages/best.pt"
            img_name = {0: '양파',
                        1: '배추',
                        2: '깻잎',
                        3: '시금치',
                        4: '깻잎',
                        5: '무',
                        6: '상추',
                        7: '양상추',
                        8: '대파',
                        9: '마늘'}
            model = torch.hub.load(path_hubconfig, 'custom', path=path_weightfile, source='local')
            model.eval()
            torch.no_grad()
            model.conf = 0.6
            model.names = img_name
            results = model(img, size=160)

            results.render()
            for img in results.ims:
                img_base64 = im.fromarray(img).resize(img_size)
                img_base64.save("media/image0.jpg", format="JPEG")

            inference_img = "/media/image0.jpg"
            img_class = set(results.pandas().xyxy[0]['class'])

            img_sta = {0: 'statistic_7',
                       1: 'statistic_5',
                       2: 'statistic_1',
                       3: 'statistic_8',
                       4: 'statistic_1',
                       5: 'statistic_4',
                       6: 'statistic_6',
                       7: 'statistic_9',
                       8: 'statistic_2',
                       9: 'statistic_3'}
            img_inf = {0: 'about_7',
                       1: 'about_5',
                       2: 'about_1',
                       3: 'about_8',
                       4: 'about_1',
                       5: 'about_4',
                       6: 'about_6',
                       7: 'about_9',
                       8: 'about_2',
                       9: 'about_3'}
            img_all = []
            for i in img_class:
                a = []
                a.append(img_name[i])
                a.append('predict')
                a.append(img_sta[i])
                a.append(img_inf[i])
                img_all.append(a)

            form = ImageUploadForm()
            context = {
                "form": form,
                "inference_img": inference_img,
                'img_all': img_all,
            }
            return render(request, 'single_pages/find.html', context)

        else:
            form = ImageUploadForm()
        context = {
            "form": form,
        }

        return render(request, 'single_pages/find.html', context)
