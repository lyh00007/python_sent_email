#李懿恒的python
# 读取文档内容
#清除文档里面的空白行
with open("xingce.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# 删除空白行
lines = [line.strip() for line in lines if line.strip()]

# 将修改后的内容写回文档
with open("xingce.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(lines))
