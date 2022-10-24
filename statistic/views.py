from django.shortcuts import render
from datetime import datetime, timedelta

today = datetime.now() - timedelta(1)
today = today.year * 10000 + today.month * 100 + today.day

def total(request):
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
    }
    return render(request, 'statistic/total.html', ctx)

def p1(requeast):
    ctx = {
        'price': f'../../static/graph/statistic_p1_{today}.png',
        'cnt': f'../../static/graph/statistic_p1_{today}_.png'
    }
    return render(requeast, 'statistic/p1.html', ctx)
def p2(requeast):
    ctx = {
        'price': f'../../static/graph/statistic_p2_{today}.png',
        'cnt': f'../../static/graph/statistic_p2_{today}_.png'
    }
    return render(requeast, 'statistic/p2.html',ctx)
def p3(requeast):
    ctx = {
        'price': f'../../static/graph/statistic_p3_{today}.png',
        'cnt': f'../../static/graph/statistic_p3_{today}_.png'
    }
    return render(requeast, 'statistic/p3.html', ctx)
def p4(requeast):
    ctx = {
        'price': f'../../static/graph/statistic_p4_{today}.png',
        'cnt': f'../../static/graph/statistic_p4_{today}_.png'
    }
    return render(requeast, 'statistic/p4.html', ctx)
def p5(requeast):
    ctx = {
        'price': f'../../static/graph/statistic_p5_{today}.png',
        'cnt': f'../../static/graph/statistic_p5_{today}_.png'
    }
    return render(requeast, 'statistic/p5.html', ctx)
def p6(requeast):
    ctx = {
        'price': f'../../static/graph/statistic_p6_{today}.png',
        'cnt': f'../../static/graph/statistic_p6_{today}_.png'
    }
    return render(requeast, 'statistic/p6.html', ctx)
def p7(requeast):
    ctx = {
        'price': f'../../static/graph/statistic_p7_{today}.png',
        'cnt': f'../../static/graph/statistic_p7_{today}_.png'
    }
    return render(requeast, 'statistic/p7.html', ctx)
def p8(requeast):
    ctx = {
        'price': f'../../static/graph/statistic_p8_{today}.png',
        'cnt': f'../../static/graph/statistic_p8_{today}_.png'
    }
    return render(requeast, 'statistic/p8.html', ctx)
def p9(requeast):
    ctx = {
        'price': f'../../static/graph/statistic_p9_{today}.png',
        'cnt': f'../../static/graph/statistic_p9_{today}_.png'
    }
    return render(requeast, 'statistic/p9.html', ctx)
