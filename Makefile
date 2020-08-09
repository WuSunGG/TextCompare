#!/usr/bin/make
repo :=registry.cn-chengdu.aliyuncs.com/sunwu
name :=arktao.textcompare
version := v0.1.11
sshport :=30152
bldf :
	docker build -t ${repo}/${name}:${version} -f $(MF)
t:
	docker build -f Dockerfiletest -t ${repo}/${name}:${version} .

v :
	@echo "version ${name}:${version}"

rmi:
	docker rmi -f ${name}:${version}

run:
	docker run  -p ${sshport}:8000  -itd --privileged  --name ${name}${version} ${repo}/${name}:${version}

del:
	docker rm -f ${name}${version}

e:
	docker exec -it ${name}${version} bash

bld :
	docker build -t ${repo}/${name}:${version} .

push:
#	docker push  --disable-content-trust  ${repo}/${name}:${version}
	docker push ${repo}/${name}:${version}

login:
	docker login --username=at2133n4o@aliyun.com registry.cn-chengdu.aliyuncs.com
pull:
	docker pull registry.cn-chengdu.aliyuncs.com/sunwu/acmis_hadoop:${version}
pre:
	yum install -y openssh-clients.x86_64

logs:
	docker logs ${name}${version}

rb:del bld run e

nb:bld run e



# 实验室
newname :=spark
newrepo :=registry.cn-chengdu.aliyuncs.com/idis-edu/
ilogin:
	#sudo docker login --username=daizyu registry.cn-hangzhou.aliyuncs.com
	sudo docker login --username=daizyu registry.cn-chengdu.aliyuncs.com
itag:
	docker tag ${repo}/${name}:${version}  ${newrepo}${newname}:${version}
ipush: itag
	docker push ${newrepo}${newname}:${version}
