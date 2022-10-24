from datetime import datetime, timedelta
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import os
plt.rcParams['font.family'] = 'Malgun Gothic'

today = datetime.now()
today = today.year * 10000 + today.month * 100 + today.day

yesterday = datetime.now() - timedelta(2)
yesterday = yesterday.year * 10000 + yesterday.month * 100 + yesterday.day

# 데이터 불러오기
data = pd.read_csv(f"../statistic/static/graph/base_data_{today}.csv")

# 데이터 전처리
data = data.tail(7)
data = data.fillna(0)
data["date"] = pd.to_datetime(data["date"]).dt.strftime('%m/%d')
dt = data.drop(columns=['Unnamed: 0', '요일', '배추_거래량(kg)', '양파_거래량(kg)', '마늘_거래량(kg)', '깻잎_거래량(kg)',
                        '대파_거래량(kg)', '상추_거래량(kg)', '양상추_거래량(kg)', '무_거래량(kg)', '시금치_거래량(kg)'])
dt.rename(columns={'배추_가격(원/kg)': '배추', '양파_가격(원/kg)': '양파', '마늘_가격(원/kg)': '마늘', '깻잎_가격(원/kg)': '깻잎',
                   '대파_가격(원/kg)': '대파', '상추_가격(원/kg)': '상추', '양상추_가격(원/kg)': '양상추', '무_가격(원/kg)': '무',
                   '시금치_가격(원/kg)': '시금치'}, inplace=True)
dt_ = data[['date', '배추_거래량(kg)', '양파_거래량(kg)', '마늘_거래량(kg)', '깻잎_거래량(kg)',
            '대파_거래량(kg)', '상추_거래량(kg)', '양상추_거래량(kg)', '무_거래량(kg)', '시금치_거래량(kg)']].copy()
dt_.rename(columns={'배추_거래량(kg)': '배추', '양파_거래량(kg)': '양파', '마늘_거래량(kg)': '마늘', '깻잎_거래량(kg)': '깻잎',
                    '대파_거래량(kg)': '대파', '상추_거래량(kg)': '상추', '양상추_거래량(kg)': '양상추', '무_거래량(kg)': '무',
                    '시금치_거래량(kg)': '시금치'}, inplace=True)
dt_[['배추', '양파', '마늘', '깻잎', '대파', '상추', '양상추', '무', '시금치']] = dt_[
    ['배추', '양파', '마늘', '깻잎', '대파', '상추', '양상추', '무', '시금치']].round(1)

# 가격통계
vege_name = ['깻잎', '대파', '마늘', '무', '배추', '상추', '양파', '시금치', '양상추']
for i in range(9):
    plt.figure(figsize=(6, 4))
    p = dt[["date", vege_name[i]]]
    bar = plt.bar(p["date"], p[vege_name[i]], label="가격 (원)", color='orange', edgecolor='darkorange', linewidth=2)
    plt.legend(loc=(0.4, -0.2))
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%.1f' % height, ha='center', va='bottom', size=12)
    plt.savefig(f'../statistic/static/graph/statistic_p{i+1}_{today}.png', bbox_inches='tight',pad_inches=0.3)
    if os.path.exists(f'../statistic/static/graph/statistic_p{i+1}_{yesterday}.png'):
        os.remove(f'../statistic/static/graph/statistic_p{i+1}_{yesterday}.png')

# 거래량통계
for i in range(9):
    plt.figure(figsize=(6, 4))
    p = dt_[["date",  vege_name[i]]]
    bar = plt.plot(p["date"], p[vege_name[i]], '.-', label="거래량 (kg)", color='darkorange')
    plt.legend(loc=(0.35, -0.2))
    plt.fill_between(p['date'], p[vege_name[i]], alpha=0.5, color='orange')
    plt.savefig(f'../statistic/static/graph/statistic_p{i+1}_{today}_.png', bbox_inches='tight',pad_inches=0.3)
    if os.path.exists(f'../statistic/static/graph/statistic_p{i+1}_{yesterday}_.png'):
        os.remove(f'../statistic/static/graph/statistic_p{i+1}_{yesterday}_.png')