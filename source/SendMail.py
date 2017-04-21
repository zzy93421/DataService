'''
Created on 2017年4月21日
本模块用于发送邮件
@author: zhangzhiyuan
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = 'zzy93421@zzy.com'
receivers = ['zzy93421@163.com']
message = MIMEMultipart()
message['From'] = Header("This is a test mail", "utf-8")
message['To'] = Header("测试", 'utf-8')
subject = "Python SMTP 邮件测试"
message['Subject'] = Header(subject, 'utf-8')

message.attach(MIMEText('这是一个测试邮件，邮件发送测试.....', 'plain', 'utf-8'))
att1 = MIMEText(open(r'D:\temp\浙江飞鱼查询工单.sql', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment;filename="test.txt"'
message.attach(att1)

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error:无法发送邮件")
