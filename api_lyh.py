import random
import requests
import http.client, urllib, json
import smtplib
from datetime import datetime


def wyy():
    url = "https://apis.tianapi.com/hotreview/index?key=a65cc4f58f52e08fd68e89d2026afac9"
    r=requests.get(url)
    content=json.loads(r.text)
    text1 = content['result']['content']
    result = content['result']['source']
    over="网易云用户 "+result+"在评论区说的:\n"+text1
    return over

def history():
    url = "https://apis.tianapi.com/douyinhot/index?key=a65cc4f58f52e08fd68e89d2026afac9"
    r = requests.get(url)
    content = json.loads(r.text)
    result = content['result']['list']


# 遍历数据列表并打印每一项
    for item in result:
        hotindex = item['hotindex']
        label = item['label']
        word = item['word']
        #print(f"{word}\n")
    return word

def dog():
    url = "https://apis.tianapi.com/tiangou/index?key=a65cc4f58f52e08fd68e89d2026afac9"
    r=requests.get(url)
    content=json.loads(r.text)
    result = content['result']['content']
    return result

def rainbow_fart():
    url = "https://apis.tianapi.com/caihongpi/index?key=a65cc4f58f52e08fd68e89d2026afac9"
    r=requests.get(url)
    content=json.loads(r.text)
    result = content['result']['content']
    return result

def list():
    with open("xingce.txt", "r", encoding="utf-8") as file:
        numbers_content = file.read()
    # 将数字内容分割为列表，保持原始顺序
        numbers_list = numbers_content.split(",")

    # 从数字列表中随机选择五个不同的序号内容
        random_samples = random.sample(numbers_list, 10)          #这里设置发送题目的个数
        numbers_list = [element.strip() for element in numbers_content.split(".")]
        #print(random_samples)
    # 输出随机选择的序号内容
    """for sample in random_samples:
        print(sample)
    for sample in random_samples:
        stripped_sample = sample.strip()
        if stripped_sample:
            print(stripped_sample)   """
    # 创建一个空列表来存储五个值
    end1 = []

    # 将每个 sample 值添加到 end1 列表中
    for sample in random_samples:
        end1.append(sample)
    return end1

    # 返回包含五个值的列表

def content_input(content):
    # 提取信息
    province = content['lives'][0]['province']
    city = content['lives'][0]['city']
    temperature = content['lives'][0]['temperature']    # 实时气温，单位：摄氏度
    weather = content["lives"][0]['weather']        # 天气现象（汉字描述）
    reporttime = content["lives"][0]["reporttime"]      # 数据发布的时间

    return province, city, temperature, weather, reporttime

def tianqi():

    # 替换为您的API密钥
    api_key = "5993a4d824ca12e2ce71734dfb2a3073"

    # 替换为您要查询的城市的adcode（行政区划代码）
    adcodes = ["440114", "440204", "441402"]  # 广州花都、韶关浈江、梅州梅江

    # 存储天气信息的列表
    weather_info_list = []

    for adcode in adcodes:
        # 构建API请求URL
        url = f"https://restapi.amap.com/v3/weather/weatherInfo?key={api_key}&city={adcode}"

        # 发送GET请求
        r = requests.get(url)

        # 解析JSON响应
        content = json.loads(r.text)

        # 调用content_input函数来提取天气信息
        province, city, temperature, weather, reporttime = content_input(content)

        # 将天气信息添加到列表中
        weather_info_list.append(f"当前{province}{city}的天气是{weather}，温度是{temperature}摄氏度，数据发布于{reporttime}")

    # 返回包含多个城市天气信息的列表
    return weather_info_list   #0花都，1浈江，2梅江

def Curriculum():
    # 定义中文星期几的名称列表
    chinese_weekdays = ["非常痛苦星期一", "一般痛苦星期二", "痛苦星期三", "疯狂星期四", "明天放假星期五", "快乐星期六", "快乐星期日"]

    # 获取当前日期
    now = datetime.now()

    # 获取当前日期的星期几的索引（0 表示星期一，1 表示星期二，以此类推）
    weekday_index = now.weekday()

    # 使用索引从中文星期几名称列表中获取中文星期几
    chinese_weekday = chinese_weekdays[weekday_index]


