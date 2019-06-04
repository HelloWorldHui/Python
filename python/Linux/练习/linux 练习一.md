linux day01作业

#### 1.服务器有哪些硬件?

  - CPU , CPUF风扇,内存,显卡,声卡,主板,网卡,电源,USB,硬盘

#### 2.内存，CPU，硬盘的作用?

- 内存:是CPU 和 磁盘之间的缓冲设备, 也叫临时存储器(存放数据),断电时数据消失

- CPU:主要判断与控制各个硬件的活动,(相当于人的脑袋)

- 硬盘: 用于CPU写入和读取,储存资料

#### 3.服务器常见品牌？

- DELL(常见)
- HP
- IBM(百度,银行,政府)
- 浪潮
- 联想

#### 4.linux优点?

- 软件支持: 大多开源软件

- 安全稳定

- 使用习惯: 兼具图形界面（需要带有桌面环境的发行版Linux）和完全命令行操作，无法使用鼠标，新手入门困难，需要学习后方可使用，熟练后效率极高！

- 应用领域广: 人们日常在Windows上访问的百度、谷歌、淘宝、qq、迅雷（xxxx大片），支撑这些软件运行的，后台是成千上万的Linux服务器，它们时时刻刻进行着忙碌的数据处理和运算

- ```
  使用linux的好处是自由传播，免费，不会犯法，任意切换图形/命令终端，安全稳定，不用杀毒软件，不卡
  ```

####  5.说出常见的linux发行版？

- Ubuntu(乌班图Linux桌面系统)
- Redhat(红帽) CentOS(服务端Linux系统)
- Debian或FreeBSD(安全可靠)
- SUSE(使用数据库或电子邮件网络用户,德国多)
- Fedora(新技术,新功能,是Redhat和CentOS的测试版)
- 红旗Linux和麒麟Linux(中文)

#### 6.如何远程连接服务器？远程连接服务器的命令是什么? xshell是什么？

- Xshell是一个强大的安全终端模拟软件,可以在Windows界面下访问远处不同系统下的服务器
- 链接服务器 ssh ip  / ssh root@ip

#### 7.简述linux下 -  ~   .   .. 的 含义

- "-" 前一个工作目录
- "~"当前[用户]的家目录
- . 当前目录
- .. 上一层目录

#### 8.打印当前工作目录的，绝对路径命令是？

```
pwd 当前文件目录
echo %PATH      (大写)
```



#### 9.简述linux文件目录结构?   10.简述linux根/目录下面各个文件的用途?



![1554953891057](assets/1554953891057.png)

 

#### 11.linux命令默写

​	(1)创建文件夹 onepiece

``` 
mkdir opepiece
```

​	(2)创建文本    onepiece.py

```
touch onepiece.pu
```

​	(3)绝对路径，相对路径

​		以绝对路径的写法，在/home/创建一个qishi.txt 

``` 
touch /home/qishi.txt
```

​		只要你写的路径，是从 /  根目录开始，就是一个绝对路径

​		在进入 /opt目录，以相对路径的方式，创建/qishi.txt  

```
cd /opt 
touch ./qishi.txt
```

​        (4)查看目录下的所有文件

```
ls 
```

​	(5)查看目录下的所有文件详情

```
ls -l
ls ll

```

​	(6)查看目录下的所有隐藏文件

``` 
ls -a
ls -la
ls -all
```



​	(7)查看文件夹内容     onepiece

```
less /
ls opepiece
```



​	(8)删除onepiece.py文件

```
rm -rf opepiece.py
```



​	(9)删除空文件夹/tmp/luffy/onepiece

```
rmdir /tmp/luffy/onepiece
rm -r /
```



13.练习绝对路径，相对路径

​    在/tmp/luffy/下，查看/opt/luffy/下的内容，两种方式

```
ls /opt/luffy/
ls ../../opt/luffy/
```

14. 复制,移动

```
cp xxx.py /tmp/  #移动到tmp目录下
cp xxx.py /tmp/tiger.py # 移动并改名
cp main.py main.py.bak  # 移动前备份
# 递归复制test文件夹，为test2
cp -r test test2

# 把老男孩从大学城搬到沙河旁边去
mv /home/shahe/oldboy /tmp/tencent

```

15 pwd 当前目录