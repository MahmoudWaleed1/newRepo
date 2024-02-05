try:
    from PyQt5.QtWidgets import *
except ImportError as e:
    print(f"Error importing PyQt5: {e}")
if __name__ == '__main__':
    app = QApplication( sys.argv )

    myviz = MyViz()
    myviz.resize( 1000, 1000 )
    myviz.show()

    app.exec_()
