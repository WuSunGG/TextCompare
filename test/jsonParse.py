import json

from dev_SimHash import getPaperSimhash, comparePaper

with open('req.json') as f:
    req = json.load(f)

papersObj = {}
for paper in req['papers']:
    tsimhash = getPaperSimhash(paper['content'])
    # print(t_file)
    papersObj[paper['sno']] = paper
    papersObj[paper['sno']]['content'] = paper['content']
    papersObj[paper['sno']]['simhash'] = tsimhash
    # print(targets)

# print( papersObj)
# 计算每篇文章和其他文章的相似度
cres = comparePaper(papersObj, req['distance'])
print(cres)
