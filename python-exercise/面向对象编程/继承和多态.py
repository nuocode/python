class Animal(object):
    def run(self):
        print("Animal is running")
# #
class Dog(Animal):
    def run(self):
        print("Dog is running...")

class Cat(Animal):
    def run(self):
        print("Cat is running...")

class Tortoise(Animal):
    def run(self):
        print("Tortoise is running slowly")
#
# dog = Dog()
# print (dog.run())
# cat = Cat()
# print(cat.run())
#
# #class也是一种类型
# b = Animal()
# print(isinstance(b,Animal)) # 返回true

# 多态
def run_twice(animal):
    animal.run()
    animal.run()

#调用哪个跑哪个
p = run_twice(Cat())
print(p)
