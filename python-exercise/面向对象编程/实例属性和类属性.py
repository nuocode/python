
# #通过实例变量或self绑定属性
# class Student(object):
#     def __init__(self,name):
#         self.name = name
#
# s = Student("Bob")

# 定义类属性,实例属性优先级比类属性高
class Student(object):
    name = "Bob" #定义类属性

s = Student() #创建实例s
print(s.name)  #Bob
print(Student.name) #Bob

s.name = "Michael"
print(s.name) #Michael
print(Student.name) #Bob

del s.name #删除实例name属性
print(s.name) #Bob
