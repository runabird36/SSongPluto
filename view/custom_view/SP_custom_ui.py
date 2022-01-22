

from PyQt5 import QtCore, QtGui, QtWidgets
import SP_path_module as sp
class FlatHead(QtWidgets.QFrame):
    def __init__(self, _parent=None):
        super(FlatHead, self).__init__(_parent)
        self._parent = _parent
        # self.init_head()
        # self.init_link()


    def init_head(self):
        self.setObjectName(u"frame_top")
        self.setMaximumSize(QtCore.QSize(16777215, 55))
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setFrameShadow(QtWidgets.QFrame.Plain)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)



        # =========================================================

        self.lab_appname = QtWidgets.QLabel()
        self.lab_appname.setObjectName(u"lab_appname")
        font = QtGui.QFont()
        font.setFamily(u"Segoe UI Light")
        font.setPointSize(24)
        self.lab_appname.setFont(font)
        self.lab_appname.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout.addWidget(self.lab_appname)

        # =========================================================
        self.bn_min = QtWidgets.QPushButton()
        self.bn_min.setObjectName(u"bn_min")
        self.bn_min.setMaximumSize(QtCore.QSize(55, 55))
        self.bn_min.setStyleSheet(u"QPushButton {\n"
                                    "	border: none;\n"
                                    "	background-color: rgba(0,0,0,0);\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "	background-color: rgb(0,143,150);\n"
                                    "}\n"
                                    "QPushButton:pressed {	\n"
                                    "	background-color: rgba(0,0,0,0);\n"
                                    "}")
        icon1 = QtGui.QIcon()
        icon1.addFile(sp.hide_icon, QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_min.setIcon(icon1)
        self.bn_min.setIconSize(QtCore.QSize(22, 22))
        self.bn_min.setFlat(True)

        self.horizontalLayout.addWidget(self.bn_min)

        # ===========================================================
        self.bn_max = QtWidgets.QPushButton()
        self.bn_max.setObjectName(u"bn_max")
        self.bn_max.setMaximumSize(QtCore.QSize(55, 55))
        self.bn_max.setStyleSheet(u"QPushButton {\n"
                            "	border: none;\n"
                            "	background-color: rgba(0,0,0,0);\n"
                            "}\n"
                            "QPushButton:hover {\n"
                            "	background-color: rgb(0,143,150);\n"
                            "}\n"
                            "QPushButton:pressed {	\n"
                            "	background-color: rgba(0,0,0,0);\n"
                            "}")
        icon2 = QtGui.QIcon()
        icon2.addFile(sp.max_icon, QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_max.setIcon(icon2)
        self.bn_max.setIconSize(QtCore.QSize(22, 22))
        self.bn_max.setFlat(True)

        self.horizontalLayout.addWidget(self.bn_max)

        # ====================================================
        self.bn_close = QtWidgets.QPushButton()
        self.bn_close.setObjectName(u"bn_close")
        self.bn_close.setMaximumSize(QtCore.QSize(55, 55))
        self.bn_close.setStyleSheet(u"QPushButton {\n"
        "	border: none;\n"
        "	background-color: rgba(0,0,0,0);\n"
        "}\n"
        "QPushButton:hover {\n"
        "	background-color: rgb(0,143,150);\n"
        "}\n"
        "QPushButton:pressed {	\n"
        "	background-color: rgba(0,0,0,0);\n"
        "}")
        icon3 = QtGui.QIcon()
        icon3.addFile(sp.close_icon, QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_close.setIcon(icon3)
        self.bn_close.setIconSize(QtCore.QSize(22, 22))
        self.bn_close.setFlat(True)

        self.horizontalLayout.addWidget(self.bn_close)

        self.horizontalLayout.setStretch(0,10)
        self.horizontalLayout.setStretch(1,1)
        self.horizontalLayout.setStretch(2,1)
        self.horizontalLayout.setStretch(3,1)

        self.setLayout(self.horizontalLayout)
        self.init_link()


    def init_link(self):
        #############################################################################################                        -------(C1)
        #SINCE THERE IS NO WINDOWS TOPBAR, THE CLOSE MIN, MAX BUTTON ARE ABSENT AND SO THERE IS A NEED FOR THE ALTERNATIVE BUTTONS IN OUR
        #DIALOG BOX, WHICH IS CARRIED OUT BY THE BELOW CODE
        #-----> MINIMIZE BUTTON OF DIALOGBOX
        self.bn_min.clicked.connect(lambda: self.window().showMinimized())

        self.bn_max.clicked.connect(self.check_between_max_normal)

        #-----> CLOSE APPLICATION FUNCTION BUTTON
        self.bn_close.clicked.connect(lambda: self.window().close())

        # #-----> THIS FUNCTION WILL CHECKT WEATHER THE BUTRTON ON THE DIALOGBOX IS CLICKED, AND IF SO DIRECTS TO THE FUNCTINON : diag_return()
        # self.bn_east.clicked.connect(lambda: self.close())
        # self.bn_west.clicked.connect(lambda: self.close())

        self.dragPos = self.pos()   #INITIAL POSOTION OF THE DIALOGBOX
        def movedialogWindow(event):
            # MOVE WINDOW
            try:
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.window().move(self.window().pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
            except Exception as e:
                print(str(e))
        # WIDGET TO MOVE
        self.mouseMoveEvent = movedialogWindow  #CA

    #----> FUNCTION TO CAPTURE THE INITIAL POSITION OF THE MOUSE
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def check_between_max_normal(self):

        if self.window().windowState() & QtCore.Qt.WindowMaximized:
            self.window().showNormal()
        else:
            self.window().showMaximized()
