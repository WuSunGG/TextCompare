FROM registry.cn-chengdu.aliyuncs.com/sunwu/centos7_py36_sqlite3.33_commontools:v0.0.2
RUN pip install Django -i https://pypi.tuna.tsinghua.edu.cn/simple/&&\
    pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple/&&\
    pip install keras -i https://pypi.tuna.tsinghua.edu.cn/simple/&&\
    pip install tensorflow  -i https://pypi.tuna.tsinghua.edu.cn/simple/&&\
    pip install python-docx -i https://pypi.tuna.tsinghua.edu.cn/simple/&&\
    pip install BeautifulSoup4 -i https://pypi.tuna.tsinghua.edu.cn/simple/&&\
    pip install pytest
RUN pip install jieba

RUN mkdir /application
WORKDIR /application
ENV LD_LIBRARY_PATH=/usr/local/lib
RUN git clone https://github.com/WuSunGG/TextCompare
WORKDIR /application/TextCompare
RUN chmod +x runserver.sh
EXPOSE 8000
ENTRYPOINT /application/TextCompare/runserver.sh