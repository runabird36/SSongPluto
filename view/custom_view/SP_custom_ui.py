

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


        # self.frame_top_east = QtWidgets.QFrame(self)
        # self.frame_top_east.setObjectName(u"frame_top_east")
        # self.frame_top_east.setMaximumSize(QtCore.QSize(16777215, 55))
        # self.frame_top_east.setStyleSheet(u"background:rgb(51,51,51);")
        # self.frame_top_east.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.frame_top_east.setFrameShadow(QtWidgets.QFrame.Plain)
        # self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_top_east)
        # self.horizontalLayout_4.setSpacing(0)
        # self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        # self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        # self.frame_appname = QtWidgets.QFrame(self.frame_top_east)
        # self.frame_appname.setObjectName(u"frame_appname")
        # self.frame_appname.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.frame_appname.setFrameShadow(QtWidgets.QFrame.Plain)
        # self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_appname)
        # self.horizontalLayout_10.setSpacing(7)
        # self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        # self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        # self.lab_appname = QtWidgets.QLabel(self.frame_appname)
        # self.lab_appname.setObjectName(u"lab_appname")
        # font = QtGui.QFont()
        # font.setFamily(u"Segoe UI Light")
        # font.setPointSize(24)
        # self.lab_appname.setFont(font)
        # self.lab_appname.setStyleSheet(u"color:rgb(255,255,255);")
        #
        # self.horizontalLayout_10.addWidget(self.lab_appname)
        #
        #
        # self.horizontalLayout_4.addWidget(self.frame_appname)
        #
        #
        #
        #
        # self.frame_min = QtWidgets.QFrame(self.frame_top_east)
        # self.frame_min.setObjectName(u"frame_min")
        # self.frame_min.setMinimumSize(QtCore.QSize(55, 55))
        # self.frame_min.setMaximumSize(QtCore.QSize(55, 55))
        # self.frame_min.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.frame_min.setFrameShadow(QtWidgets.QFrame.Plain)
        # self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_min)
        # self.horizontalLayout_7.setSpacing(0)
        # self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        # self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        # self.bn_min = QtWidgets.QPushButton(self.frame_min)
        # self.bn_min.setObjectName(u"bn_min")
        # self.bn_min.setMaximumSize(QtCore.QSize(55, 55))
        # self.bn_min.setStyleSheet(u"QPushButton {\n"
        #                             "	border: none;\n"
        #                             "	background-color: rgba(0,0,0,0);\n"
        #                             "}\n"
        #                             "QPushButton:hover {\n"
        #                             "	background-color: rgb(0,143,150);\n"
        #                             "}\n"
        #                             "QPushButton:pressed {	\n"
        #                             "	background-color: rgba(0,0,0,0);\n"
        #                             "}")
        # icon1 = QtGui.QIcon()
        # icon1.addFile(sp.hide_icon, QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.bn_min.setIcon(icon1)
        # self.bn_min.setIconSize(QtCore.QSize(22, 22))
        # self.bn_min.setFlat(True)
        #
        # self.horizontalLayout_7.addWidget(self.bn_min)
        #
        #
        # self.horizontalLayout_4.addWidget(self.frame_min)
        #
        # self.frame_max = QtWidgets.QFrame(self.frame_top_east)
        # self.frame_max.setObjectName(u"frame_max")
        # self.frame_max.setMinimumSize(QtCore.QSize(55, 55))
        # self.frame_max.setMaximumSize(QtCore.QSize(55, 55))
        # self.frame_max.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.frame_max.setFrameShadow(QtWidgets.QFrame.Plain)
        # self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_max)
        # self.horizontalLayout_6.setSpacing(0)
        # self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        # self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        # self.bn_max = QtWidgets.QPushButton(self.frame_max)
        # self.bn_max.setObjectName(u"bn_max")
        # self.bn_max.setMaximumSize(QtCore.QSize(55, 55))
        # self.bn_max.setStyleSheet(u"QPushButton {\n"
        #                     "	border: none;\n"
        #                     "	background-color: rgba(0,0,0,0);\n"
        #                     "}\n"
        #                     "QPushButton:hover {\n"
        #                     "	background-color: rgb(0,143,150);\n"
        #                     "}\n"
        #                     "QPushButton:pressed {	\n"
        #                     "	background-color: rgba(0,0,0,0);\n"
        #                     "}")
        # icon2 = QtGui.QIcon()
        # icon2.addFile(sp.max_icon, QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.bn_max.setIcon(icon2)
        # self.bn_max.setIconSize(QtCore.QSize(22, 22))
        # self.bn_max.setFlat(True)
        #
        # self.horizontalLayout_6.addWidget(self.bn_max)
        #
        #
        # self.horizontalLayout_4.addWidget(self.frame_max)
        #
        # self.frame_close = QtWidgets.QFrame(self.frame_top_east)
        # self.frame_close.setObjectName(u"frame_close")
        # self.frame_close.setMinimumSize(QtCore.QSize(55, 55))
        # self.frame_close.setMaximumSize(QtCore.QSize(55, 55))
        # self.frame_close.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.frame_close.setFrameShadow(QtWidgets.QFrame.Plain)
        # self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_close)
        # self.horizontalLayout_5.setSpacing(0)
        # self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        # self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        #
        # self.bn_close = QtWidgets.QPushButton(self.frame_close)
        # self.bn_close.setObjectName(u"bn_close")
        # self.bn_close.setMaximumSize(QtCore.QSize(55, 55))
        # self.bn_close.setStyleSheet(u"QPushButton {\n"
        # "	border: none;\n"
        # "	background-color: rgba(0,0,0,0);\n"
        # "}\n"
        # "QPushButton:hover {\n"
        # "	background-color: rgb(0,143,150);\n"
        # "}\n"
        # "QPushButton:pressed {	\n"
        # "	background-color: rgba(0,0,0,0);\n"
        # "}")
        # icon3 = QtGui.QIcon()
        # icon3.addFile(sp.close_icon, QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.bn_close.setIcon(icon3)
        # self.bn_close.setIconSize(QtCore.QSize(22, 22))
        # self.bn_close.setFlat(True)
        #
        # self.horizontalLayout_5.addWidget(self.bn_close)
        #
        #
        # self.horizontalLayout_4.addWidget(self.frame_close)
        #
        #
        # self.horizontalLayout.addWidget(self.frame_top_east)




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


    def check_between_max_normal(self):
        
        if self.window().windowState() & QtCore.Qt.WindowMaximized:
            self.window().showNormal()
        else:
            self.window().showMaximized()
