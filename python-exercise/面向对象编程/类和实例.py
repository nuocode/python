# class Student(object):
#     pass
# #bart是指向Student的实例
# bart = Student()
# print(bart) # 返回<__main__.Student object at 0x00000230C87C9630> 0x00000230C87C9630表示内存
# print(Student)
#
# #给实例绑定属性
# bart.name = "Simpson Blair"
# print(bart.name)

#### 创建模板，绑定属性 ####
# class Student(object):
#     # 第一个参数永远是self，指向自己，不需要传参
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
# bart = Student('Simpson Blair', 19)
# print(bart.name)
# print(bart.score)

#类的方法
# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
#
# bart = Student('Simpson Blair', 19)
# result_score = bart.print_score()
# print(result_score)

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >=90:
            return "A"
        elif self.score >=60:
            return "B"
        else:
            return "C"

lisa = Student("Lisa", 99)
bart = Student("Bart", 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
