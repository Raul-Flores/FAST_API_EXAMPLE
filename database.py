from re import I
from peewee import *

database = MySQLDatabase('test', user='root', password='test', host='localhost', port=3306)

class item(Model):
    name = CharField(max_length=30)
    price = IntegerField()
    quantity = IntegerField()

    def __str_(self):
        return self.name
    class Meta:
        database = database
        table_name = 'items'
    