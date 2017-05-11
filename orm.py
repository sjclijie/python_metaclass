# coding: utf-8


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.columt_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.name, self.columt_type)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class InterField(Field):
    def __init__(self, name):
        super(InterField, self).__init__(name, "int")


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)

        print("Found model: %s" % name)

        mappings = dict()

        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mapping: %s ==> %s" % (k, v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs["__mappings__"] = mappings
        attrs["__table__"] = name

        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(" 'Model' object has no attribute %s " % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []

        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))

        sql = 'insert into %s (%s) values(%s)' % (self.__table__, ','.join(fields), ','.join(params))

        print("SQL: %s" % sql)
        print("ARGS: %s" % str(args))


# Test

class User(Model):
    id = InterField("id")
    name = StringField("username")
    email = StringField("email")
    password = StringField("password")


u = User(id=12345, name="hello")

u.save()


