import json

from django.http import HttpResponse
from simhash.logger import Logger
loger=Logger()

def buildResponseSuccess(data):
    resdata=json.dumps({
        "code": 200,
        "type": "success",
        "msg": "",
        "data": data
    })
    loger.debug(resdata)
    return HttpResponse(resdata,content_type="application/json,charset=utf-8")


def buildResponseError(msg):
    return HttpResponse(json.dumps({
        "code": 500,
        "type": "error",
        "msg": msg
        ,
    }),content_type="application/json,charset=utf-8")
