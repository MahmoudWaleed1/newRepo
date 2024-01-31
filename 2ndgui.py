from PyQt5 import QtWidgets, uic ,QtGui
from PyQt5.QtCore import QTimer, QTime
import datetime
import os

yawPid_para = [ 6.6, 10 , 1.09]
pitchPid_para = [4.2 , 6.4 , 0.68]

class Gui(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super (Gui, self).__init__(parent)
        self.script_dir = os.path.abspath(os.path.dirname(__file__))
        self.gui_path = os.path.join(self.script_dir, 'newRepo.ui')        
        uic.loadUi(self.gui_path, self)


        self.trial_timer = QTimer(self)
        self.trial_timer.timeout.connect(self.update_trialTimer)
        self.trial_elapsed_time = 0

        self.startTrial.clicked.connect(self.start_trialTimer)
        self.resetTrial.clicked.connect(self.reset_trialTimer)
        self.stopTrial.clicked.connect(self.stop_trialTimer)

        self.tuningButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.trialButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        
        self.cancelYaw.clicked.connect(self.cancel_yaw_control)
        self.returnYaw.clicked.connect(self.return_yaw)
        self.cancelPitch.clicked.connect(self.cancel_pitch_control)
        self.returnPitch.clicked.connect(self.return_pitch)
      
        
      
        
        self.yawFlag = False
        self.yawFlag2 = True
        self.pitchFlag = False
        self.pitchFlag2 = True

        self.yaw_kp_slider.setMaximum(2000)
        self.yaw_ki_slider.setMaximum(2000)
        self.yaw_kd_slider.setMaximum(2000)
        self.pitch_kp_slider.setMaximum(2000)
        self.pitch_ki_slider.setMaximum(2000)
        self.pitch_kd_slider.setMaximum(2000)
        self.yaw_kp_slider.setSingleStep(1)
        self.yaw_ki_slider.setSingleStep(1)
        self.yaw_kd_slider.setSingleStep(1)
        self.pitch_kp_slider.setSingleStep(1)
        self.pitch_ki_slider.setSingleStep(1)
        self.pitch_kd_slider.setSingleStep(1)
        yaw_kp_ = self.findChild(QtWidgets.QSlider,"yaw_kp_slider")
        yaw_kp_.valueChanged.connect(lambda value: self.yaw_update_kp (value))
        yaw_kp_.setValue(round(yawPid_para[0]*5))
        self.yaw_kp_label = self.findChild(QtWidgets.QLabel,"yaw_kp_label")
        
        yaw_ki_ = self.findChild(QtWidgets.QSlider,"yaw_ki_slider")
        yaw_ki_.valueChanged.connect(lambda value: self.yaw_update_ki (value))
        yaw_ki_.setValue(round(yawPid_para[1]*5))
        self.yaw_ki_label = self.findChild(QtWidgets.QLabel,"yaw_ki_label")

        yaw_kd_ = self.findChild(QtWidgets.QSlider,"yaw_kd_slider")
        yaw_kd_.valueChanged.connect(lambda value: self.yaw_update_kd (value))
        yaw_kd_.setValue(round(yawPid_para[2]*5))
        self.yaw_kd_label = self.findChild(QtWidgets.QLabel,"yaw_kd_label")
        
        pitch_kp_ = self.findChild(QtWidgets.QSlider,"pitch_kp_slider")
        pitch_kp_.valueChanged.connect(lambda value: self.pitch_update_kp (value))
        pitch_kp_.setValue(round(pitchPid_para[0]*5))
        self.pitch_kp_label = self.findChild(QtWidgets.QLabel,"pitch_kp_label")

        pitch_ki_ = self.findChild(QtWidgets.QSlider,"pitch_ki_slider")
        pitch_ki_.valueChanged.connect(lambda value: self.pitch_update_ki (value))
        pitch_ki_.setValue(round(pitchPid_para[1]*5))
        self.pitch_ki_label = self.findChild(QtWidgets.QLabel,"pitch_ki_label")
        
        pitch_kd_ = self.findChild(QtWidgets.QSlider,"pitch_kd_slider")
        pitch_kd_.valueChanged.connect(lambda value: self.pitch_update_kd (value))
        pitch_kd_.setValue(round(pitchPid_para[2]*5))
        self.pitch_kd_label = self.findChild(QtWidgets.QLabel,"pitch_kd_label")


    def start_trialTimer(self):
        self.trial_timer.start(1000)
        self.trial_elapsed_time = 0

    def start_missionTimer(self):
        self.mission_timer.start(1000)
        self.mission_elapsed_time = 0
        
    def stop_trialTimer(self):
        self.trial_timer.stop()

    def reset_trialTimer(self):
        self.stop_trialTimer()
        self.trial_elapsed_time = 0
        self.TrialTimerLCD.display(str(QTime(0, 20, 0).toString("mm:ss")))

    def update_trialTimer(self):
        self.trial_elapsed_time += 1
        minute = self.trial_elapsed_time // 60
        second = self.trial_elapsed_time % 60
        elapsed = QTime(0, minute, second)
        time_str = str(QTime(0, 20, 0).addSecs(-self.trial_elapsed_time).toString("mm:ss"))
        self.TrialTimerLCD.display(time_str)

        if elapsed == QTime(0, 20, 0):
            self.stop_trialTimer()

    ##########################################################################################################
    def yaw_update_kp(self, value):
        self.kp = value / 100   
        yawPid_para[0] = self.kp
        self.yaw_kp_label.setText(f"{self.kp:.2f}")
    
    def yaw_update_ki(self, value):
        self.ki = value / 100
        yawPid_para[1] = self.ki

        self.yaw_ki_label.setText(f"{self.ki:.2f}")

    def yaw_update_kd(self, value):
        self.kd = value / 100
        yawPid_para[2] = self.kd    

        self.yaw_kd_label.setText(f"{self.kd:.2f}")        


    def pitch_update_kp(self, value):
        
        self.kp = value / 100
        pitchPid_para[0] = self.kp
        self.pitch_kp_label.setText(f"{self.kp:.2f}")

    def pitch_update_ki(self, value):
        self.ki = value / 100
        pitchPid_para[1] = self.ki
        self.pitch_ki_label.setText(f"{self.ki:.2f}")

    def pitch_update_kd(self, value):
        self.kd = value / 100
        pitchPid_para[2] = self.kd

        self.pitch_kd_label.setText(f"{self.kd:.2f}")
            

    def cancel_yaw_control(self):
        if self.yawFlag2:
            if not self.yawFlag:

                self.temp_yaw_kp = self.yaw_kp_slider.value()
                self.temp_yaw_ki = self.yaw_ki_slider.value()
                self.temp_yaw_kd = self.yaw_kd_slider.value()
        
                self.yaw_update_kp(0)
                self.yaw_update_ki(0)
                self.yaw_update_kd(0)
               
                self.yaw_kp_slider.setValue(0)
                self.yaw_ki_slider.setValue(0)
                self.yaw_kd_slider.setValue(0)
           
                self.yawFlag2 = False

            elif self.yawFlag:
                self.yaw_update_kp(self.temp_yaw_kp)
                self.yaw_update_ki(self.temp_yaw_ki)
                self.yaw_update_kd(self.temp_yaw_kd)
                self.yaw_kp_slider.setValue(self.temp_yaw_kp)
                self.yaw_ki_slider.setValue(self.temp_yaw_ki)
                self.yaw_kd_slider.setValue(self.temp_yaw_kd)

    def cancel_pitch_control(self):
        if self.pitchFlag2:
            if not self.pitchFlag:


                self.temp_pitch_kp = self.pitch_kp_slider.value()
                self.temp_pitch_ki = self.pitch_ki_slider.value()
                self.temp_pitch_kd = self.pitch_kd_slider.value()

                self.pitch_update_kp(0)
                self.pitch_update_ki(0)
                self.pitch_update_kd(0)

                self.pitch_kp_slider.setValue(0)
                self.pitch_ki_slider.setValue(0)
                self.pitch_kd_slider.setValue(0)
                self.pitchFlag2 = False

            elif self.pitchFlag:
                self.pitch_update_kp(self.temp_pitch_kp)
                self.pitch_update_ki(self.temp_pitch_ki)
                self.pitch_update_kd(self.temp_pitch_kd)
                self.pitch_kp_slider.setValue(self.temp_pitch_kp)
                self.pitch_ki_slider.setValue(self.temp_pitch_ki)
                self.pitch_kd_slider.setValue(self.temp_pitch_kd)


    def return_yaw(self):
        self.yawFlag = True
        self.yawFlag2 = True
        self.cancel_yaw_control()
        self.yawFlag = False
        self.yawFlag2 = True

    def return_pitch(self):
        self.pitchFlag = True
        self.pitchFlag2 = True
        self.cancel_pitch_control()
        self.pitchFlag = False
        self.pitchFlag2 = True



app = QtWidgets.QApplication([])
win = Gui()
win.showFullScreen()
app.exec()
