'''
(1) @property : When the value of A B property is derived from another A property. 
And the B attribute is updated as the value of the initial A attribute changes
    @attribute.setter use to reAssign the value of B (A could be renewed) 

(2) class constructor : __new__
    创建实例 : __new__
    初始化 : __init__
    link : https://zhuanlan.zhihu.com/p/366156798

(3) static method
    not use class or object variables
'''
class Sample:
   
  @staticmethod
  def method():
    print('This is a static method')
 
Sample.method()
'''
    class method
    used by class but not object
'''    
class Sample:
  var = "Class Variable"
 
  @classmethod
  def method(cls):
    print(cls.var)
 
Sample.method()
'''
    instance method
    used by instance
'''   
class Sample:
  def __init__(self, a):
        self.a = a
 
  def method(self):
    print(self.a)
 
obj = Sample(10)
obj.method()
'''
    link : https://www.pythonpool.com/python-cls-vs-self/
'''
