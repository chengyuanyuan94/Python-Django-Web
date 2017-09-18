###Python Django Web

## 一、环境搭建
- 知识补充： Python下有许多款不同的 Web 框架。Django是重量级选手中最有代表性的一位。许多成功的网站和APP都基于Django。
Django是一个开放源代码的Web应用框架，由Python写成。
- 环境：
	- Windows64+Python2.7
	- 配置环境变量（ps:cmd输入Python显示版本号即成功）
	![django.png](http://upload-images.jianshu.io/upload_images/2539401-bc88f1adde695b58.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
	- pip install django
	- 进入Python的script目录中，将django-admin.exe配置到环境变量中，cmd查看如下：
	![django.png](http://upload-images.jianshu.io/upload_images/2539401-f6966957c11db8c3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
	以上环境就搭建完成了……

## 二、创建Django项目
- 进入一个特定的目录下（此处d:/demo）
![django.png](http://upload-images.jianshu.io/upload_images/2539401-2dd9b5c5a2b895ed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- django-admin startproject testdemo
![django.png](http://upload-images.jianshu.io/upload_images/2539401-9ebbd18a9dce1632.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 进入项目里输入：python manage.py runserver
![django.png](http://upload-images.jianshu.io/upload_images/2539401-583f9b155ad302a0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 打开网页验证
-![django.png](http://upload-images.jianshu.io/upload_images/2539401-ab0afcbbb882cc2c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 三、网页展示
- 首页
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/2539401-b25bf70e2214fc09.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 文章列表
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/2539401-76d57fc19ec988fa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 文章详情
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/2539401-245896a4a221213f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 分页
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/2539401-2c639f5452bd884a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

好了，暂时先到这吧~
> 不懂得先自己找方法去解决，那样比问别人得到的答案更有意义……