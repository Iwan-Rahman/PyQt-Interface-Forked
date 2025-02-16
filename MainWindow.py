# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 571)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.connectionWidget = QtWidgets.QWidget(self.centralwidget)
        self.connectionWidget.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.connectionWidget.setObjectName("connectionWidget")
        self.horizontalLayout.addWidget(self.connectionWidget)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.warningWidget = QtWidgets.QWidget(self.centralwidget)
        self.warningWidget.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.warningWidget.setObjectName("warningWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.warningWidget)
        self.verticalLayout_4.setContentsMargins(4, 0, 4, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout.addWidget(self.warningWidget)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setStyleSheet("background-color: rgb(120, 120, 120);")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setStyleSheet("background-color: rgb(120, 120, 120);")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout.addWidget(self.widget_4, 0, 1, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setStyleSheet("background-color: rgb(120, 120, 120);")
        self.widget_5.setObjectName("widget_5")
        self.gridLayout.addWidget(self.widget_5, 1, 0, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setStyleSheet("background-color: rgb(120, 120, 120);")
        self.widget_6.setObjectName("widget_6")
        self.gridLayout.addWidget(self.widget_6, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuData = QtWidgets.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        self.menuSensor_Configuration = QtWidgets.QMenu(self.menuData)
        self.menuSensor_Configuration.setObjectName("menuSensor_Configuration")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuDisplay = QtWidgets.QMenu(self.menuSettings)
        self.menuDisplay.setObjectName("menuDisplay")
        self.menuWidgets = QtWidgets.QMenu(self.menuSettings)
        self.menuWidgets.setObjectName("menuWidgets")
        self.menuFile_Paths = QtWidgets.QMenu(self.menuSettings)
        self.menuFile_Paths.setObjectName("menuFile_Paths")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionOpen_Project = QtWidgets.QAction(MainWindow)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionSave_Project = QtWidgets.QAction(MainWindow)
        self.actionSave_Project.setObjectName("actionSave_Project")
        self.actionSave_Project_As = QtWidgets.QAction(MainWindow)
        self.actionSave_Project_As.setObjectName("actionSave_Project_As")
        self.actionImport_Data = QtWidgets.QAction(MainWindow)
        self.actionImport_Data.setObjectName("actionImport_Data")
        self.actionExport_Data = QtWidgets.QAction(MainWindow)
        self.actionExport_Data.setObjectName("actionExport_Data")
        self.actionGauges = QtWidgets.QAction(MainWindow)
        self.actionGauges.setObjectName("actionGauges")
        self.actionSystem_Health = QtWidgets.QAction(MainWindow)
        self.actionSystem_Health.setObjectName("actionSystem_Health")
        self.actionAdd_Sensor = QtWidgets.QAction(MainWindow)
        self.actionAdd_Sensor.setObjectName("actionAdd_Sensor")
        self.actionAdd_Sensor_2 = QtWidgets.QAction(MainWindow)
        self.actionAdd_Sensor_2.setObjectName("actionAdd_Sensor_2")
        self.actionRemove_Sensor = QtWidgets.QAction(MainWindow)
        self.actionRemove_Sensor.setObjectName("actionRemove_Sensor")
        self.actionSampling_Rate = QtWidgets.QAction(MainWindow)
        self.actionSampling_Rate.setObjectName("actionSampling_Rate")
        self.actionAlert_Thresholds = QtWidgets.QAction(MainWindow)
        self.actionAlert_Thresholds.setObjectName("actionAlert_Thresholds")
        self.actionProject_Settings = QtWidgets.QAction(MainWindow)
        self.actionProject_Settings.setObjectName("actionProject_Settings")
        self.actionUser_Preferences = QtWidgets.QAction(MainWindow)
        self.actionUser_Preferences.setObjectName("actionUser_Preferences")
        self.actionUnits = QtWidgets.QAction(MainWindow)
        self.actionUnits.setObjectName("actionUnits")
        self.actionLock_Layout = QtWidgets.QAction(MainWindow)
        self.actionLock_Layout.setObjectName("actionLock_Layout")
        self.actionUnlock_Layout = QtWidgets.QAction(MainWindow)
        self.actionUnlock_Layout.setObjectName("actionUnlock_Layout")
        self.actionAdd_Widget = QtWidgets.QAction(MainWindow)
        self.actionAdd_Widget.setObjectName("actionAdd_Widget")
        self.actionRemove_Widget = QtWidgets.QAction(MainWindow)
        self.actionRemove_Widget.setObjectName("actionRemove_Widget")
        self.actionSave_Layout = QtWidgets.QAction(MainWindow)
        self.actionSave_Layout.setObjectName("actionSave_Layout")
        self.actionLoad_Layout = QtWidgets.QAction(MainWindow)
        self.actionLoad_Layout.setObjectName("actionLoad_Layout")
        self.actionDefault_File_Path = QtWidgets.QAction(MainWindow)
        self.actionDefault_File_Path.setObjectName("actionDefault_File_Path")
        self.actionDefault_Snap_Path = QtWidgets.QAction(MainWindow)
        self.actionDefault_Snap_Path.setObjectName("actionDefault_Snap_Path")
        self.menuFile.addAction(self.actionConnect)
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addAction(self.actionSave_Project_As)
        self.menuFile.addAction(self.actionImport_Data)
        self.menuFile.addAction(self.actionExport_Data)
        self.menuView.addAction(self.actionGauges)
        self.menuView.addAction(self.actionSystem_Health)
        self.menuSensor_Configuration.addAction(self.actionAdd_Sensor_2)
        self.menuSensor_Configuration.addAction(self.actionRemove_Sensor)
        self.menuData.addAction(self.menuSensor_Configuration.menuAction())
        self.menuData.addAction(self.actionSampling_Rate)
        self.menuData.addAction(self.actionAlert_Thresholds)
        self.menuData.addAction(self.actionUnits)
        self.menuDisplay.addAction(self.actionLock_Layout)
        self.menuDisplay.addAction(self.actionUnlock_Layout)
        self.menuDisplay.addAction(self.actionSave_Layout)
        self.menuDisplay.addAction(self.actionLoad_Layout)
        self.menuWidgets.addAction(self.actionAdd_Widget)
        self.menuWidgets.addAction(self.actionRemove_Widget)
        self.menuFile_Paths.addAction(self.actionDefault_File_Path)
        self.menuFile_Paths.addAction(self.actionDefault_Snap_Path)
        self.menuSettings.addAction(self.actionProject_Settings)
        self.menuSettings.addAction(self.actionUser_Preferences)
        self.menuSettings.addAction(self.menuDisplay.menuAction())
        self.menuSettings.addAction(self.menuWidgets.menuAction())
        self.menuSettings.addAction(self.menuFile_Paths.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuData.setTitle(_translate("MainWindow", "Data"))
        self.menuSensor_Configuration.setTitle(_translate("MainWindow", "Sensor Configuration"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuDisplay.setTitle(_translate("MainWindow", "Display"))
        self.menuWidgets.setTitle(_translate("MainWindow", "Widgets"))
        self.menuFile_Paths.setTitle(_translate("MainWindow", "File Paths"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project"))
        self.actionSave_Project.setText(_translate("MainWindow", "Save Project"))
        self.actionSave_Project_As.setText(_translate("MainWindow", "Save Project As"))
        self.actionImport_Data.setText(_translate("MainWindow", "Import Data"))
        self.actionExport_Data.setText(_translate("MainWindow", "Export Data"))
        self.actionGauges.setText(_translate("MainWindow", "Gauges"))
        self.actionSystem_Health.setText(_translate("MainWindow", "System Health"))
        self.actionAdd_Sensor.setText(_translate("MainWindow", "Add Sensor"))
        self.actionAdd_Sensor_2.setText(_translate("MainWindow", "Add Sensor"))
        self.actionRemove_Sensor.setText(_translate("MainWindow", "Remove Sensor"))
        self.actionSampling_Rate.setText(_translate("MainWindow", "Sampling Rate"))
        self.actionAlert_Thresholds.setText(_translate("MainWindow", "Alert Thresholds"))
        self.actionProject_Settings.setText(_translate("MainWindow", "Project Settings"))
        self.actionUser_Preferences.setText(_translate("MainWindow", "User Preferences"))
        self.actionUnits.setText(_translate("MainWindow", "Units"))
        self.actionLock_Layout.setText(_translate("MainWindow", "Lock Layout"))
        self.actionUnlock_Layout.setText(_translate("MainWindow", "Unlock Layout"))
        self.actionAdd_Widget.setText(_translate("MainWindow", "Add Widget"))
        self.actionRemove_Widget.setText(_translate("MainWindow", "Remove Widget"))
        self.actionSave_Layout.setText(_translate("MainWindow", "Save Layout"))
        self.actionLoad_Layout.setText(_translate("MainWindow", "Load Layout"))
        self.actionDefault_File_Path.setText(_translate("MainWindow", "Default File Path"))
        self.actionDefault_Snap_Path.setText(_translate("MainWindow", "Default Snap Path"))
