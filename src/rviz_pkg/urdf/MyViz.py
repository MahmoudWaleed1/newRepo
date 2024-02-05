#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

from rviz import bindings as rviz

class RVizWidget(QWidget):
    def __init__(self, config_file):
        super(RVizWidget, self).__init__()

        self.frame = rviz.VisualizationFrame()
        self.frame.setSplashPath("")
        self.frame.initialize()

        reader = rviz.YamlConfigReader()
        config = rviz.Config()
        reader.readFile(config, config_file)
        self.frame.load(config)

        self.frame.setMenuBar(None)
        self.frame.setStatusBar(None)
        self.frame.setHideButtonVisibility(False)

        self.manager = self.frame.getManager()
        self.grid_display = self.manager.getRootDisplayGroup().getDisplayAt(0)

        layout = QVBoxLayout()
        layout.addWidget(self.frame)

        h_layout = QHBoxLayout()
        layout.addLayout(h_layout)

        self.setLayout(layout)

    def onThicknessSliderChanged(self, new_value):
        if self.grid_display is not None:
            self.grid_display.subProp("Line Style").subProp("Line Width").setValue(new_value / 1000.0)

class AnotherUI(QWidget):
    def __init__(self):
        super(AnotherUI, self).__init__()

        self.rviz_widget = RVizWidget("/home/ahmedyahia/robot_ws/src/rviz_pkg/config/model_config.rviz")

        layout = QVBoxLayout()
        layout.addWidget(self.rviz_widget)

        button = QPushButton("Do Something in Another UI")
        button.clicked.connect(self.do_something)
        layout.addWidget(button)

        self.setLayout(layout)

    def do_something(self):
        print("Button clicked in Another UI")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create and show the first UI with RViz
    my_viz_widget = RVizWidget("/home/ahmedyahia/robot_ws/src/rviz_pkg/config/model_config.rviz")
    my_viz_widget.resize(1000, 1000)
    my_viz_widget.show()

    # Create and show the second UI
    another_ui = AnotherUI()
    another_ui.resize(800, 600)
    another_ui.show()

    sys.exit(app.exec_())
