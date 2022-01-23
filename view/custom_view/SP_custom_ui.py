

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








class custom_listwidget(QtWidgets.QListWidget):

    def __init__(self, _parent):
        super(custom_listwidget, self).__init__(_parent)

        self._drop_file_list = []




    def reset_listwidget(self):
        self.clear()
        self._drop_file_list = []

    def set_items(self, item_list):
        # self.addItems(item_list)

        for _item in item_list:
            # _dirname = os.path.dirname(_item)
            if _item in self._drop_file_list:
                # print 11111111
                # print self._drop_file_list
                continue
            _basename = os.path.basename(_item)

            _custom_item = MP_custom_item.Ui_Form()
            _fname, _ext = os.path.splitext(_basename)
            _custom_item.set_info(_item, _fname, _ext)
            _custom_item.cancel_btn.clicked.connect(self.delete_custom_item)


            _listwidet_item = QtGui.QListWidgetItem(self)
            _listwidet_item.setSizeHint(_custom_item.sizeHint())

            self.addItem(_listwidet_item)
            self.setItemWidget(_listwidet_item, _custom_item)




    def set_file_list(self, _info):
        if isinstance(_info, str):
            self._drop_file_list.extend([_info])
        elif isinstance(_info, list):
            self._drop_file_list.extend(_info)

        self._drop_file_list = list(set(self._drop_file_list))


    def get_file_list(self):
        return self._drop_file_list





    def delete_custom_item(self):
        # print '============== Before pub list =============='
        # print self._drop_file_list
        # print '=============================================='
        _click_pos = self.mapFromGlobal(QtGui.QCursor.pos())
        item = self.itemAt(_click_pos)
        pop_widget = self.itemWidget(item)
        idx  = self.indexFromItem(item).row()
        pop_item = self.takeItem(idx)

        # print QtGui.QCursor.pos()
        # print _click_pos
        # print item
        # print idx
        # print pop_widget


        _removed_filename = pop_widget.get_full_path()

        self._drop_file_list.remove(_removed_filename)
        # print '============== After pub list =============='
        # print self._drop_file_list
        # print '=============================================='







    def unwrap_folder(self, _dirpath):
        tar_list = os.listdir(_dirpath)
        # print tar_list

        paths = []
        for _tar in tar_list:
            _tar = '{0}/{1}'.format(_dirpath, _tar)
            if sequence_file_toolkit.is_glob(_tar):
                _tar = sequence_file_toolkit.get_glob_path(_tar)

            paths.append(_tar)

        # print paths
        # print 22222222222222222222
        paths = list(set(paths))

        self.set_items(paths)
        self.set_file_list(paths)





    def dragEnterEvent(self, event):

        hasUrls = event.mimeData().hasUrls()
        if hasUrls == True:
            urls = event.mimeData().urls()
            # if len(urls) == 1:
            url_qurl = urls[0]
            try:
                # url = str(url.path())
                url = str(url_qurl.toString())
                if 'file:' in url:
                    if 'file:///' in url:
                        url = url.split('file:///')[1]
                    elif 'file://' in url:
                        url = url.split('file:')[1]
                else:
                    url = url[1:]

            except:
                url = str(url.toString())
                if 'file:///' in url:
                    url = url.split('file:///')[1]

            # print url
            # if os.path.isfile(url):
            event.setAccepted(True)
            # else:
            #     event.setAccepted(False)

            # elif len(urls) >=2:
            #     print "mulitples"
            #     print urls
            #     event.setAccepted(True)




    def dragMoveEvent(self, event):
        # print event
        pass

    def dropEvent(self, event):
        # self.reset_listwidget()
        # print event
        urls = event.mimeData().urls()

        # if len(urls) == 1:
        paths = []
        # display_list = []
        url_qurl = urls[0]
        # if os.path.isdir(url_qurl)
        for url_qurl in urls:
            try:
                # url = str(url.path())
                url = str(url_qurl.toString())
                if 'file:' in url:
                    if 'file:///' in url:
                        url = url.split('file:///')[1]
                    elif 'file://' in url:
                        url = url.split('file:')[1]
                else:
                    url = url[1:]

                path = url
            except:
                path = str(url.toString())
                if 'file:///' in path:
                    path = path.split('file:///')[1]

            if os.path.exists(path) == False:
                return None

            if os.path.isdir(path) == True:
                self.unwrap_folder(path)
                continue

            if sequence_file_toolkit.is_glob(path):
                path = sequence_file_toolkit.get_glob_path(path)

            paths.append(path)
            # display_list.append(os.path.basename(path))




        paths = list(set(paths))
        # pprint(paths)
        self.set_items(paths)
        self.set_file_list(paths)
