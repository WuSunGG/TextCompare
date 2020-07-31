from dev_SimHash import SimHash
# import  json
# res=json.dumps({'id':'1','list':[
#     {"a":'a1'},
#     {"b":'b1'},
#     {"c":'c1'},
# ]})
# # print(res)
# # str="./works/15软工-15-陈鸿.doc"
# # sindex=str.rfind("/")
# # endindex=str.rfind(".")
# # print(sindex,endindex)
# # print(str[sindex+1:endindex])
#
# data={'list':[
#     {"a":'a1'},
#     {"b":'b1'},
#     {"c":'c1'},
# ]}
#
from docx import Document
document = Document("./works/15软工-37-郑梦月.docx")
tx1 = ""
for paragraph in document.paragraphs:
    tx1 += paragraph.text + "\n"
print(tx1.splitlines())

import re
sentences = re.split('(。|！|\!|\.|？|\?|\n|，)', tx1)  # 保留分割符
#
new_sents = []
for i in range(int(len(sentences) / 2)):
    sent = sentences[2 * i] + sentences[2 * i + 1]
    new_sents.append(sent)
print(new_sents)