# 使用 strftime 方法将日期格式化为英文星期几的字符串
    weekday = now.strftime("%A")  # 输出英文格式星期几如Thursday

    chinese_weekday = chinese_weekday   #中文的星期几
    today = weekday  # 当前日期
    no_classes = "不关你事，玩去吧!"
    class_schedule = {
        "lyh":{
    "Monday": [
        {"time": "08:00 AM - 9:40  AM" ,"address":"",  "course": no_classes},
        {"time": "10:00 AM - 11:40 PM","address":"", "course": no_classes},
        {"time": "14:40 PM - 16:20 PM","address":"", "course": no_classes},
        {"time": "16:30 PM - 18:00 PM","address":"", "course": no_classes},
        {"time": "19:30 PM - 21:10 PM","address":"", "course": no_classes},
    ],
    "Tuesday": [
        {"time": "08:00 AM - 9:40  AM","address":"北二-505", "course": "人工智能基础"},
        {"time": "10:00 AM - 11:40 PM","address":"南一-C405", "course": "电磁场与电磁波"},
        {"time": "14:40 PM - 16:20 PM","address":"", "course": no_classes},
        {"time": "16:30 PM - 18:00 PM","address":"", "course": no_classes},
        {"time": "19:30 PM - 21:10 PM","address":"南二-A302", "course": "计算机网络"},
    ],
    "Wednesday": [
        {"time": "08:00 AM - 9:40  AM","address":"北二-505", "course": "人工智能基础"},
        {"time": "10:00 AM - 11:40 PM","address":"", "course": no_classes},
        {"time": "14:40 PM - 16:20 PM","address":"", "course": no_classes},
        {"time": "16:30 PM - 18:00 PM","address":"", "course": no_classes},
        {"time": "19:30 PM - 21:10 PM","address":"", "course": no_classes},
    ],
    "Thursday": [
        {"time": "08:00 AM - 9:40  AM","address":"信工楼-(321-322)", "course":  "智能识别技术原理与应用"},
        {"time": "10:00 AM - 11:40 PM","address":"信工楼-(321-322)", "course": "智能识别技术原理与应用"},
        {"time": "14:40 PM - 16:20 PM","address":"北2-501", "course": "计算机网络"},
        {"time": "16:30 PM - 18:00 PM","address":"", "course": no_classes},
        {"time": "19:30 PM - 21:10 PM","address":"", "course": no_classes},
    ],
    "Friday": [
        {"time": "08:00 AM - 9:40  AM","address":"", "course":  no_classes},
        {"time": "10:00 AM - 11:40 PM","address":"", "course": no_classes},
        {"time": "14:40 PM - 16:20 PM","address":"南一-C405", "course": "电磁场与电磁波"},
        {"time": "16:30 PM - 18:00 PM","address":"", "course": no_classes},
        {"time": "19:30 PM - 21:10 PM","address":"", "course": no_classes},
    ],
    "Saturday": [
        {"time": "08:00 AM - 9:40  AM","address":"", "course": no_classes},
        {"time": "10:00 AM - 11:40 PM","address":"", "course": no_classes},
        {"time": "14:40 PM - 16:20 PM","address":"", "course": no_classes},
        {"time": "16:30 PM - 18:00 PM","address":"", "course": no_classes},
        {"time": "19:30 PM - 21:10 PM","address":"", "course": no_classes},
    ],
    "Sunday": [
        {"time": "08:00 AM - 9:40  AM","address":"", "course": no_classes},
        {"time": "10:00 AM - 11:40 PM","address":"", "course": no_classes},
        {"time": "14:40 PM - 16:20 PM","address":"", "course": no_classes},
        {"time": "16:30 PM - 18:00 PM","address":"", "course": no_classes},
        {"time": "19:30 PM - 21:10 PM","address":"", "course": no_classes},
    ],
        },

    "hzh":{
    "Monday": [
        {"time": "08:00 AM - 9:40  AM" ,"address":"锡科楼604",  "course":"临床基础检验技术"},
        {"time": "10:00 AM - 11:40 PM","address":"锡科楼404", "course": "临床输血与检验"},
        {"time": "14:40 PM - 16:20 PM","address":"锡科楼604", "course": "临床分子生物学检验技"},
        {"time": "16:30 PM - 18:00 PM","address":"", "course": no_classes},
        {"time": "19:30 PM - 21:10 PM","address":"", "course": no_classes},
    ],
    "Tuesday": [
        {"time": "08:00 AM - 9:40  AM","address":"锡科楼602", "course": "临床分子生物学检验技术"},
        {"time": "10:00 AM - 11:40 PM","address":"双周有课", "course": "临床分子生物学检验技术"},
        {"time": "14:40 PM - 16:20 PM","address":"锡科楼404", "course": "医学检验仪器学"},
        {"time": "16:30 PM - 18:00 PM","address":"锡科楼404", "course": "卫生理化检验"},
        {"time": "19:30 PM - 21:10 PM","address":"", "course": no_classes},
    ],
    "Wednesday": [
        {"time": "08:00 AM - 9:40  AM","address":"锡科楼602", "course": "临床微生物学检验技术"},
        {"time": "10:00 AM - 11:40 PM","address":"", "course": no_classes},
        {"time": "14:40 PM - 16:20 PM","address":"", "course": no_classes},
        {"time": "16:30 PM - 18:00 PM","address":"", "course": no_classes},
        {"time": "19:30 PM - 21:10 PM","address":"", "course": no_classes},
    ],
    "Thursday": [
        {"time": "08:00 AM - 9:40  AM","address":"锡科楼604", "course":  "临床基础检验技术"},
        {"time": "10:00 AM - 11:40 PM(1--3节)","address":"锡科楼604", "course": "临床基础检验技术"},
        {"time": "14:40 PM - 16:20 PM","address":"锡科楼602", "course": "临床微生物学检验技术"},
        {"time": "16:30 PM - 18:00 PM","address":"", "course": no_classes},
        {"time": "19:30 PM - 21:10 PM","address":"", "course": no_classes},
    ],
    "Friday": [
        {"time": "08:00 AM - 9:40  AM","address":"锡科楼604", "course": "临床基础檢验技术"},
        {"time": "10:00 AM - 11:40 PM","address":"锡科楼602", "course": "临床微生物学检验技术"},
        {"time": "14:40 PM - 16:20 PM","address":"锡科楼404", "course": "临床实验室质量控制与管理"},
        {"time": "16:30 PM - 18:00 PM","address":"", "course": no_classes},
        {"time": "19:30 PM - 21:10 PM","address":"", "course": no_classes},
    ],
    "Saturday": [
        {"time": "08:00 AM - 9:40  AM","address":"", "course": no_classes},
        {"time": "10:00 AM - 11:40 PM","address":"", "course": no_classes},
        {"time": "14:40 PM - 16:20 PM","address":"", "course": no_classes},
        {"time": "16:30 PM - 18:00 PM","address":"", "course": no_classes},
        {"time": "19:30 PM - 21:10 PM","address":"", "course": no_classes},
    ],
    "Sunday": [
        {"time": "08:00 AM - 9:40  AM","address":"", "course": no_classes},
        {"time": "10:00 AM - 11:40 PM","address":"", "course": no_classes},
        {"time": "14:40 PM - 16:20 PM","address":"", "course": no_classes},
        {"time": "16:30 PM - 18:00 PM","address":"", "course": no_classes},
        {"time": "19:30 PM - 21:10 PM","address":"", "course": no_classes},
    ],

    # 添加其他日期的课程和时间
},


}

    lyh_schedule = class_schedule["lyh"]
    hzh_schedule = class_schedule["hzh"]

    today_lyhschedule = lyh_schedule[today]
    today_hzhschedule = hzh_schedule[today]

    today_hzh = today
    today_lyh = today
    # 构建邮件正文内容
    for class_info in today_lyhschedule:
        time = class_info["time"]
        course = class_info["course"]
        address = class_info["address"]
        class_info_str = f"\n时间：{time} \n地点：{address} \n课程：{course}\n"
        today_lyh += class_info_str

    for class_info in today_hzhschedule:
        time = class_info["time"]
        course = class_info["course"]
        address = class_info["address"]
        class_info_str = f"\n时间：{time} \n地点：{address} \n课程：{course}\n"
        today_hzh += class_info_str

    body_hzh = f"请查看{chinese_weekday}的课表{today_hzh}"
    body_lyh = f"请查看{chinese_weekday}的课表{today_lyh}"
    return body_lyh,body_hzh

