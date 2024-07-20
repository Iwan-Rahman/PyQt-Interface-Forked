

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.7
import QtQuick.Controls 6.7
import CCC

Rectangle {
    id: rectangle
    width: Constants.width
    height: Constants.height
    color: "#2f2f2f"


    Text {
        id: label
        y: 46
        width: 313
        height: 48
        visible: true
        text: qsTr("Connection Manager")
        font.family: Constants.font.family
        font.pixelSize: 32
        font.bold: true
        color: "white"
        anchors.topMargin: -500
        anchors.horizontalCenterOffset: -772
        anchors.horizontalCenter: parent.horizontalCenter
    }

    Text {
        id: label1
        y: 129
        visible: true
        color: "#ffffff"
        text: qsTr("Sync Status:")
        anchors.topMargin: -401
        font.pixelSize: 25
        font.family: Constants.font.family
        font.bold: false
        anchors.horizontalCenterOffset: -849
        anchors.horizontalCenter: parent.horizontalCenter
    }

    Text {
        id: label2
        y: 202
        visible: true
        color: "#ffffff"
        text: qsTr("Active Channel:")
        anchors.topMargin: -329
        font.pixelSize: 25
        font.family: Constants.font.family
        font.bold: false
        anchors.horizontalCenterOffset: -829
        anchors.horizontalCenter: parent.horizontalCenter
    }

    Text {
        id: label3
        y: 279
        visible: true
        color: "#ffffff"
        text: qsTr("Static Channel:")
        anchors.topMargin: -260
        font.pixelSize: 25
        font.family: Constants.font.family
        font.bold: false
        anchors.horizontalCenterOffset: -833
        anchors.horizontalCenter: parent.horizontalCenter
    }
    states: [
        State {
            name: "clicked"

            PropertyChanges {
                target: label
                text: qsTr("Button Checked")
            }
        }
    ]

    Rectangle {
        id: rectangle1
        x: 515
        y: 52
        width: 2
        height: 287
        color: "#ffffff"
    }

    Rectangle {
        id: rectangle2
        x: 538
        y: 62
        width: 413
        height: 198
        color: "#515151"

        Text {
            id: text1
            x: 152
            y: 137
            width: 118
            height: 39
            text: qsTr("2D Plotter")
            font.pixelSize: 25
            color: "white"
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }

        Image {
            id: image
            x: 31
            y: 40
            width: 84
            height: 79
            source: "qrc:/qtquickplugin/images/template_image.png"
            fillMode: Image.PreserveAspectFit
        }

        Image {
            id: image1
            x: 165
            y: 40
            width: 84
            height: 79
            source: "qrc:/qtquickplugin/images/template_image.png"
            fillMode: Image.PreserveAspectFit
        }

        Image {
            id: image2
            x: 294
            y: 40
            width: 84
            height: 79
            source: "qrc:/qtquickplugin/images/template_image.png"
            fillMode: Image.PreserveAspectFit
        }

        Rectangle {
            id: rectangle4
            x: 455
            y: 0
            width: 413
            height: 198
            color: "#515151"
            Text {
                id: text2
                x: 152
                y: 137
                width: 118
                height: 39
                color: "#ffffff"
                text: qsTr("3D Plotter")
                font.pixelSize: 25
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter

                Rectangle {
                    id: rectangle6
                    x: 295
                    y: -137
                    width: 413
                    height: 198
                    color: "#515151"
                    Text {
                        id: text3
                        x: 152
                        y: 137
                        width: 118
                        height: 39
                        color: "#ffffff"
                        text: qsTr("Warnings")
                        font.pixelSize: 25
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }

                    Image {
                        id: image20
                        x: 31
                        y: 40
                        width: 84
                        height: 79
                        source: "qrc:/qtquickplugin/images/template_image.png"
                        fillMode: Image.PreserveAspectFit
                    }

                    Image {
                        id: image21
                        x: 165
                        y: 40
                        width: 84
                        height: 79
                        source: "qrc:/qtquickplugin/images/template_image.png"
                        fillMode: Image.PreserveAspectFit
                    }

                    Image {
                        id: image22
                        x: 294
                        y: 40
                        width: 84
                        height: 79
                        source: "qrc:/qtquickplugin/images/template_image.png"
                        fillMode: Image.PreserveAspectFit
                    }
                }

                Rectangle {
                    id: rectangle7
                    x: 295
                    y: 67
                    width: 413
                    height: 73
                    color: "#868686"
                    Image {
                        id: image23
                        x: 8
                        y: 8
                        width: 50
                        height: 57
                        source: "qrc:/qtquickplugin/images/template_image.png"
                        fillMode: Image.PreserveAspectFit
                    }

                    Image {
                        id: image24
                        x: 64
                        y: 8
                        width: 50
                        height: 57
                        source: "qrc:/qtquickplugin/images/template_image.png"
                        fillMode: Image.PreserveAspectFit
                    }

                    Image {
                        id: image25
                        x: 126
                        y: 8
                        width: 50
                        height: 57
                        source: "qrc:/qtquickplugin/images/template_image.png"
                        fillMode: Image.PreserveAspectFit
                    }

                    Image {
                        id: image26
                        x: 182
                        y: 8
                        width: 50
                        height: 57
                        source: "qrc:/qtquickplugin/images/template_image.png"
                        fillMode: Image.PreserveAspectFit
                    }

                    Image {
                        id: image27
                        x: 243
                        y: 8
                        width: 50
                        height: 57
                        source: "qrc:/qtquickplugin/images/template_image.png"
                        fillMode: Image.PreserveAspectFit
                    }

                    Image {
                        id: image28
                        x: 299
                        y: 8
                        width: 50
                        height: 57
                        source: "qrc:/qtquickplugin/images/template_image.png"
                        fillMode: Image.PreserveAspectFit
                    }

                    Image {
                        id: image29
                        x: 355
                        y: 8
                        width: 50
                        height: 57
                        source: "qrc:/qtquickplugin/images/template_image.png"
                        fillMode: Image.PreserveAspectFit
                    }
                }
            }

            Image {
                id: image10
                x: 31
                y: 40
                width: 84
                height: 79
                source: "qrc:/qtquickplugin/images/template_image.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: image11
                x: 165
                y: 40
                width: 84
                height: 79
                source: "qrc:/qtquickplugin/images/template_image.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: image12
                x: 294
                y: 40
                width: 84
                height: 79
                source: "qrc:/qtquickplugin/images/template_image.png"
                fillMode: Image.PreserveAspectFit
            }
        }

        Rectangle {
            id: rectangle5
            x: 455
            y: 204
            width: 413
            height: 73
            color: "#868686"
            Image {
                id: image13
                x: 8
                y: 8
                width: 50
                height: 57
                source: "qrc:/qtquickplugin/images/template_image.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: image14
                x: 64
                y: 8
                width: 50
                height: 57
                source: "qrc:/qtquickplugin/images/template_image.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: image15
                x: 126
                y: 8
                width: 50
                height: 57
                source: "qrc:/qtquickplugin/images/template_image.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: image16
                x: 182
                y: 8
                width: 50
                height: 57
                source: "qrc:/qtquickplugin/images/template_image.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: image17
                x: 243
                y: 8
                width: 50
                height: 57
                source: "qrc:/qtquickplugin/images/template_image.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: image18
                x: 299
                y: 8
                width: 50
                height: 57
                source: "qrc:/qtquickplugin/images/template_image.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: image19
                x: 355
                y: 8
                width: 50
                height: 57
                source: "qrc:/qtquickplugin/images/template_image.png"
                fillMode: Image.PreserveAspectFit
            }
        }
    }

    Rectangle {
        id: rectangle3
        x: 538
        y: 266
        width: 413
        height: 73
        color: "#868686"

        Image {
            id: image3
            x: 8
            y: 8
            width: 50
            height: 57
            source: "qrc:/qtquickplugin/images/template_image.png"
            fillMode: Image.PreserveAspectFit
        }

        Image {
            id: image4
            x: 64
            y: 8
            width: 50
            height: 57
            source: "qrc:/qtquickplugin/images/template_image.png"
            fillMode: Image.PreserveAspectFit
        }

        Image {
            id: image5
            x: 126
            y: 8
            width: 50
            height: 57
            source: "qrc:/qtquickplugin/images/template_image.png"
            fillMode: Image.PreserveAspectFit
        }

        Image {
            id: image6
            x: 182
            y: 8
            width: 50
            height: 57
            source: "qrc:/qtquickplugin/images/template_image.png"
            fillMode: Image.PreserveAspectFit
        }

        Image {
            id: image7
            x: 243
            y: 8
            width: 50
            height: 57
            source: "qrc:/qtquickplugin/images/template_image.png"
            fillMode: Image.PreserveAspectFit
        }

        Image {
            id: image8
            x: 299
            y: 8
            width: 50
            height: 57
            source: "qrc:/qtquickplugin/images/template_image.png"
            fillMode: Image.PreserveAspectFit
        }

        Image {
            id: image9
            x: 355
            y: 8
            width: 50
            height: 57
            source: "qrc:/qtquickplugin/images/template_image.png"
            fillMode: Image.PreserveAspectFit
        }
    }

    Button {
        id: button
        x: 77
        y: 348
        text: qsTr("PORT 1")
        font.pixelSize: 20
        background: Rectangle {
            implicitWidth: button.implicitWidth
            implicitHeight: button.implicitHeight
            color: "white"
            radius: 10
            border.color: "black"
            border.width: 1
        }
        Connections {
            target: button
            onClicked: colorAnimation.start()
        }

    }

    Button {
        id: button1
        x: 231
        y: 348
        text: qsTr("PORT 2")
        font.pixelSize: 20
        background: Rectangle {
            color: "#ffffff"
            radius: 10
            border.color: "#000000"
            border.width: 1
            implicitWidth: button1.implicitWidth
            implicitHeight: button1.implicitHeight
        }
        Connections {
            target: button1
            onClicked: colorAnimation.start()
        }
    }

    Button {
        id: button2
        x: 391
        y: 348
        text: qsTr("PORT 3")
        font.pixelSize: 20
        background: Rectangle {
            color: "#ffffff"
            radius: 10
            border.color: "#000000"
            border.width: 1
            implicitWidth: button2.implicitWidth
            implicitHeight: button2.implicitHeight
        }
        Connections {
            target: button2
            onClicked: colorAnimation.start()
        }
    }

    Rectangle {
        id: warnignwidget
        x: 1395
        y: 482
        width: 455
        height: 526
        color: "#5b5b5b"

        Text {
            id: text4
            x: 21
            y: 27
            width: 146
            height: 46
            text: qsTr("Warnings")
            font.pixelSize: 30
            font.bold: true
            color: "white"
        }
    }

    Rectangle {
        id: portPressed
        x: 124
        y: 436
        width: 314
        height: 34
        color: "#ffffff"

        ColorAnimation {
            id: colorAnimation
            target: portPressed
            property: "color"
            from: "#ffffff"
            to: "#00ff00"
            duration: 500
            running: false
        }
    }
}
