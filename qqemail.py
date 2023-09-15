# -*- coding: utf-8 -*-
import requests
import http.client, urllib, json
import smtplib
import api_lyh
import re
import random
import chardet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_email_body(subject, body_lines):
    body = "\n".join(map(str, body_lines))
    return subject, body

def send_email(sender_email, app_password, receiver_emails, subject, body_lines):
    subject, body = get_email_body(subject, body_lines)

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = ", ".join(receiver_emails)
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        smtp_server = "smtp.qq.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_emails, message.as_string())
        server.quit()
        print(f"{sender_email}邮件发送成功")
    except Exception as e:
        print(f"邮件发送失败: {e}")

if __name__ == '__main__':
    sender_email = "1612061987@qq.com"
    app_password = "fmgrfgnnfqwscfif"
    receiver_emails_tsy = ["934779790@qq.com","1612061987@qq.com"]
    receiver_emails_hzh = ["hzh13714645712@163.com"]
    receiver_emails_lyh = ["1612061987@qq.com","2953265769@qq.com"]

    subject_tsy = api_lyh.rainbow_fart()
    subject_hzh = api_lyh.rainbow_fart()
    subject_lyh = api_lyh.rainbow_fart()

    body_lines_tsy = [
        "当前天气温馨提示：" + api_lyh.tianqi()[0],
        "要好好学习才是乖宝宝",
        "\n".join(api_lyh.list()),  # 将列表转换为字符串
        "想对姐姐说的话:\n" + api_lyh.dog(),
        api_lyh.wyy()
    ]

    body_lines_hzh = [
        "当前天气温馨提示：" + api_lyh.tianqi()[2],
        "你个傻杯能不能好好学习",
        api_lyh.Curriculum()[1],
        "今日舔狗:\n" + api_lyh.dog(),
        api_lyh.wyy()
    ]
    body_lines_lyh = [
        "当前天气温馨提示：" + api_lyh.tianqi()[1],
        "出门记得检查垃圾袋",
        api_lyh.Curriculum()[0],
        "今日舔狗:\n" + api_lyh.dog(),
        api_lyh.wyy()
    ]
    send_email(sender_email, app_password, receiver_emails_tsy, subject_tsy, body_lines_tsy)
    send_email(sender_email, app_password, receiver_emails_hzh, subject_hzh, body_lines_hzh)
    send_email(sender_email, app_password, receiver_emails_lyh, subject_lyh, body_lines_lyh)
