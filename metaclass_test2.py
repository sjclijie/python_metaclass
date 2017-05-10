# coding: utf-8

class UpperAttrMetaClass(type):
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith(""))
        upperattr_attr = dict((name.upper(), value) for name, value in attrs)
        """
        return type(future_class_name, future_class_parents, future_class_attr)
        """
        # 父类type.__new__方法
        return type.__new__(upperattr_metaclass, future_class_name, future_class_parents, upperattr_attr)
        # or
        # return super(UpperAttrMetaClass, upperattr_metaclass).__new__(future_class_name, future_class_parents,
        # upperattr_attr)


"""
1.拦截类的创建
2.修改类
3.返回修改之后的类
"""


class Foo(object): pass

print(id(Foo))
