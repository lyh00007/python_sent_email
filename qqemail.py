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
        print(f"{receiver_email}邮件发送成功")
    except Exception as e:
        print(f"邮件发送失败给{receiver_email}: {e}")

if __name__ == '__main__':
    sender_email = "1612061987@qq.com"
    app_password = "fmgrfgnnfqwscfif"

    receivers = {#13922813448@163.com
        "tsy": ["934779790@qq.com"],#,"1612061987@qq.com"
        "hzh": ["hzh13714645712@163.com"],#,"1612061987@qq.com"
        "lyh": ["1612061987@qq.com","2953265769@qq.com"],#
        "zyt": ["1836535514@qq.com"]  #"1612061987@qq.com","13922813448@163.com"
    }

    subject_names = ["tsy", "hzh", "lyh", "zyt"]
    subjects = {name: api_lyh.rainbow_fart() for name in subject_names}


    body_lines = {
        "tsy": [
            f"当前天气温馨提示：{api_lyh.tianqi()[0]}",
            "要好好学习才是乖宝宝",
            "\n".join(api_lyh.list())
        ],
        "lyh": [
            f"当前天气温馨提示：{api_lyh.tianqi()[1]}",
            "出门记得检查垃圾袋",
            api_lyh.Curriculum()[0],
            f"今日舔狗:\n{api_lyh.dog()}\n",
            api_lyh.wyy()
        ],
        "hzh": [
            f"当前天气温馨提示：{api_lyh.tianqi()[2]}",
            "你个傻杯能不能好好学习",
            api_lyh.Curriculum()[1],
            f"今日舔狗:\n{api_lyh.dog()}\n",
            api_lyh.wyy()
        ],
        "zyt": [
            f"当前天气温馨提示：{api_lyh.tianqi()[1]}",
            "你个傻杯能不能好好学习",
            api_lyh.Curriculum()[2],
            f"今日舔狗:\n{api_lyh.dog()}\n",
            api_lyh.wyy()
        ]
    }

    for name in receivers:
        for receiver_email in receivers[name]:
            send_email(sender_email, app_password, receiver_email, subjects[name], body_lines[name])