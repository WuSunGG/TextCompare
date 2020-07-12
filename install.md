wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install Django
python -m django --version
django-admin startproject textsim
python manage.py runserver 0:8000

## SQLite 3.8.3 or later is required (found %s).' % Database.sqlite_version
https://blog.csdn.net/lee006006/article/details/90444473
wget https://www.sqlite.org/snapshot/sqlite-snapshot-202007061213.tar.gz
tar zxvf sqlite-autoconf-3300100.tar.gz
cd sqlite-autoconf-3300100/
./configure
make & make install


mv /usr/bin/sqlite3  /usr/bin/sqlite3_old
ln -s /usr/local/bin/sqlite3   /usr/bin/sqlite3
echo  export LD_LIBRARY_PATH=/usr/local/lib >> /etc/profile && source /etc/profile
python manage.py runserver 0:8000

Django
 https://docs.djangoproject.com/zh-hans/2.0/intro/

 ## You may need to add '192.168.184.129' to ALLOWED_HOSTS.
 D:\NLP\textsim\settings.py
 ALLOWED_HOSTS = ["*"]


 python manage.py startapp simhash
 python manage.py startapp picpre
 
 http://192.168.184.129:8000/simhash/
 
 
 ## Django出错提示TemplateDoesNotExist at /
  D:\NLP\textsim\settings.py
'DIRS': [os.path.join(BASE_DIR, 'templates')],




## No module named 'matplotlib'
清华大学镜像
https://pypi.tuna.tsinghua.edu.cn/simple/
阿里云
http://mirrors.aliyun.com/pypi/simple/
中科大镜像
https://pypi.mirrors.ustc.edu.cn/simple/
豆瓣镜像
http://pypi.douban.com/simple/
中科大镜像2
http://pypi.mirrors.ustc.edu.cn/simple/

pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install keras -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install tensorflow  -i https://pypi.tuna.tsinghua.edu.cn/simple/
