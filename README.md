# -
基于Django2.2可重用登录与注册系统

具体实现步骤：原文地址：http://www.liujiangblog.com/course/django/102

环境：python3.5  Django2.2

开发流程

1、搭建项目环境
python3.5 Django2.2
创建项目以及APP
在settings文件中修改时区和语言
然后你就可以启动服务试一下啦
  
2、设计数据模型
login/models.py
数据库模型：
用户名
密码
邮箱地址
性别
创建时间
数据后端文件settings 默认使用SQLite
在settings中注册APP
创建记录和数据表
可以在pycharm的终端执行：
python manage.py makemigrations（数据迁移，创建模型）
python manage.py migrate（在数据库中创建真实的数据表）

  
3、admin后台
在admin中注册模型
在settings中注册APP（2中已完成）
在login/admin.py中注册模型
创建超级管理员->python manage.py createsuperuser
http://127.0.0.1:8000/admin/可进入管理页面
可以创建几个测试账号

4、url路由和视图
路由设计：
我们初步设想需要下面的四个URL：


URL   	         视图  	                  模板	            说明
/index/	    login.views.index	        index.html	          主页
/login/   	login.views.login	        login.html	          登录
/register/	login.views.register	    register.html	        注册
/logout/	  login.views.logout	      无需专门的页面	        登出

说明：由于本项目目的是打造一个针对管理系统、应用程序等需求下的可重用的登录/注册app，而不是门户网站、免费博客等无需登录即可访问的网站，所以在url路由、跳转策略和文件结构的设计上都是尽量自成体系。具体访问的策略如下：

未登录人员，不论是访问index还是login和logout，全部跳转到login界面
已登录人员，访问login会自动跳转到index页面
已登录人员，不允许直接访问register页面，需先logout
登出后，自动跳转到login界面

根据策划，修改register_and_sign_in/urls.py

架构初步视图：
路由写好了，就进入login/views.py文件编写视图的框架
创建HTML页面文件：
在login/templates/login目录中创建三个文件index.html、login.html以及register.html

测试路由和视图：
启动服务器，在浏览器访问http://127.0.0.1:8000/index/等页面，如果能正常显示，说明一切OK！

5、前端页面设计
使用原生HTML页面
引入Bootstrap 4
  注意：此次引入的是4版本，与3有一定的差异
添加静态文件：
/login/static/login目录下创建一个css和一个image目录，css中添加我们为登录视图写的css文件，这里是login.css，image目录中，拷贝进来你想要的背景图片，这里是bg.jpg

6、登录视图
login/views.py
如果出现CSRF验证失败的错误，我们需要在前端页面的form表单内添加一个{% csrf_token %}标签
可添加提示信息

7、Django表单
Django在内部集成了一个表单功能，以面向对象的方式，直接使用Python代码生成HTML表单代码，专门帮助我们快速处理表单相关的内容。

Django的表单给我们提供了下面三个主要功能：

  准备和重构数据用于页面渲染；
  为数据创建HTML表单元素；
  接收和处理用户从表单发送过来的数据。
创建表单模型
  在项目根目录的login文件夹下，新建一个forms.py文件，也就是/login/forms.py
修改视图-views.py
  使用了Django的表单后，就要在视图中进行相应的修改
修改login页面
  Django的表单很重要的一个功能就是自动生成HTML的form表单内容
手动渲染表单字段

8、图片验证码
为了防止机器人频繁登录网站或者破坏分子恶意登录，很多用户登录和注册系统都提供了图形验证码功能。

9、session会话
  保存数据

10、 注册视图
  注册功能
  密码加密
  
11、使用Django发送邮件
  注意，如果提示邮箱访问错误，可能是没有打开smtp服务，去邮箱设置中打开
12、邮件注册确认
