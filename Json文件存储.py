'''
读取JSON数据
'''
import json

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(str))
print(dir(str))
# 数据必须是双引号
data = json.loads(str)
print(data)
print(data[0]['name'])
# 添加默认值,当key不存在是显示值
print(data[0].get('name', '无'))

'''
读取本地json文件
'''
with open('json_data.json', 'r') as file:
    str = file.read()
    data = json.loads(str)
    print(data)

'''
输出JSON
'''

data = [{
    "key1": "value",
    "key2": "value",
    "key3": "value",
    "key4": "value"
}, {
    "key1": "张三",
    "key2": "李四",
    "key3": "王五",
    "key4": "麻六"
}]
with open('output_json_data.json', 'w') as file:
    # file.write(json.dumps(data))
    # 缩进字符
    # file.write(json.dumps(data, indent=2))
    # 解决中文乱码
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
