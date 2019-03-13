# print(type(123))
# print(type(abs))
# # 判断一个对象是否是函数
# import types
# def fn():
#     pass
#
# print(type(fn)==types.FunctionType)
# print(type(abs)== types.BuiltinFunctionType)
# print(type(lambda x:x)==types.LambdaType)
# print(type(x for x in range(10))==types.GeneratorType)

#dir()方法
#print(dir("ABD"))

#等价的方法
# print(len("ABC") == "ABC".__len__())

#getattr(), setattr(), hasattr()
class Myobject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = Myobject()

print(hasattr(obj,"x")) #是否有属性x？
print(obj.x)
print(hasattr(obj,"y")) #有属性y吗？目前没有
print(setattr(obj,"y",19)) #设置属性y
print(hasattr(obj,"y"))
print(getattr(obj,"y"))

#传入default参数
print(getattr(obj,"z",404))# 获取属性'z'，如果不存在，返回默认值404
