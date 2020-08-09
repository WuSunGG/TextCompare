import json
import logging
import os

from flask import Flask, request

from component.progress.progress import progress
from dev_SimHash import comparePaper, getPaperSimhash
from tools import buildSuccessResponse, buildErrorResponse

app = Flask(__name__)

if not os.path.isdir("./logs"):
    os.mkdir("./logs")

logging.basicConfig(
    filename="./logs/access.log",
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    datefmt='%Y-%m-%d  %H:%M:%S %a'
)

logging.info("start application.....")


@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin'] = '*'
    environ.headers['Access-Control-Allow-Method'] = '*'
    environ.headers['Access-Control-Allow-Headers'] = '*'
    return environ


@app.route('/')
def index():
    return "access denied"


"""
html 查重
req:
{
  "type": "html",  
  "distance":20,  
  "papers": [   
    {
      "name": "zhangsan",
      "sno": "2019201964",
      "papername": "if i was a boy",
      "content":"<h1>if i was a boy, i will go to fly like a bird</h1>"
    },
       {
      "name": "zhangsan",
      "sno": "2019201963",
      "papername": "if i was a boy",
      "content":"<h1>if i was a boy, i will go to fly like a bird</h1>"
    }
  ]
}
res:
{
  "code": "成功",
  "data": {
    "2019201961": [
      {
        "content": "<h1>if i was a boy, i will go to fly like a birdxxx</h1>",
        "distance": -1,
        "name": "zhangsan",
        "papername": "if i was a boysss",
        "sno": "2019201961"
      },
      {
        "content": "<h1>if i was a boy, i will go to fly like a bird</h1>",
        "distance": 8,
        "name": "zhangsan",
        "papername": "if i was a boy",
        "percent": 77.77777777777779,
        "sno": "2019201962"
      }
    ]
  },
  "message": "成功",
  "status": 200,
  "type": "sshd"
}
"""


@app.route('/v1/html', methods=['POST'])
def compare_text():
    try:
        req = json.loads(request.data.decode())
        req['uid']
        req['type']
        req['papers']
        req['distance']
    except Exception as e:
        logging.error(e)
        return buildErrorResponse("request format is error : {}".format(e))
    pross = progress(req['uid'])
    try:
        pross.putMsg("开始转换", 0.0)
        papersObj = {}
        all_counts = len(req['papers'])
        count = 0
        for paper in req['papers']:
            pross.putMsg("转换地 {} 篇文章".format(count + 1), (count / all_counts)*100)
            count += 1
            tsimhash = getPaperSimhash(paper['content'])
            papersObj[paper['sno']] = paper
            papersObj[paper['sno']]['content'] = paper['content']
            papersObj[paper['sno']]['simhash'] = tsimhash
            # 计算每篇文章和其他文章的相似度
        cres = comparePaper(papersObj, req['distance'])
        pross.putMsg("转换完成", 100.0)
        return buildSuccessResponse(cres)

    except Exception as e:
        logging.error(e)
        return buildSuccessResponse("paper format is error: {}".format(e))
