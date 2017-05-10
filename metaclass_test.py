# coding: utf-8

def upper_attr(future_class_name, future_class_parents, future_class_attr):
    print(future_class_attr.items())

    # 选择所有非内置属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith("__"))

    # 转大写
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)

    print(attrs)
    print(uppercase_attr)

    #创建新对象
    return type(future_class_name, future_class_parents, future_class_attr)

__metaclass__ = upper_attr


class Foo():
    bar = "bip"


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, "BAR"))

f = Foo()

print(getattr(f, "BAR", None))
