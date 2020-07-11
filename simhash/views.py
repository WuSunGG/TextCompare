from django.http import HttpResponse
from django.shortcuts import render

from simhash.simhash import SimHash
import difflib
import sys

def index(request):
    context = {
        'answer':'1',
        'tx1':'1',
        'tx2':'1',
        'issame':"",#是否显示
        'hmdistance':'',#海明距离,
        'dedistance':'',# 判断距离,
        'diffe':''# 对比结果
    }

    try:
        simhash=SimHash()
        tx1 =  (request.POST['tx1'])
        tx2 =  (request.POST['tx2'])
        context['tx1']=tx1
        context['tx2']=tx2
        if len(tx1) <= 2 or len(tx2) <= 2:
            context['answer'] = "对比文本不能小于2字符"
        else:
            hash1 = simhash.hash(tx1)
            hash2 = simhash.hash(tx2)
            distince = simhash.getDistince(hash1, hash2)
            value = 20
            context['hmdistance']=distince
            context['dedistance']=value
            context['issame']=distince <= value
            res="海明距离："+ str(distince)+ " 判定距离："+ str(value) + " 是否相似 "+ str(distince <= value)
            context['answer']=res

            dtx1=tx1.splitlines()
            dtx2=tx2.splitlines()
            d = difflib.HtmlDiff()
            dres = d.make_file(dtx1, dtx2, charset="utf-8")
            context['diffe']=dres
    except KeyError:
        context['answer'] = '空字符串'
        return render(request, 'simhash.html', context)
    return render(request, 'simhash.html', context)



def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)