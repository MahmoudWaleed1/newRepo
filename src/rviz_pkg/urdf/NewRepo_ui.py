# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewRepo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2284, 1215)
        MainWindow.setStyleSheet(u"background-color: black\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{}\n"
"#widget{\n"
"border-top: 3px solid rgb(79, 192, 208);\n"
"border-bottom: 3px solid rgb(79, 192, 208);\n"
"border-right: 3px solid rgb(79, 192, 208);\n"
"border-left: 3px solid rgb(79, 192, 208);\n"
"border-radius:20px;\n"
"}\n"
"#frame{\n"
"border-top: 3px solid rgb(79, 192, 208);\n"
"border-bottom: 3px solid rgb(79, 192, 208);\n"
"border-right: 3px solid rgb(79, 192, 208);\n"
"border-left: 3px solid rgb(79, 192, 208);\n"
"border-radius:20px;\n"
"}\n"
"#frame2{\n"
"border-top: 3px solid rgb(79, 192, 208);\n"
"border-bottom: 3px solid rgb(79, 192, 208);\n"
"border-right: 3px solid rgb(79, 192, 208);\n"
"border-left: 3px solid rgb(79, 192, 208);\n"
"border-radius:20px;\n"
"}\n"
"#widget2{\n"
"border-bottom: 3px solid rgb(79, 192, 208);\n"
"border-right: 3px solid rgb(79, 192, 208);\n"
"border-left: 3px solid rgb(79, 192, 208);\n"
"border-radius:20px;\n"
"}\n"
"#frame3{\n"
"border-top: 3px solid rgb(79, 192, 208);\n"
"border-bottom: 3px solid rgb(79, 192, 208);\n"
"border-right: 3px solid rgb"
                        "(79, 192, 208);\n"
"border-left: 3px solid rgb(79, 192, 208);\n"
"border-radius:20px;\n"
"}\n"
"#frame4{\n"
"border-top: 3px solid rgb(79, 192, 208);\n"
"border-bottom: 3px solid rgb(79, 192, 208);\n"
"border-right: 3px solid rgb(79, 192, 208);\n"
"border-left: 3px solid rgb(79, 192, 208);\n"
"border-radius:20px;\n"
"}\n"
"#frame5{\n"
"border-top: 3px solid rgb(79, 192, 208);\n"
"border-bottom: 3px solid rgb(79, 192, 208);\n"
"border-right: 3px solid rgb(79, 192, 208);\n"
"border-left: 3px solid rgb(79, 192, 208);\n"
"border-radius:20px;\n"
"}\n"
"QLCDNumber\n"
"{\n"
"background-color:transparent;\n"
"}\n"
"QPushButton\n"
"{\n"
"color: rgb(61, 151, 179);\n"
"background-color: rgb(35, 37, 44);\n"
"}\n"
"QLabel\n"
"{\n"
"color: rgb(53, 172, 190);\n"
"font: 23pt \"JetBrains Mono\";\n"
"background-color: transparent;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget2 = QStackedWidget(self.centralwidget)
        self.stackedWidget2.setObjectName(u"stackedWidget2")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.floatReturnButton = QPushButton(self.page)
        self.floatReturnButton.setObjectName(u"floatReturnButton")
        self.floatReturnButton.setGeometry(QRect(10, 10, 390, 90))
        self.floatReturnButton.setMinimumSize(QSize(0, 90))
        self.floatReturnButton.setMaximumSize(QSize(390, 16777215))
        self.floatReturnButton.setStyleSheet(u"font: 20pt \"Ubuntu\";")
        self.stackedWidget2.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame3 = QFrame(self.page_2)
        self.frame3.setObjectName(u"frame3")
        self.frame3.setMinimumSize(QSize(0, 380))
        self.frame3.setMaximumSize(QSize(550, 16777215))
        self.frame3.setStyleSheet(u"font: 10pt \"Ubuntu\";")
        self.frame3.setFrameShape(QFrame.StyledPanel)
        self.frame3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.frame3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 14pt \"Ubuntu\";")

        self.gridLayout_3.addWidget(self.label_5, 3, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 4, 1, 1)

        self.MagnetometerLabel = QLabel(self.frame3)
        self.MagnetometerLabel.setObjectName(u"MagnetometerLabel")
        self.MagnetometerLabel.setStyleSheet(u"font: 14pt \"Ubuntu\";")

        self.gridLayout_3.addWidget(self.MagnetometerLabel, 3, 7, 1, 1)

        self.MotionDirectionLabel = QLabel(self.frame3)
        self.MotionDirectionLabel.setObjectName(u"MotionDirectionLabel")
        self.MotionDirectionLabel.setStyleSheet(u"font: 14pt \"Ubuntu\";")

        self.gridLayout_3.addWidget(self.MotionDirectionLabel, 3, 3, 1, 1)

        self.label_8 = QLabel(self.frame3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 14pt \"Ubuntu\";")

        self.gridLayout_3.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_16 = QLabel(self.frame3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: 14pt \"Ubuntu\";")

        self.gridLayout_3.addWidget(self.label_16, 1, 5, 1, 1)

        self.GyroscopeLabel = QLabel(self.frame3)
        self.GyroscopeLabel.setObjectName(u"GyroscopeLabel")
        self.GyroscopeLabel.setStyleSheet(u"font: 14pt \"Ubuntu\";")

        self.gridLayout_3.addWidget(self.GyroscopeLabel, 1, 7, 1, 1)

        self.label_20 = QLabel(self.frame3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font: 14pt \"Ubuntu\";")

        self.gridLayout_3.addWidget(self.label_20, 3, 5, 1, 1)

        self.MaxSpeedLabel = QLabel(self.frame3)
        self.MaxSpeedLabel.setObjectName(u"MaxSpeedLabel")
        self.MaxSpeedLabel.setStyleSheet(u"font: 14pt \"Ubuntu\";")

        self.gridLayout_3.addWidget(self.MaxSpeedLabel, 2, 3, 1, 1)

        self.OperationModeLabel = QLabel(self.frame3)
        self.OperationModeLabel.setObjectName(u"OperationModeLabel")
        self.OperationModeLabel.setStyleSheet(u"font: 14pt \"Ubuntu\";")

        self.gridLayout_3.addWidget(self.OperationModeLabel, 1, 3, 1, 1)

        self.ControlLabel = QLabel(self.frame3)
        self.ControlLabel.setObjectName(u"ControlLabel")
        self.ControlLabel.setStyleSheet(u"font: 14pt \"Ubuntu\";")

        self.gridLayout_3.addWidget(self.ControlLabel, 0, 3, 1, 1)

        self.SystemLabel = QLabel(self.frame3)
        self.SystemLabel.setObjectName(u"SystemLabel")
        self.SystemLabel.setStyleSheet(u"font: 14pt \"Ubuntu\";")

        self.gridLayout_3.addWidget(self.SystemLabel, 0, 7, 1, 1)

        self.label_7 = QLabel(self.frame3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 14pt \"Ubuntu\";")

        self.gridLayout_3.addWidget(self.label_7, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.label_13 = QLabel(self.frame3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 14pt \"Ubuntu\";")

        self.gridLayout_3.addWidget(self.label_13, 0, 5, 1, 1)

        self.AccelerometerLabel = QLabel(self.frame3)
        self.AccelerometerLabel.setObjectName(u"AccelerometerLabel")
        self.AccelerometerLabel.setStyleSheet(u"font: 14pt \"Ubuntu\";")

        self.gridLayout_3.addWidget(self.AccelerometerLabel, 2, 7, 1, 1)

        self.label_6 = QLabel(self.frame3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 14pt \"Ubuntu\";")

        self.gridLayout_3.addWidget(self.label_6, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 8, 1, 1)

        self.label_18 = QLabel(self.frame3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font: 14pt \"Ubuntu\";")

        self.gridLayout_3.addWidget(self.label_18, 2, 5, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 6, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.frame3, 0, 2, 1, 1)

        self.widget = QWidget(self.page_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 380))
        self.widget.setMaximumSize(QSize(550, 800))

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.frame2 = QFrame(self.page_2)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Raised)
        self.mission = QComboBox(self.frame2)
        self.mission.setObjectName(u"mission")
        self.mission.setGeometry(QRect(210, 50, 271, 25))
        self.mission.setStyleSheet(u" background-color: rgb(105,117,115);")
        self.label_3 = QLabel(self.frame2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 20, 181, 71))
        self.label_3.setStyleSheet(u"font: 16t \"Ubuntu\";")
        self.label_4 = QLabel(self.frame2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 100, 221, 71))
        self.missionTimerLCD = QLCDNumber(self.frame2)
        self.missionTimerLCD.setObjectName(u"missionTimerLCD")
        self.missionTimerLCD.setGeometry(QRect(150, 170, 141, 41))
        self.startMission = QPushButton(self.frame2)
        self.startMission.setObjectName(u"startMission")
        self.startMission.setGeometry(QRect(40, 240, 151, 31))
        self.stopMission = QPushButton(self.frame2)
        self.stopMission.setObjectName(u"stopMission")
        self.stopMission.setGeometry(QRect(200, 240, 151, 31))
        self.resetMission = QPushButton(self.frame2)
        self.resetMission.setObjectName(u"resetMission")
        self.resetMission.setGeometry(QRect(360, 240, 151, 31))

        self.gridLayout.addWidget(self.frame2, 2, 0, 2, 1)

        self.frame5 = QFrame(self.page_2)
        self.frame5.setObjectName(u"frame5")
        self.frame5.setFrameShape(QFrame.StyledPanel)
        self.frame5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.depthButton = QPushButton(self.frame5)
        self.depthButton.setObjectName(u"depthButton")
        self.depthButton.setMinimumSize(QSize(0, 90))
        self.depthButton.setMaximumSize(QSize(390, 16777215))
        self.depthButton.setStyleSheet(u"font: 20pt \"Ubuntu\";")

        self.gridLayout_4.addWidget(self.depthButton, 1, 0, 1, 1)

        self.floatButton = QPushButton(self.frame5)
        self.floatButton.setObjectName(u"floatButton")
        self.floatButton.setMinimumSize(QSize(0, 90))
        self.floatButton.setMaximumSize(QSize(390, 16777215))
        self.floatButton.setStyleSheet(u"font: 20pt \"Ubuntu\";")

        self.gridLayout_4.addWidget(self.floatButton, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_4.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.frame5, 2, 2, 2, 1)

        self.rviz_widget = QWidget(self.page_2)
        self.rviz_widget.setObjectName(u"rviz_widget")
        self.rviz_widget.setStyleSheet(u"#rviz_widget{\n"
"border-top: 3px solid rgb(79, 192, 208);\n"
"border-bottom: 3px solid rgb(79, 192, 208);\n"
"border-right: 3px solid rgb(79, 192, 208);\n"
"border-left: 3px solid rgb(79, 192, 208);\n"
"border-radius:20px;\n"
"}")

        self.gridLayout.addWidget(self.rviz_widget, 0, 1, 2, 1)

        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(550, 380))
        self.frame.setMaximumSize(QSize(550, 380))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.TrialTimerLCD = QLCDNumber(self.page_5)
        self.TrialTimerLCD.setObjectName(u"TrialTimerLCD")
        self.TrialTimerLCD.setGeometry(QRect(130, 110, 271, 121))
        self.startTrial = QPushButton(self.page_5)
        self.startTrial.setObjectName(u"startTrial")
        self.startTrial.setGeometry(QRect(100, 320, 101, 31))
        self.startTrial.setStyleSheet(u"font: 15pt \"Ubuntu\";")
        self.stopTrial = QPushButton(self.page_5)
        self.stopTrial.setObjectName(u"stopTrial")
        self.stopTrial.setGeometry(QRect(210, 320, 101, 31))
        self.stopTrial.setStyleSheet(u"font: 15pt \"Ubuntu\";")
        self.resetTrial = QPushButton(self.page_5)
        self.resetTrial.setObjectName(u"resetTrial")
        self.resetTrial.setGeometry(QRect(320, 320, 101, 31))
        self.resetTrial.setStyleSheet(u"font: 15pt \"Ubuntu\";")
        self.label_2 = QLabel(self.page_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 40, 201, 41))
        self.label_2.setStyleSheet(u"")
        self.tuningButton = QPushButton(self.page_5)
        self.tuningButton.setObjectName(u"tuningButton")
        self.tuningButton.setGeometry(QRect(0, 10, 111, 41))
        self.tuningButton.setStyleSheet(u"font: 15pt \"Ubuntu\";")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.trialButton = QPushButton(self.page_6)
        self.trialButton.setObjectName(u"trialButton")
        self.trialButton.setGeometry(QRect(0, 10, 111, 41))
        self.trialButton.setStyleSheet(u"font: 15pt \"Ubuntu\";")
        self.yaw_ki_slider = QSlider(self.page_6)
        self.yaw_ki_slider.setObjectName(u"yaw_ki_slider")
        self.yaw_ki_slider.setGeometry(QRect(210, 60, 311, 16))
        self.yaw_ki_slider.setStyleSheet(u"background-color: rgb(50, 175, 138);")
        self.yaw_ki_slider.setOrientation(Qt.Horizontal)
        self.yaw_kd_slider = QSlider(self.page_6)
        self.yaw_kd_slider.setObjectName(u"yaw_kd_slider")
        self.yaw_kd_slider.setGeometry(QRect(210, 120, 311, 16))
        self.yaw_kd_slider.setStyleSheet(u"background-color: rgb(50, 175, 138);")
        self.yaw_kd_slider.setOrientation(Qt.Horizontal)
        self.yaw_kp_slider = QSlider(self.page_6)
        self.yaw_kp_slider.setObjectName(u"yaw_kp_slider")
        self.yaw_kp_slider.setGeometry(QRect(210, 0, 311, 16))
        self.yaw_kp_slider.setStyleSheet(u"background-color: rgb(50, 175, 138);")
        self.yaw_kp_slider.setOrientation(Qt.Horizontal)
        self.yaw_kp_label = QLabel(self.page_6)
        self.yaw_kp_label.setObjectName(u"yaw_kp_label")
        self.yaw_kp_label.setGeometry(QRect(300, 20, 81, 31))
        self.yaw_kp_label.setStyleSheet(u"font: 18pt \"Ubuntu\";")
        self.yaw_ki_label = QLabel(self.page_6)
        self.yaw_ki_label.setObjectName(u"yaw_ki_label")
        self.yaw_ki_label.setGeometry(QRect(300, 80, 81, 31))
        self.yaw_ki_label.setStyleSheet(u"font: 18pt \"Ubuntu\";")
        self.yaw_kd_label = QLabel(self.page_6)
        self.yaw_kd_label.setObjectName(u"yaw_kd_label")
        self.yaw_kd_label.setGeometry(QRect(300, 140, 81, 31))
        self.yaw_kd_label.setStyleSheet(u"font: 18pt \"Ubuntu\";")
        self.pitch_kp_label = QLabel(self.page_6)
        self.pitch_kp_label.setObjectName(u"pitch_kp_label")
        self.pitch_kp_label.setGeometry(QRect(300, 200, 111, 31))
        self.pitch_kp_label.setStyleSheet(u"font: 18pt \"Ubuntu\";")
        self.pitch_ki_label = QLabel(self.page_6)
        self.pitch_ki_label.setObjectName(u"pitch_ki_label")
        self.pitch_ki_label.setGeometry(QRect(300, 260, 111, 31))
        self.pitch_ki_label.setStyleSheet(u"font: 18pt \"Ubuntu\";")
        self.pitch_kd_label = QLabel(self.page_6)
        self.pitch_kd_label.setObjectName(u"pitch_kd_label")
        self.pitch_kd_label.setGeometry(QRect(300, 320, 111, 31))
        self.pitch_kd_label.setStyleSheet(u"font: 18pt \"Ubuntu\";")
        self.yaw_kp_label_2 = QLabel(self.page_6)
        self.yaw_kp_label_2.setObjectName(u"yaw_kp_label_2")
        self.yaw_kp_label_2.setGeometry(QRect(130, -10, 81, 31))
        self.yaw_kp_label_2.setStyleSheet(u"font: 18pt \"Ubuntu\";")
        self.yaw_ki_label_2 = QLabel(self.page_6)
        self.yaw_ki_label_2.setObjectName(u"yaw_ki_label_2")
        self.yaw_ki_label_2.setGeometry(QRect(130, 50, 81, 31))
        self.yaw_ki_label_2.setStyleSheet(u"font: 18pt \"Ubuntu\";")
        self.yaw_kd_label_2 = QLabel(self.page_6)
        self.yaw_kd_label_2.setObjectName(u"yaw_kd_label_2")
        self.yaw_kd_label_2.setGeometry(QRect(130, 110, 81, 31))
        self.yaw_kd_label_2.setStyleSheet(u"font: 18pt \"Ubuntu\";")
        self.pitch_kp_label_2 = QLabel(self.page_6)
        self.pitch_kp_label_2.setObjectName(u"pitch_kp_label_2")
        self.pitch_kp_label_2.setGeometry(QRect(120, 170, 111, 31))
        self.pitch_kp_label_2.setStyleSheet(u"font: 18pt \"Ubuntu\";")
        self.pitch_ki_label_2 = QLabel(self.page_6)
        self.pitch_ki_label_2.setObjectName(u"pitch_ki_label_2")
        self.pitch_ki_label_2.setGeometry(QRect(120, 230, 111, 31))
        self.pitch_ki_label_2.setStyleSheet(u"font: 18pt \"Ubuntu\";")
        self.pitch_kd_label_2 = QLabel(self.page_6)
        self.pitch_kd_label_2.setObjectName(u"pitch_kd_label_2")
        self.pitch_kd_label_2.setGeometry(QRect(120, 290, 111, 31))
        self.pitch_kd_label_2.setStyleSheet(u"font: 18pt \"Ubuntu\";")
        self.cancelYaw = QPushButton(self.page_6)
        self.cancelYaw.setObjectName(u"cancelYaw")
        self.cancelYaw.setGeometry(QRect(0, 70, 101, 61))
        self.cancelYaw.setStyleSheet(u"font: 13pt \"Ubuntu\";")
        self.cancelPitch = QPushButton(self.page_6)
        self.cancelPitch.setObjectName(u"cancelPitch")
        self.cancelPitch.setGeometry(QRect(0, 140, 101, 61))
        self.cancelPitch.setStyleSheet(u"font: 13pt \"Ubuntu\";")
        self.returnYaw = QPushButton(self.page_6)
        self.returnYaw.setObjectName(u"returnYaw")
        self.returnYaw.setGeometry(QRect(0, 220, 101, 61))
        self.returnYaw.setStyleSheet(u"font: 13pt \"Ubuntu\";")
        self.returnPitch = QPushButton(self.page_6)
        self.returnPitch.setObjectName(u"returnPitch")
        self.returnPitch.setGeometry(QRect(0, 290, 101, 61))
        self.returnPitch.setStyleSheet(u"font: 13pt \"Ubuntu\";")
        self.pitch_kp_slider = QSlider(self.page_6)
        self.pitch_kp_slider.setObjectName(u"pitch_kp_slider")
        self.pitch_kp_slider.setGeometry(QRect(210, 180, 311, 16))
        self.pitch_kp_slider.setStyleSheet(u"background-color: rgb(50, 175, 138);")
        self.pitch_kp_slider.setOrientation(Qt.Horizontal)
        self.pitch_ki_slider = QSlider(self.page_6)
        self.pitch_ki_slider.setObjectName(u"pitch_ki_slider")
        self.pitch_ki_slider.setGeometry(QRect(210, 240, 311, 16))
        self.pitch_ki_slider.setStyleSheet(u"background-color: rgb(50, 175, 138);")
        self.pitch_ki_slider.setOrientation(Qt.Horizontal)
        self.pitch_kd_slider = QSlider(self.page_6)
        self.pitch_kd_slider.setObjectName(u"pitch_kd_slider")
        self.pitch_kd_slider.setGeometry(QRect(210, 300, 311, 16))
        self.pitch_kd_slider.setStyleSheet(u"background-color: rgb(50, 175, 138);")
        self.pitch_kd_slider.setOrientation(Qt.Horizontal)
        self.stackedWidget.addWidget(self.page_6)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.frame4 = QFrame(self.page_2)
        self.frame4.setObjectName(u"frame4")
        self.frame4.setFrameShape(QFrame.StyledPanel)
        self.frame4.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame4, 1, 2, 1, 1)

        self.logo_label = QLabel(self.page_2)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setStyleSheet(u"background-color :rgb(0, 0, 0) ;\n"
"image:url(:/logo/logo.png)")

        self.gridLayout.addWidget(self.logo_label, 2, 1, 2, 1)

        self.stackedWidget2.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.depthReturnButton = QPushButton(self.page_3)
        self.depthReturnButton.setObjectName(u"depthReturnButton")
        self.depthReturnButton.setGeometry(QRect(10, 10, 390, 90))
        self.depthReturnButton.setMinimumSize(QSize(0, 90))
        self.depthReturnButton.setMaximumSize(QSize(390, 16777215))
        self.depthReturnButton.setStyleSheet(u"font: 20pt \"Ubuntu\";")
        self.stackedWidget2.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.stackedWidget2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget2.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.floatReturnButton.setText(QCoreApplication.translate("MainWindow", u"RETURN", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"MotionDirection", None))
        self.MagnetometerLabel.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.MotionDirectionLabel.setText(QCoreApplication.translate("MainWindow", u"Normal/Reverse", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Control", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Gyroscope", None))
        self.GyroscopeLabel.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Magnetometer", None))
        self.MaxSpeedLabel.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.OperationModeLabel.setText(QCoreApplication.translate("MainWindow", u"Auto/Manual", None))
        self.ControlLabel.setText(QCoreApplication.translate("MainWindow", u"On/Off", None))
        self.SystemLabel.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"OperationMode", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.AccelerometerLabel.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"MaxSpeed", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Accelerometer", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Mission List", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Mission Timer", None))
        self.startMission.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.stopMission.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.resetMission.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.depthButton.setText(QCoreApplication.translate("MainWindow", u"DEPTH GRAPH", None))
        self.floatButton.setText(QCoreApplication.translate("MainWindow", u"FLOAT GRAPH", None))
        self.startTrial.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.stopTrial.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.resetTrial.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TIME LEFT", None))
        self.tuningButton.setText(QCoreApplication.translate("MainWindow", u"TUNING", None))
        self.trialButton.setText(QCoreApplication.translate("MainWindow", u"TRIAL", None))
        self.yaw_kp_label.setText(QCoreApplication.translate("MainWindow", u"Yaw kp", None))
        self.yaw_ki_label.setText(QCoreApplication.translate("MainWindow", u"Yaw ki", None))
        self.yaw_kd_label.setText(QCoreApplication.translate("MainWindow", u"Yaw kd", None))
        self.pitch_kp_label.setText(QCoreApplication.translate("MainWindow", u"Pitch Kp", None))
        self.pitch_ki_label.setText(QCoreApplication.translate("MainWindow", u"Pitch Ki", None))
        self.pitch_kd_label.setText(QCoreApplication.translate("MainWindow", u"Pitch Kd", None))
        self.yaw_kp_label_2.setText(QCoreApplication.translate("MainWindow", u"Yaw kp", None))
        self.yaw_ki_label_2.setText(QCoreApplication.translate("MainWindow", u"Yaw ki", None))
        self.yaw_kd_label_2.setText(QCoreApplication.translate("MainWindow", u"Yaw kd", None))
        self.pitch_kp_label_2.setText(QCoreApplication.translate("MainWindow", u"Pitch Kp", None))
        self.pitch_ki_label_2.setText(QCoreApplication.translate("MainWindow", u"Pitch Ki", None))
        self.pitch_kd_label_2.setText(QCoreApplication.translate("MainWindow", u"Pitch Kd", None))
        self.cancelYaw.setText(QCoreApplication.translate("MainWindow", u"Cancel Yaw", None))
        self.cancelPitch.setText(QCoreApplication.translate("MainWindow", u"Cancel Pitch", None))
        self.returnYaw.setText(QCoreApplication.translate("MainWindow", u"Return Yaw", None))
        self.returnPitch.setText(QCoreApplication.translate("MainWindow", u"Return Pitch", None))
        self.logo_label.setText("")
        self.depthReturnButton.setText(QCoreApplication.translate("MainWindow", u"RETURN", None))
    # retranslateUi

