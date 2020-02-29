# # 添加文件 emailSender.py
# import smtplib
# import datetime
# from email.mime.text import MIMEText
 
 
# class EmailSender(object):
#     def __init__(self):
#         self.smtp_host = "smtp.qq.com"  # 发送邮件的smtp服务器（从QQ邮箱中取得）
#         self.smtp_user = "1598902968@qq.com"  # 用于登录smtp服务器的用户名，也就是发送者的邮箱
#         self.smtp_pwd = "enflodemhqcthahg"  # 授权码，和用户名user一起，用于登录smtp， 非邮箱密码
#         self.smtp_port = 465  # smtp服务器SSL端口号，默认是465
#         self.sender = "1598902968@qq.com"  # 发送方的邮箱
 
#     def send_email(self, toLst, subject, body):
#         '''
#         发送邮件
#         :param toLst: 收件人的邮箱列表["123456@qq.com", "987654@qq.com"]
#         :param subject: 邮件标题
#         :param body: 邮件内容
#         :return:
#         '''
#         message = MIMEText(body, 'plain', 'utf-8')  # 邮件内容，格式，编码
#         message['From'] = self.sender               # 发件人
#         message['To'] = ",".join(toLst)             # 收件人列表
#         message['Subject'] = subject                # 邮件标题
#         att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
#         att1["Content-Type"] = 'application/octet-stream'
#         att1["Content-Disposition"] = 'attachment; filename="test.txt"'
#         message.attach(att1)
# 		# 构造附件1，传送当前目录下的 test.txt 文件

		
		
# 		# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
		

#         try:
#             smtpSSLClient = smtplib.SMTP_SSL(self.smtp_host, self.smtp_port)   # 实例化一个SMTP_SSL对象
#             loginRes = smtpSSLClient.login(self.smtp_user, self.smtp_pwd)      # 登录smtp服务器
#             print(f"登录结果：loginRes = {loginRes}")    # loginRes = (235, b'Authentication successful')
#             if loginRes and loginRes[0] == 235:
#                 print(f"登录成功，code = {loginRes[0]}")
#                 smtpSSLClient.sendmail(self.sender, toLst, message.as_string())
#                 print(f"mail has been send successfully. message:{message.as_string()}")
#                 smtpSSLClient.quit()
#             else:
#                 print(f"登陆失败，code = {loginRes[0]}")
#         except Exception as e:
#             print(f"发送失败，Exception: e={e}")
 
# email = EmailSender()
# toSendEmailLst = ['2460670348@qq.com']
# finishTime = datetime.datetime.now()
# subject = f"我是标题, finishedTime = {finishTime}"
# body = "我是内容。。。"
# email.send_email(toSendEmailLst, subject, body)

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
 
def send_email(smtpHost = 'smtp.qq.com', sendAddr = '2460670348@qq.com', password = 'irwnugkktslbebce', recipientAddrs = '1598902968@qq.com', subject='', content=''):
    ''''smtp.qq.com', '2460670348@qq.com', 'irwnugkktslbebce', '1598902968@qq.com'
    :param smtpHost: 域名
    :param sendAddr: 发送邮箱
    :param password: 邮箱密码
    :param recipientAddrs: 发送地址
    :param subject: 标题
    :param content: 内容
    :return: 无
    '''
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = sendAddr
    msg['to'] = recipientAddrs
    msg['subject'] = subject
    content = content
    txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)
 
    # 添加附件地址
    part = MIMEApplication(open(r'D:\CS\Python\practice\test.txt', 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="111.txt")  # 发送文件名称
    msg.attach(part)
 
    smtp = smtplib.SMTP()
    smtp.connect(smtpHost, '25')
    smtp.login(sendAddr, password)
    smtp.sendmail(sendAddr, recipientAddrs, str(msg))
    print("发送成功！")
    smtp.quit()


def main():
	try:
	    subject = 'Python 测试邮件'
	    content = '这是一封来自 Python 编写的测试邮件。'
	    send_email(recipientAddrs = '1598902968@qq.com', subject = subject, content = content)
	except Exception as err:
	    print(err)

if __name__ == '__main__':
	main()