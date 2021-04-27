import QtQuick 2.7
import QtQuick.Controls 2.5
import QtQuick.Controls.Material 2.4

ApplicationWindow {
    id: root
    visible: true
    width: 640; height: 480
    minimumWidth: 640; minimumHeight: 480

    function addTodo() {                    
        todoController.add(descriptionTextField.text)
        descriptionTextField.text = ""
    }

    Row {
        anchors.fill: parent
        Item {
            width: parent.width * 2/3; height: parent.height
            Label {
                visible: todoController.isEmpty
                text: "A lista está vazia"
                font.pointSize: 20
                color: "#333"
                anchors {
                    topMargin: 10
                    top: parent.top
                    horizontalCenter: parent.horizontalCenter
                }
            }
            ListView {
                id: todoListView
                anchors {
                    fill: parent
                    margins: 5
                }
                spacing: 10
                model: todoController.items
                delegate: Rectangle {
                    width: todoListView.width; height: 50
                    radius: 3
                    color: "#CCC"
                    Row {
                        id: delegateMainRow
                        property int marginVal: 5
                        anchors {
                            fill: parent
                            margins: delegateMainRow.marginVal
                        }                        
                        spacing: 3
                        Label {
                            anchors.verticalCenter: parent.verticalCenter
                            width: parent.width * 0.9 - delegateMainRow.marginVal; height: parent.height - delegateMainRow.marginVal * 2
                            text: description
                            font.pointSize: 15
                            color: "#333"
                            fontSizeMode: "Fit"
                            verticalAlignment: "AlignVCenter"
                            wrapMode: "WrapAnywhere"
                        }

                        Rectangle {
                            anchors.verticalCenter: parent.verticalCenter
                            width: 1; height: parent.height - delegateMainRow.marginVal * 2
                            color: "#999"
                        }

                        Item {
                            anchors.verticalCenter: parent.verticalCenter
                            width: parent.width * 0.1 - delegateMainRow.marginVal; height: parent.height - delegateMainRow.marginVal * 2

                            Label {
                                id: xLabel
                                property string defaultColor: "#333"
                                anchors.centerIn: parent
                                text: "X"
                                color: defaultColor
                                font {
                                    pointSize: 15
                                    bold: true
                                }
                            }

                            MouseArea {
                                anchors.fill: parent

                                onClicked: {
                                    todoController.remove(index)
                                }

                                onPressed: {
                                    xLabel.color = Qt.lighter(xLabel.defaultColor, 2)
                                }

                                onReleased: {
                                    xLabel.color = xLabel.defaultColor
                                }

                                onCanceled: {
                                    xLabel.color = xLabel.defaultColor
                                }
                            }
                        }
                    }
                }
            }
        }
        Column {
            width: parent.width * 1/3
            anchors.verticalCenter: parent.verticalCenter
            TextField {
                id: descriptionTextField
                placeholderText: "Descrição"
                maximumLength: 120
                anchors.horizontalCenter: parent.horizontalCenter
                
                Keys.onReturnPressed: {
                    root.addTodo()
                }
            }

            Button {
                id: addButton
                text: "Adicionar"
                anchors.horizontalCenter: parent.horizontalCenter

                onClicked: {
                    root.addTodo()
                }
            }
        }
    }
}