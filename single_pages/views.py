from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

def make():
    # 데이터 불러오기
    data = pd.read_csv(
        "C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/ns.csv")

    # 데이터 전처리
    data = data.tail(7)
    data["date"] = pd.to_datetime(data["date"]).dt.strftime('%m/%d')
    dt = data.drop(columns=['Unnamed: 0', '배추_거래량(kg)', '양파_거래량(kg)', '마늘_거래량(kg)', '깻잎_거래량(kg)',
                            '대파_거래량(kg)', '상추_거래량(kg)', '양상추_거래량(kg)', '무_거래량(kg)', '시금치_거래량(kg)', 'day'])
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
    ## 깻잎
    plt.figure(figsize=(6, 4))
    p1 = dt[["date", "깻잎"]]
    bar1 = plt.bar(p1["date"], p1["깻잎"], label="가격 (원)", color='orange', edgecolor='darkorange', linewidth=2)
    plt.legend(loc=(0.4, -0.2))
    for rect in bar1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%.1f' % height, ha='center', va='bottom', size=10)
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p1.png', bbox_inches='tight',
                pad_inches=0.3)

    ## 대파
    plt.figure(figsize=(6, 4))
    p2 = dt[["date", "대파"]]
    bar2 = plt.bar(p2["date"], p2["대파"], label="가격 (원)", color='orange', edgecolor='darkorange', linewidth=2)
    plt.legend(loc=(0.4, -0.2))
    for rect in bar2:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%.1f' % height, ha='center', va='bottom', size=12)
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p2.png', bbox_inches='tight',
                pad_inches=0.3)

    ## 마늘
    plt.figure(figsize=(6, 4))
    p3 = dt[["date", "마늘"]]
    bar3 = plt.bar(p3["date"], p3["마늘"], label="가격 (원)", color='orange', edgecolor='darkorange', linewidth=2)
    plt.legend(loc=(0.4, -0.2))
    for rect in bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height * 0.99, '%.1f' % height, ha='center', va='bottom',
                 size=12)
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p3.png', bbox_inches='tight',
                pad_inches=0.3)

    ## 무
    plt.figure(figsize=(6, 4))
    p4 = dt[["date", "무"]]
    bar4 = plt.bar(p4["date"], p4["무"], label="가격 (원)", color='orange', edgecolor='darkorange', linewidth=2)
    plt.legend(loc=(0.4, -0.2))
    for rect in bar4:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height * 0.99, '%.1f' % height, ha='center', va='bottom',
                 size=12)
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p4.png', bbox_inches='tight',
                pad_inches=0.3)

    ## 배추
    plt.figure(figsize=(6, 4))
    p5 = dt[["date", "배추"]]
    bar5 = plt.bar(p5["date"], p5["배추"], label="가격 (원)", color='orange', edgecolor='darkorange', linewidth=2)
    plt.legend(loc=(0.4, -0.2))
    for rect in bar5:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height * 0.99, '%.1f' % height, ha='center', va='bottom',
                 size=12)
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p5.png', bbox_inches='tight',
                pad_inches=0.3)

    ## 상추
    plt.figure(figsize=(6, 4))
    p6 = dt[["date", "상추"]]
    bar6 = plt.bar(p6["date"], p6["상추"], label="가격 (원)", color='orange', edgecolor='darkorange', linewidth=2)
    plt.legend(loc=(0.4, -0.2))
    for rect in bar6:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height * 0.99, '%.1f' % height, ha='center', va='bottom',
                 size=12)
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p6.png', bbox_inches='tight',
                pad_inches=0.3)

    ## 양파
    plt.figure(figsize=(6, 4))
    p7 = dt[["date", "양파"]]
    bar7 = plt.bar(p7["date"], p7["양파"], label="가격 (원)", color='orange', edgecolor='darkorange', linewidth=2)
    plt.legend(loc=(0.4, -0.2))
    for rect in bar7:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height * 0.99, '%.1f' % height, ha='center', va='bottom',
                 size=12)
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p7.png', bbox_inches='tight',
                pad_inches=0.3)

    ## 시금치
    plt.figure(figsize=(6, 4))
    p8 = dt[["date", "시금치"]]
    bar8 = plt.bar(p8["date"], p8["시금치"], label="가격 (원)", color='orange', edgecolor='darkorange', linewidth=2)
    plt.legend(loc=(0.4, -0.2))
    for rect in bar8:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height * 0.99, '%.1f' % height, ha='center', va='bottom',
                 size=12)
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p8.png', bbox_inches='tight',
                pad_inches=0.3)

    ## 양상추
    plt.figure(figsize=(6, 4))
    p9 = dt[["date", "양상추"]]
    bar9 = plt.bar(p9["date"], p9["양상추"], label="가격 (원)", color='orange', edgecolor='darkorange', linewidth=2)
    plt.legend(loc=(0.4, -0.2))
    for rect in bar9:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%.1f' % height, ha='center', va='bottom', size=12)
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p9.png', bbox_inches='tight',
                pad_inches=0.3)

    # 거래량통계
    ## 깻잎
    plt.figure(figsize=(6, 4))
    p = dt_[["date", "깻잎"]]
    bar = plt.plot(p["date"], p["깻잎"], '.-', label="거래량 (kg)", color='darkorange')
    plt.legend(loc=(0.35, -0.2))
    plt.fill_between(p['date'], p["깻잎"], alpha=0.5, color='orange')
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p1_.png', bbox_inches='tight',
                pad_inches=0.3)

    ## 대파
    plt.figure(figsize=(6, 4))
    p = dt_[["date", "대파"]]
    bar = plt.plot(p["date"], p["대파"], '.-', label="거래량 (kg)", color='darkorange')
    plt.legend(loc=(0.35, -0.2))
    plt.fill_between(p['date'], p["대파"], alpha=0.5, color='orange')
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p2_.png', bbox_inches='tight',
                pad_inches=0.3)

    ## 마늘
    plt.figure(figsize=(6, 4))
    p = dt_[["date", "마늘"]]
    bar = plt.plot(p["date"], p["마늘"], '.-', label="거래량 (kg)", color='darkorange')
    plt.legend(loc=(0.35, -0.2))
    plt.fill_between(p['date'], p["마늘"], alpha=0.5, color='orange')
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p3_.png', bbox_inches='tight',
                pad_inches=0.3)

    ## 무
    plt.figure(figsize=(6, 4))
    p = dt_[["date", "무"]]
    bar = plt.plot(p["date"], p["무"], '.-', label="거래량 (kg)", color='darkorange')
    plt.legend(loc=(0.35, -0.2))
    plt.fill_between(p['date'], p["무"], alpha=0.5, color='orange')
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p4_.png', bbox_inches='tight',
                pad_inches=0.3)

    ## 배추
    plt.figure(figsize=(6, 4))
    p = dt_[["date", "배추"]]
    bar = plt.plot(p["date"], p["배추"], '.-', label="거래량 (kg)", color='darkorange')
    plt.legend(loc=(0.35, -0.2))
    plt.fill_between(p['date'], p["배추"], alpha=0.5, color='orange')
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p5_.png', bbox_inches='tight',
                pad_inches=0.3)

    ## 상추
    plt.figure(figsize=(6, 4))
    p = dt_[["date", "상추"]]
    bar = plt.plot(p["date"], p["상추"], '.-', label="거래량 (kg)", color='darkorange')
    plt.legend(loc=(0.35, -0.2))
    plt.fill_between(p['date'], p["상추"], alpha=0.5, color='orange')
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p6_.png', bbox_inches='tight',
                pad_inches=0.3)

    ## 양파
    plt.figure(figsize=(6, 4))
    p = dt_[["date", "양파"]]
    bar = plt.plot(p["date"], p["양파"], '.-', label="거래량 (kg)", color='darkorange')
    plt.legend(loc=(0.35, -0.2))
    plt.fill_between(p['date'], p["양파"], alpha=0.5, color='orange')
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p7_.png', bbox_inches='tight',
                pad_inches=0.3)

    ## 시금치
    plt.figure(figsize=(6, 4))
    p = dt_[["date", "시금치"]]
    bar = plt.plot(p["date"], p["시금치"], '.-', label="거래량 (kg)", color='darkorange')
    plt.legend(loc=(0.35, -0.2))
    plt.fill_between(p['date'], p["시금치"], alpha=0.5, color='orange')
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p8_.png', bbox_inches='tight',
                pad_inches=0.3)

    ## 양상추
    plt.figure(figsize=(6, 4))
    p = dt_[["date", "양상추"]]
    bar = plt.plot(p["date"], p["양상추"], '.-', label="거래량 (kg)", color='darkorange')
    plt.legend(loc=(0.35, -0.2))
    plt.fill_between(p['date'], p["양상추"], alpha=0.5, color='orange')
    plt.savefig('C:/Users/Admin/Desktop/WEB/project/statistic/static/graph/statistic_p9_.png', bbox_inches='tight',
                pad_inches=0.3)

def landing(request):
    make()
    return render(
        request,
        'single_pages/landing.html'
    )

def find(request):
    return render(
        request,
        'single_pages/find.html'
    )