import csv

with open('csv_data.csv', 'w') as file:
    # print(type(csv.writer(file)))
    #
    writer = csv.writer(file, delimiter=' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1001', 'Jack', 20])
    writer.writerow(['1002', 'Summer', 33])
    # 多行写入
    writer.writerows([['1003', 'Tim', 34], ['1004', 'Fuck', 99]])

'''
字典写入方式
'''

with open('csv_data2.csv', 'w', encoding='utf-8') as file:
    filednames = ['id', 'name', 'age']
    writer = csv.DictWriter(file, fieldnames=filednames)
    # 写入头信息
    writer.writeheader()
    writer.writerow({'id': '1001', 'name': 'Jack', 'age': 22})
    writer.writerow({'id': '1002', 'name': 'Tim', 'age': 33})

'''
读取
'''

with open('csv_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

'''
pandas
'''
import pandas as pd
df = pd.read_csv('csv_data.csv')
print(df)