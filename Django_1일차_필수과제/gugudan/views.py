from django.shortcuts import render

def gugudan(request):
    gugudan_list = []
    for i in range(2, 10):
        dan_list = []
        for j in range(1, 10):
            dan_list.append(f'{i} * {j} = {i*j}')
        gugudan_list.append(dan_list)
    return render(request, 'gugudan/gugudan.html', {'gugudan_list': gugudan_list})

def gugudan_dan(request, dan):
    dan_list = []
    for i in range(1, 10):
        dan_list.append(f'{dan} * {i} = {dan*i}')
    return render(request, 'gugudan/gugudan_dan.html', {'dan_list': dan_list, 'dan': dan})
