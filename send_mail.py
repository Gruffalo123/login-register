#第一种：在Django中发送邮件

# import os
# from django.core.mail import send_mail
##register_and_sign_in项目名称
# os.environ['DJANGO_SETTINGS_MODULE'] = 'register_and_sign_in.settings'
#
# if __name__ == '__main__':
#
#     send_mail(
#         '来自www.xxx.com的测试邮件',  #主题
#         '欢迎访问www.xxx.com',        #邮件具体内容
#         'xxx@sina.com',               #邮件发送方
#         ['xxx@qq.com'],               #接收方
#     )



#第二种：发送HTML格式的邮件，删除一测试二
import os
from django.core.mail import EmailMultiAlternatives
os.environ['DJANGO_SETTINGS_MODULE'] = 'register_and_sign_in.settings'

if __name__ == '__main__':

    subject,from_email,to = '来自www.xxx.com的测试邮件','xxx@sina.com','xxx@qq.com'
    test_content = '欢迎访问xxx.xxx.xxx'
    html_content = '<p>欢迎访问<a href="http://xxx.xxx.xxx" target=blank>www.xxx.com</p>'
    msg = EmailMultiAlternatives(subject,test_content,from_email,[to])
    msg.attach_alternative(html_content,"text/html")
    msg.send()

# 这个send_mail.py文件只是一个测试脚本，使用完毕后可以从项目里删除。