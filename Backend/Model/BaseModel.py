from PySide2.QtCore import QObject
from peewee import Model, CharField, SqliteDatabase

db = SqliteDatabase('dados.db')

class FinalMeta(type(Model), type(QObject)):
    pass

class BaseModel(Model, QObject, metaclass=FinalMeta):    
    class Meta:
        database = db