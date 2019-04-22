from django.db import models

# Create your models here.
class User(models.Model):

    #定义性别选项
    gender = (
        ('male',"男"),
        ('female',"女"),
    )

    #这里是注册用户名，不等同于人名，所以不能重复
    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length= 256)
    email = models.EmailField(unique=True)
    #性别choices = gender
    sex = models.CharField(max_length=32,choices=gender,default="男")
    create_time = models.DateTimeField(auto_now=True)

    #更加人性化显示对象信息
    def __str__(self):
        return self.name

    #元数据选项
    class Meta:

        #默认排序字段及排序方式，用于得到一个对象列表的任何场合，可选前缀'-'（降序）
        ordering = ["-create_time"]

        #是该对象的一个可读性更好的唯一名字
        verbose_name = "用户"

        #对象名字的复数
        verbose_name_plural = "用户"