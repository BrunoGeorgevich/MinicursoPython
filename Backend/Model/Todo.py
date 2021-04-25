from PySide2.QtCore import QObject, Property, Signal
from Backend.Model.BaseModel import BaseModel
from peewee import CharField

class Todo(BaseModel):    
    _description = CharField()
       
    # Getters and Setters    
    description_changed = Signal(str)
    @Property(str, notify=description_changed)
    def description(self): return self._description
    @description.setter
    def set_description(self, value): self._description = value