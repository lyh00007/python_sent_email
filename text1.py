import time
import api_lyh

result = api_lyh.tianqi()
date = result[1]  # 当前日期

def Curriculum():
    # 获取今日日期，例如 Monday
    today = time.strftime("%A")

    # 课程表
    class_schedule = {
        "Monday": [
            {"time_week": "星期一"},
            {"time": "08:00 AM - 9:40 AM", "course": "Math"},
            {"time": "10:00 AM - 11:40 PM", "course": "History"},
            {"time": "14:40 PM - 16:20 PM", "course": "Science"},
            {"time": "16:30 PM - 18:00 PM", "course": "Science"},
            {"time": "16:30 PM - 18:00 PM", "course": "Science"},
            {"time": "19:30 PM - 21:10 PM", "course": "Science"},
        ],
        # 添加其他日期的课程和时间
    }

    # 获取今日课程安排
    if today in class_schedule:
        today_schedule = class_schedule[today]
    else:
        today_schedule = [{"time": "无课程安排", "course": ""}]

    # 构建邮件正文内容
    body = f"今天是{date} {today}，您的课程安排如下：\n\n"
    for class_info in today_schedule:
        time_info = class_info.get("time", "")
        course_info = class_info.get("course", "")
        class_info_str = f"时间：{time_info}\n课程：{course_info}\n\n"
        body += class_info_str

    print(body)
    return body

Curriculum()
