'''


                表达式	    描述

                nodename	选取此节点的所有子节点

                /	        从当前节点选取直接子节点

                //	        从当前节点选取子孙节点

                .	        选取当前节点

                ..	        选取当前节点的父节点

                @	        选取属性

'''

from lxml import html

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

'''读取字符串'''
# etree = html.etree
# html_data = etree.HTML(text)
# result = etree.tostring(html_data)
# print(result.decode('utf-8'))#自动补全缺失标签

'''读取文件'''
# html_data = etree.parse('./test.html', etree.HTMLParser())
# result = etree.tostring(html_data)
# print(result.decode('utf-8'))#自动补全缺失标签并添加DOCTYPE声明

'''读取所有节点'''
# etree = html.etree
# html_data = etree.parse('./test.html', etree.HTMLParser())
# result = html_data.xpath('//*')#*代表所有
# print(result)

'''指定标签读取'''
# etree = html.etree
# html_data = etree.parse('./test.html', etree.HTMLParser())  # 解析html文件
# result = html_data.xpath('//li')  # 读取所有li标签
# print(result)
# print(result[0])

'''读取子节点'''
# etree = html.etree
# html_data = etree.parse('./test.html', etree.HTMLParser())
# result = html_data.xpath('//li/a')  # 读取所有li标签的子标签
# print(result)


'''读取父节点'''
# etree = html.etree
# html_data = etree.parse('./test.html', etree.HTMLParser())
# result = html_data.xpath('//a[@href="link4.html"]/../@class')
# print(result)

'''属性匹配'''
# etree = html.etree
# html_data = etree.parse('./test.html', etree.HTMLParser())
# result = html_data.xpath('//li[@class="item-0"]')  # 所有li下class="item-0"的标签
# print(result)

'''文本获取'''
# etree = html.etree
# html_data = etree.parse('./test.html', etree.HTMLParser())
# result = html_data.xpath('//li[@class="item-0"]//text()')  # 包含换行符
# print(result)
# result = html_data.xpath('//li[@class="item-0"]/a/text()')  # 没有特使符号的数据
# print(result)

'''属性获取'''
# etree = html.etree
# html_data = etree.parse('./test.html', etree.HTMLParser())
# result = html_data.xpath('//li/a/@href')
# print(result)

'''属性多值匹配'''
text = '''<li class="li li-first" name="item"><a href="link.html">first item</a></li>'''
# etree = html.etree
# html_data = etree.HTML(text)
# result = html_data.xpath('//li[contains(@class, "li")]/a/text()')
# print(result)

'''多属性匹配'''
# etree = html.etree
# html_data = etree.HTML(text)
# result = html_data.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# print(result)


text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
etree = html.etree
html_data = etree.HTML(text)
result = html_data.xpath('//li[1]/ancestor::*')  # 所有祖先节点
print(result)
result = html_data.xpath('//li[1]/ancestor::div')  # 限定div 选择div这个祖先
print(result)
result = html_data.xpath('//li[1]/attribute::*')  # 相同属性节点
print(result)
result = html_data.xpath('//li[1]/child::a[@href="link1.html"]')  # 找出href属性为link1.html的a标签
print(result)
result = html_data.xpath('//li[1]/descendant::span')  # 获取子节点限定词为span
print(result)
result = html_data.xpath('//li[1]/following::*[5]')
print(result)
result = html_data.xpath('//li[1]/following-sibling::*')
print(result)