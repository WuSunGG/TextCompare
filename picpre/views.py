from django.http import HttpResponse
from django.shortcuts import render

from simhash.simhash import SimHash
import difflib
import sys
from  picpre.pic_prediect import pre_pic


def index(request):
    context = {
        'pre':'',
        'sourcepic':'',# 原图片
        'targetpic':'' # 目标图片
    }

    try:
        if request.method == 'POST':
            file=request.FILES['upic']
            with open(str(file), 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            filename=str(file)
            context['sourcepic']=filename
            res=pre_pic(filename,5)
            context['targetpic']=res
            return render(request, 'picpre.html', context)
        else:
            print("get")

    except KeyError:
        context['answer'] = '空字符串'
        return render(request, 'picpre.html', context)
    return render(request, 'picpre.html', context)
