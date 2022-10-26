    # 배추, 양파, 고추, 마늘, 깻잎, 대파(일반), 상추, 무, 시금치, 애호박


def func():
    import requests
    import xml.etree.ElementTree as ET
    import pandas as pd
    from datetime import datetime, timedelta
    import os
    def check_(set, 작물):
        if set.shape[0] == 0:
            return
        if 작물 == '배추':
            b = set.loc[(set[0] == '배추') & (set[3].isin(['특(1등)', '상(2등)']))]
            c['배추_거래량(kg)'] = [b[2].str[:-2].astype(float).sum()]
            c['배추_가격(원/kg)'] = [int(round((b[4].astype(float) / b[2].str[:-2].astype(float)).mean(), 0))]
            return

        if 작물 == '양파':
            b = set.loc[(set[0] == '양파') & (set[3].isin(['특(1등)', '상(2등)']))]
            c['양파_거래량(kg)'] = [b[2].str[:-2].astype(float).sum()]
            c['양파_가격(원/kg)'] = [int(round((b[4].astype(float) / b[2].str[:-2].astype(float)).mean(), 0))]
            return

        if 작물 == '마늘':
            b = set.loc[set[3].isin(['특(1등)', '상(2등)'])]
            c['마늘_거래량(kg)'] = [b[2].str[:-2].astype(float).sum()]
            c['마늘_가격(원/kg)'] = [int(round((b[4].astype(float) / b[2].str[:-2].astype(float)).mean(), 0))]
            return

        if 작물 == '깻잎':
            b = a.loc[(a[3] == '특(1등)') & (a[1].isin(['깻잎', '깻잎(찹찹)', '찹찹이', '깻잎(찹)']))]
            c['깻잎_거래량(kg)'] = [b[2].str[:-2].astype(float).sum()]
            c['깻잎_가격(원/kg)'] = [int(round((b[4].astype(float) / b[2].str[:-2].astype(float)).mean(), 0))]
            return

        if 작물 == '대파':
            b = set.loc[(set[3].isin(['특(1등)', '상(2등)'])) & (set[1].isin(['대파(일반) ', '대파']))]
            c['대파_거래량(kg)'] = [b[2].str[:-2].astype(float).sum()]
            c['대파_가격(원/kg)'] = [int(round((b[4].astype(float) / b[2].str[:-2].astype(float)).mean(), 0))]
            return

        if 작물 == '상추':
            b = set.loc[(a[0].isin(['상추'])) & (set[3].isin(['특(1등)', '상(2등)']))]
            c['상추_거래량(kg)'] = [b[2].str[:-2].astype(float).sum()]
            c['상추_가격(원/kg)'] = [int(round((b[4].astype(float) / b[2].str[:-2].astype(float)).mean(), 0))]
            return

        if 작물 == '양상추':
            b = set.loc[(set[0].isin(['양상추', '양상추기타'])) & (set[3].isin(['특(1등)', '상(2등)']))]
            c['양상추_거래량(kg)'] = [b[2].str[:-2].astype(float).sum()]
            c['양상추_가격(원/kg)'] = [int(round((b[4].astype(float) / b[2].str[:-2].astype(float)).mean(), 0))]
            return

        if 작물 == '무':
            b = set.loc[(set[1].isin(['무순', '가을무', '월동무', '무', '가을무(김장)', '다발무', '총각무(일반)', '세척무', '무우',
                                      '마대무우', '저장무우', '저장무', '봄무', '봄무우', '여름무', '고냉지무우', '고냉지무 ', '고랭지무',
                                      '다발무우', '무(다발)', '김장무우', '천수무'])) & (set[3].isin(['특(1등)', '상(2등)']))]
            c['무_거래량(kg)'] = [b[2].str[:-2].astype(float).sum()]
            c['무_가격(원/kg)'] = [int(round((b[4].astype(float) / b[2].str[:-2].astype(float)).mean(), 0))]
            return

        if 작물 == '시금치':
            b = set.loc[(set[3].isin(['특(1등)', '상(2등)']))]
            c['시금치_거래량(kg)'] = [b[2].str[:-2].astype(float).sum()]
            c['시금치_가격(원/kg)'] = [int(round((b[4].astype(float) / b[2].str[:-2].astype(float)).mean(), 0))]
            return

    today = datetime.now()
    today = today.year * 10000 + today.month * 100 + today.day

    yesterday = datetime.now() - timedelta(1)
    yesterday = yesterday.year * 10000 + yesterday.month * 100 + yesterday.day

    glyph = datetime.now() - timedelta(2)
    glyph = glyph.year * 10000 + glyph.month * 100 + glyph.day

    start = today
    all_date = pd.DataFrame()
    c = pd.DataFrame()
    c['date'] = [start]
    작물 = ['배추', '양파', '마늘', '깻잎', '대파', '상추', '양상추', '무', '시금치']
    for wkranf in range(9):
        a = []
        for s_bubin in range(1,7):
            j = 1
            while True:
                url = f'https://www.garak.co.kr/publicdata/dataOpen.do?id=3279&passwd=qwer1234!@&dataid=data12&pagesize=10&pageidx={j}&portal.templet=false&s_date={start}&s_bubin=1100010{s_bubin}&s_pummok={작물[wkranf]}&s_sangi='
                text =  requests.get(url).text
                root = ET.fromstring(text)
                if int(root.find('list_total_count').text) == 0:
                    break
                else:
                    j += 1
                    for i in root.findall('list'):
                        b = []
                        b.append(i.find('PUMMOK').text)
                        b.append(i.find('PUMJONG').text)
                        b.append(i.find('UUN').text)
                        b.append(i.find('DDD').text)
                        b.append(i.find('PPRICE').text)
                        b.append(i.find('ADJ_DT').text)
                        a.append(b)
        a = pd.DataFrame(a)
        check_(a,작물[wkranf])
    all_date = pd.concat([all_date, c])
    data = all_date

    data['date'] = data['date'].astype(int).astype(str)
    data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
    data['요일'] = data['date'].dt.weekday
    data['date'] = data['date'].astype(str)
    data['요일'] = data['요일'].replace([0,1,2,3,4,5,6],['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일'])
    data = pd.concat([data['date'], data['요일'], data.iloc[:,1:-1]], axis = 1)

    qwer = pd.read_csv(f'./statistic/static/graph/base_data_{yesterday}.csv')
    qwer = pd.concat([qwer, data])
    if 'Unnamed: 0' in qwer.columns:
        qwer.drop(['Unnamed: 0'], axis = 1, inplace = True)
    qwer.to_csv(f'./statistic/static/graph/base_data_{today}.csv')

    if os.path.exists(f'./statistic/static/graph/base_data_{glyph}.csv'):
        os.remove(f'./statistic/static/graph/base_data_{glyph}.csv')