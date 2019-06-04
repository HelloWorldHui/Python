## linux day02作业



1.简述linux的文档目录结构



![1132884-20180823103948862-1376998015](G:\PYTHON DAY\08 Linux\day114-linux基本命令\assets\1132884-20180823103948862-1376998015.png)

![1132884-20180921150307683-759085586](G:\PYTHON DAY\08 Linux\day114-linux基本命令\assets\1132884-20180921150307683-759085586.png)

2.递归创建文件夹/tmp/oldboy/python/{alex,wusir,nvshen,xiaofeng}

```
mkdir -p /tmp/oldboy/python/{alex,wusir,nvshen,xiaofeng}
```

3.显示/tmp/下所有内容详细信息

```
ls -la /tmp/
```



4.简述 / ~ - 的含义

```
/ 根目录
~ 当前用户家目录
- 上一次目录
```



5.请简述你如何使用vi命令

```
i 编辑
esc 退出编辑
:wq! 强制写入并退出
:w 写入
:q 推出

```



6.查看/etc/passwd的内容并且打印行号

```
cat -n /etc/passwd
```



7.查看文本有哪些命令？

```
cat 文本
less 文本
more 文本
head 
tail
```



8.如何用echo清空一个文件？

```
echo > 文件
```



9.复制/tmp/下所有内容到/home，(在修改文件前，先拷贝一份，防止内容被破坏)

```
cp -r /tmp/ /home/
```



10.重命名test.py为my.py

```
mv test.py my.py
```



11.强制删除/tmp下内容

```
rm -rf /tmp/*
```



12.找到服务器上的settings.py

```
find / -name settings.py
```



13.找到/etc下的网卡配置文件，提示网卡配置文件名是ifc开头

```
find /etc/ -name ifc*
```



14.过滤出/tmp/passwd下有关root的信息

提示：

先cat /etc/passwd > /tmp/passwd 生成一个passwd文件

```
cat /tmp/passwd | grep root
grep root /tmp/passwd
```



15.过滤出/tmp/passwd下除了/sbin/nologin的信息，且打印行号

```
cat /tmp/passwd | grep -vin /sbin/nologin
cat /tmp/passwd | grep -v -i -n /sbin/nologin
```



16.查看/tmp/passwd前25行

```
head -25 /tmp/passwd 
head -30 /tmp/passwd | tail -21 # 第10-30行(找出前30行过滤出尾部21行,10-30) 

```



17.查看/tmp/passwd后3行

```
tail -3 /tmp/passwd 
```



18.不间断打印/etc/lpasswd的信息

```
tail -f /var/log/py.log  
  # more /etc/passwd
```



19.替换/tmp/passwd中的所有root为ROOT

```
sed -i 's/root/ROOT/g' /tmp/passwd
cat 's/root/ROOT/' /tmp/passwd
```



20.用sed删除'/tmp/passwd'中的5,10行

```
sed -i '5,10d' /tmp/passwd
```



21.配置rm别名为“禁止你用rm，谢谢”，然后取消别名

```
alias rm="echo '禁用rm' "
unalias rm 
alias rm="rm -i"
```

22.将服务器1的/tmp/my.py远程传输到服务器2的/opt/目录下

````
scp  /tmp/my.py root@192.168.12.xx:/root/
````



23.将服务器2的/opt/test.py拷贝到服务器1的/home目录下

```
scp root@192.168.12.xx:/opt/test.py /home/
```



24.统计/etc/文件夹大小

```
du /etc/
du -s -h /etc/ #统计指定文件夹或文件大小
df -h # 统计磁盘大小和使用率
```



25.给settings.py加锁，禁止删除

```
chattr +a 文件  加锁
chattr -a 文件  解锁
lsattr 查看
```



26.从ntp.aliyun.com同步服务器时间

```
ntpdate -u ntp.aliyun.com

```



27.下载http://pythonav.cn/av/xiaobo.jpg资源

```
wget -r -p http://www.luffycity.com  # 递归下载路飞所有资源，保存到www.luffycity.com文件中
wget http://pythonav.cn/av/xiaobo.jpg
```

