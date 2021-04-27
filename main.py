import sys
import os

from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QResource

from Backend.Controller.TodoController import TodoController

if __name__ == "__main__":
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
    app = QApplication(sys.argv)
    QResource.registerResource("main.rcc")

    engine = QQmlApplicationEngine()
    ctx = engine.rootContext()

    todo_controller = TodoController()    
    ctx.setContextProperty("todoController", todo_controller)
    
    engine.load('qrc:/main.qml')

    sys.exit(app.exec_())