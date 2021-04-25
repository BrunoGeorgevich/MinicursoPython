from PySide2.QtCore import QAbstractListModel, Slot, Signal, Qt, QObject, Property

from Backend.Controller.Controller import Controller, Items
from Backend.Model.Todo import Todo

class TodoItems(Items):
    DescriptionRole = Qt.UserRole + 1001

    def __init__(self, parent=None):
        super(TodoItems, self).__init__(parent)

    def data(self, index, role=Qt.DisplayRole):
        if 0 <= index.row() < self.rowCount() and index.isValid():
            item = self.entries[index.row()]
            if role == self.DescriptionRole:
                return item.description
        else:
            return None

    def roleNames(self):
        roles = dict()
        roles[self.DescriptionRole] = b'description'
        return roles

class TodoController(Controller):
    # Constructor
    def __init__(self):
        super().__init__(TodoItems())
        Todo.create_table()
        print("TABELA TODO CRIADA/CARREGADA COM SUCESSO!")
        self.sync()
        print(f"DADOS LIDOS COM SUCESSO :: {self.count}")
    
    def sync(self):
        self.items.clear()
        for it in list(Todo.select()):
            super().add(it)

    @Slot(str)
    def add(self, description):
        Todo.create(_description=description)
        self.sync()

    @Slot(int)
    def remove(self, idx):
        if not self.isEmpty and idx <= self.count -1 and idx >= 0:
            el = self.items.getRow(idx)
            el.delete_instance()
            super().remove(idx)
            self.sync()
#%%