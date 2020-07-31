# myfilter.py文件里
from urllib.parse import quote

from django import template
register = template.Library()
import base64

@register.filter(name="parsetostring")  # 起一个名字
def parsetostring(value):
    return value
    # print("filter---",base64.b64encode(str(value).encode()))
    # return base64.b64encode(str(value).encode())
    # return base64.b64encode(str(value))
# http://192.168.5.30:8000/v2/compare/Li93b3Jrcy8xNei9r+W3pS00NS3lkLTlvLouZG9jeA==/Li93b3Jrcy8xNei9r+W3pS00Ni3nvZfmsLjlj4wuZG9jeA==
# 编码过后的字符串解码
def stringtofile(value):
    base64.decode(value.decode())