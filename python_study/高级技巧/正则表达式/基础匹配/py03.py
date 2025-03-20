# 正则表达式，又称规则表达式，是使用单个字符串来描述，匹配某个句法规则的字符串，
# 常被用于检索、替换那些符合某个模式（规则）的文本
# 正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，
# 组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑

# Python正则表达式，使用re模块，并基于re模块中三个基础方法来做正则匹配
# 分别是：match、search、findall三个基础方法
import re
# re.match(匹配规则, 被匹配字符串)
# 从被匹配字符串开头匹配，匹配成功返回匹配对象（包含匹配的信息），匹配不成功则返回None
# s = "hello world"
# result = re.match("hello", s)
# result2 = re.match("world", s)
# print(result)            # <re.Match object; span=(0, 5), match='hello'>
# print(result.span())     # (0, 5)
# print(result.group())    # hello
# print(result2)           # None

# re.search(匹配规则, 被匹配字符串)
# 搜索整个字符串，找出匹配的。从前向后，找到第一个后就停止，不会继续向后
# s = "oh hhh ni hao ya xiao nai long hhh"
# result = re.search("hhh", s)
# result2 = re.search("bbb", s)
# print(result)            # <re.Match object; span=(3, 6), match='hhh'>
# print(result.span())     # (3, 6)
# print(result.group())    # hhh
# print(result2)           # None

# re.findall(匹配规则, 被匹配字符串)
# 搜索整个字符串，找出所有匹配的，返回一个列表，列表中每个元素都是匹配对象
# s = "ha ha ha he he he"
# result = re.findall("ha", s)
# result2 = re.findall("666", s)
# print(result)            # ['ha', 'ha', 'ha']
# print(result2)           # []

