# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

# 通过邮件给单个对象发消息
def send_mail(mail_username, mail_password, mail_host, receiver, text, subject, receiver_name, sender_name):
    flag = True
    interval = 0
    while(flag):
        try:
            message = MIMEText(text, 'plain', 'utf-8')
            message['From'] = Header(sender_name, 'utf-8')
            message['To'] = Header(receiver_name, 'utf-8')
            message['Subject'] = Header(subject, 'utf-8')

            smtpObj = smtplib.SMTP_SSL(mail_host, 465)    # 25 为 SMTP 端口号 465是SMTP over SSL
            # print('login')
            smtpObj.login(mail_username, mail_password)
            # print('send')
            smtpObj.sendmail(mail_username, [receiver], message.as_string())
            print('successfully send mail to ', receiver_name)
            flag = False
        except smtplib.SMTPException:
            print('send mail failed to ', receiver_name)
            if(interval>5):
                print('all sending to ', receiver_name, ' trails failed')
                break
            time.sleep(2**interval)
            interval += 1
