# linux day03 作业



1.配置好阿里云yum源，下载redis软件，然后启动redis，访问redis数据库

```
yum install redis 
systemctl start redis 
netstat -tounlp | grep redis  # 查看是否开启
redis-server /etc/redis.conf # 启动
redis-cli shutdown # 关闭
```



2.linux的超级用户是什么？如何查看用户身份信息？

```
超级用户 root 
$ 普通用户
# 超级管理员

id   whoami

```



3.inux有哪些用户身份？

```
超级管理员root
普通用户
-------
在Linux系统中，用户也有自己的UID身份账号且唯一
系统管理员UID为0
系统用户UID为1~999    Linux安装的服务程序都会创建独有的用户负责运行。
普通用户UID从1000开始：由管理员创建
```



4.如何创建普通用户，并且修改用户密码，然后使用普通用户登录

```
useradd user
passwd user 
ssh ip 
su - root
```



5.在linux下如何切换用户

```
su命令可以切换用户身份的需求，
su - username
#先看下当前用户（我是谁）
whoami
#切换用户
su - oldboy
#退出用户登录
logout
ctrl + d
```



6.如何使用root身份执行普通用户的命令?请详细说明配置步骤

```
sudo ls /root
(修改配置文件  visudo)
```



7.简述linux文件的权限有哪些？  

```
读    4   r
写    2   w
执行  1   x 
```



8.linux文件权限的755，700是什么意思？

```
       755      700
用户  读写执行   读写执行
属组  读-执行	---
其他  读-执行    ---
```





9.如何修改test.py文件权限为700

```
chmod 700 test.py
```



10.如何修改test.py属组是oldboy?

```
chown root:oldboy test.py
chgrp oldboy test.py
```



11.已知test.py文件权限是rwxr--r--，如何修改权限为rw-rw-rw

```
chmod 666 test.py 
```



12.linux如何建立软连接？

```
ln -s 原文件(创建链接的文件) 快捷文件
ln -s /opt/zhangqihang/lihua.py  lihuadashuaige.py
ln -s /opt/python36/bin/python3  /usr/bin/python3
ln -s /opt/python36/bin/pip3  /usr/bin/pip3
```



13.centos7用什么命令管理服务，只有通过yum安装的软件才可以使用systemctl

````
systemctl start 服务
systemctl stop 服务
systemctl restart 服务
systemctl status 服务 
````



14.linux解析dns的命令是什么？

```
用来将域名解析为IP
nslookup
nslookup www.baidu.com
```



15.linux的/etc/hosts文件作用是？

```
本地强制dns解析文件 /etc/hosts
本地主机解析
```



16.将/tmp/下所有内容压缩成All_log.tar.gz并且放到/home/下

```
tar -zcf  all_log.tar.gz  /tmp/*
mv all_log.tar.gz /home/    -------------------------
tar -zxfv all_log.tar.gz 
```



17.解压缩Python源码包Python-3.7.0b3.tgz

```
tar -zxfv Python-3.7.0b3.tgz
```



18.查看mysql端口状态,查看redis端口状态

```
netstat -tounlp | grep redis
netstat -tounlp | grep mysql
```



19.如何查看nginx的进程

```
systemctl status nginx 
ps -ef |grep nginx
```



20.如何杀死nginx进程

```
kill 10637 (nginx id)

```



21.如何统计/var/log大小

```
du -sh /var/log
df -sh  (磁盘大小)
```



22.每月的,5,15,25天的晚上5点50重启nginx

```
crontab -e 
50 17 5,15,25 * * systemctl restart nginx
```



23.每周3到周5的深夜11点，备份/var/log /vmtp/

```
crontab -e 
0 23 * * 3-5 cp -r /var/log  /vmtp/
```



24.每天早上6.30清空/tmp/内容

```
30 6 * * * echo > /tmp/
30 6 * * * rm -rf /tmp/
```



25.每个星期三的下午6点到8点的第5，15分钟执行命令 command

```
5,15 18-20 * * 3 command 
```

