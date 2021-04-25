from PySide2.QtCore import QObject, QAbstractListModel, QModelIndex, Slot, Signal, Property

import numpy as np

class Items(QAbstractListModel):
    __entries = []

    def __init__(self, parent=None):
        super(Items, self).__init__(parent)
    @Slot()    
    def rowCount(self, parent=QModelIndex()):
        if parent.isValid(): return 0
        return len(self.__entries)

    def appendRow(self, obj):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.__entries.append(obj)
        self.endInsertRows()

    def removeRow(self, index):
        self.beginRemoveRows(QModelIndex(), index, index)
        del self.__entries[index]
        self.endRemoveRows()

    def firstRow(self):
        if len(self.__entries) > 0:
            return self.__entries[0]

    def getRow(self, index):
        if len(self.__entries) > 0:
            return self.__entries[index]

    def lastRow(self):
        if len(self.__entries) > 0:
            return self.__entries[-1]

    def isEmpty(self):
        return len(self.__entries) == 0

    def clear(self):
        self.beginRemoveRows(QModelIndex(), 0, self.rowCount())
        self.__entries = []
        self.endRemoveRows()

    @Property(np.ndarray)
    def entries(self): return self.__entries

class Controller(QObject):
    
    # Signals
    synchronize = Signal()

    #Attributes
    __items = None

    #Constructor
    def __init__(self, items):
        super().__init__()
        self.__items = items
        
    #Methods
    def add(self, value):
        self.__items.appendRow(value)
        self.is_empty_changed.emit()
        self.count_changed.emit()

    @Slot('QVariant')
    def remove(self, index):
        self.__items.removeRow(index)
        self.is_empty_changed.emit()
        self.count_changed.emit()

    @Property('QVariant')
    def last(self):
        return self.__items.lastRow()

    first_has_changed = Signal()
    @Property('QVariant', notify=first_has_changed)
    def first(self):
        return self.__items.firstRow()

    is_empty_changed = Signal()
    @Property('QVariant', notify=is_empty_changed)
    def isEmpty(self):
        return self.__items.isEmpty()

    items_changed = Signal()
    @Property(QObject, notify=items_changed)
    def items(self):
        return self.__items

    count_changed = Signal()
    @Property(int, notify=count_changed)
    def count(self):
        return self.__items.rowCount()

    def clear(self):
        self.__items.clear()
        self.is_empty_changed.emit()
        self.count_changed.emit()
#%%