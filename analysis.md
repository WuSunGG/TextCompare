# simhash  文本相似度计算方法
# 原文链接：https://blog.csdn.net/al_xin/java/article/details/38919361
# C++ 实现: https://github.com/yanyiwu/simhash
# Python实现：https://leons.im/posts/a-python-implementation-of-simhash-algorithm/
# 算法主要原理：
# 1、分词，把需要判断文本分词形成这个文章的特征单词。最后形成去掉噪音词的单词序列并为每个词加上权重，我们假设权重分为5个级别（1~5）。比如：“ 美国“51区”雇员称内部有9架飞碟，曾看见灰色外星人 ” ==> 分词后为 “ 美国（4） 51区（5） 雇员（3） 称（1） 内部（2） 有（1） 9架（3） 飞碟（5） 曾（1） 看见（3） 灰色（4） 外星人（5）”，括号里是代表单词在整个句子里重要程度，数字越大越重要。
# 2、hash，通过hash算法把每个词变成hash值，比如“美国”通过hash算法计算为 100101,“51区”通过hash算法计算为 101011。这样我们的字符串就变成了一串串数字，还记得文章开头说过的吗，要把文章变为数字计算才能提高相似度计算性能，现在是降维过程进行时。
# 3、加权，通过 2步骤的hash生成结果，需要按照单词的权重形成加权数字串，比如“美国”的hash值为“100101”，通过加权计算为“4 -4 -4 4 -4 4”；“51区”的hash值为“101011”，通过加权计算为 “ 5 -5 5 -5 5 5”。
# 4、合并，把上面各个单词算出来的序列值累加，变成只有一个序列串。比如 “美国”的 “4 -4 -4 4 -4 4”，“51区”的 “ 5 -5 5 -5 5 5”， 把每一位进行累加， “4+5 -4+-5 -4+5 4+-5 -4+5 4+5” ==》 “9 -9 1 -1 1 9”。这里作为示例只算了两个单词的，真实计算需要把所有单词的序列串累加。
# 5、降维，把4步算出来的 “9 -9 1 -1 1 9” 变成 0 1 串，形成我们最终的simhash签名。 如果每一位大于0 记为 1，小于0 记为 0。最后算出结果为：“1 0 1 0 1 1”。
# demo
# “你妈妈喊你回家吃饭哦，回家罗回家罗” 和 “你妈妈叫你回家吃饭啦，回家罗回家罗”。
# 通过simhash计算结果为：
# 1000010010101101111111100000101011010001001111100001001011001011
# 1000010010101101011111100000101011010001001111100001101010001011

import math
import jieba
import jieba.analyse

class SimHash(object):
    def __init__(self):
        pass

    def getBinStr(self, source):
        """
        将 原文本 转换为 二进制
        如 资源 转换为 0100000000111101100101001111110101101000101000010111010001011110
        :param source: 原文本
        :return:  二进制
        """
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** 128 - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            x = bin(x).replace('0b', '').zfill(64)[-64:]
            return str(x)

    def getWeight(self, source):
        # fake weight with keyword
        return ord(source)

    def unwrap_weight(self, arr):
        ret = ""
        for item in arr:
            tmp = 0
            if int(item) > 0:
                tmp = 1
            ret += str(tmp)
        return ret

    def hash(self, rawstr):
        """

        :param rawstr: 文本
        :return:
        """
        # 例子州道教育科技有限公司（ARKTAO）的一员是孙武同学。
        # 1 分词
        seg = jieba.cut(rawstr)

        # 文字关键词
        #  找到文章的关键词，词频解析为 （词语，权重）,如
        keywords = jieba.analyse.extract_tags("|".join(seg), topK=1000, withWeight=True)
        # RES:
        # 0 = {tuple: 2} ('ARKTAO', 1.7078239289857142)
        # 1 = {tuple: 2} ('孙武', 1.426950663792857)
        # 2 = {tuple: 2} ('一员', 1.1383474949328571)
        # 3 = {tuple: 2} ('同学', 1.0294450847785714)
        # 4 = {tuple: 2} ('科技', 0.8331820990585713)
        # 5 = {tuple: 2} ('教育', 0.8111989397285715)
        # 6 = {tuple: 2} ('有限公司', 0.7419558412757142)
        
        ret = []
        # keyword = '资源' weight = 0.26808614843899997
        for keyword, weight in keywords:
            # 2 hash
            binstr = self.getBinStr(keyword) # '0100000000111101100101001111110101101000101000010111010001011110'
            keylist = []

            # 3 加权
            for c in binstr:
                weight = math.ceil(weight)
                # 4 合并
                if c == "1":
                    keylist.append(int(weight))
                else:
                    keylist.append(-int(weight))
            ret.append(keylist)
        # 5 降维
        rows = len(ret)
        cols = len(ret[0])
        result = []
        for i in range(cols):
            tmp = 0
            for j in range(rows):
                tmp += int(ret[j][i])
            if tmp > 0:
                tmp = "1"
            elif tmp <= 0:
                tmp = "0"
            result.append(tmp)
        return "".join(result)

    def getDistince(self, hashstr1, hashstr2):
        """
        计算距离
        :param hashstr1: 第一个 simHash
        :param hashstr2: 第二个 simHash
        :return:
        """
        length = 0
        for index, char in enumerate(hashstr1):
            if char == hashstr2[index]:
                continue
            else:
                length += 1
        return length

# print(__name__)
## res __main__
if __name__ == "__main__":
    tx1="sdfsdf"
    tx2="sdfsdf"
    simhash=SimHash()
    hash1 = simhash.hash(tx1)
    hash2 = simhash.hash(tx2)
    distince = simhash.getDistince(hash1, hash2)
    value = 20
    res = "海明距离：" + str(distince) + " 判定距离：" + str(value) + " 是否相似 " + str(distince <= value)
    print(res)