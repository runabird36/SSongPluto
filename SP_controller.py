# -*- coding: utf-8 -*-

'''

controller all model, view, and anything else


'''


import sys

from PyQt5 import QtWidgets, QtCore

import SP_path_module as sp

import SP_main_view

import SP_py_toolkit

import SP_hub_controller as sh

from pprint import pprint
import traceback, os, subprocess, time, datetime, math, re

import functools





class SPController():
    def __init__(self):
        self._ui = SP_main_view.Ui_SSongPluto()

        try:
            pass
        except:
            traceback.print_exc()



    def _setup(self):
        self._ui.setupUi()
        self.init_data()
        self.set_link()


    def init_data(self):
        self._ui.frame_top.set_status_gif('IMPROGRESS')

        self.load_default()
        _root_path = sp.get_root_path()
        if _root_path is not None:
            self.set_root_info_in_tool(_root_path)
            self.thread_pool = SP_py_toolkit.Pool()
            self.thread_pool.add_job(self.query_prj_info)
            self.thread_pool.finished.connect(self.init_prj_view)
            self.thread_pool.start_pool()


    def _show(self):
        self._ui.show()


    def set_link(self):
        # self._ui.frame_top.bn_min.clicked.connect(lambda: self._ui.showMinimized())
        # self._ui.frame_top.bn_close.clicked.connect(lambda: self._ui.close())
        self._ui.SP_root_dir_btn.clicked.connect(self.select_root_dir)
        self._ui.SP_info_prj_lw.itemClicked.connect(self.select_cur_prj)

    def run(self):
        self._setup()
        self._show()







    def select_root_dir(self):
        '''
        - check default info (root) by txt
        - if there is no default info, set path by user input
        '''
        try:
            _sel_path = self._ui.get_selectedpath()
            self.set_root_info_in_tool(_sel_path)

            self._ui.refresh_all()
            sh.refresh_data()
            self.init_data()
        except:
            traceback.print_exc()

    def set_root_info_in_tool(self, _path):
        '''
        - global variable
        - ui
        '''
        sp._ROOT_PATH_ = _path
        self._ui.set_root_lb(_path)

        sp.set_root_path(_path)

        self.save_default()






    def query_prj_info(self):
        _root_path = sp.get_root_path()
        sh.collect_prj_info(_root_path)
        time.sleep(1)


    def init_prj_view(self):
        self._ui.set_prj_lw(sh._PRJ_HUB_)
        self._ui.frame_top.set_status_gif('CLEAR')





    def select_cur_prj(self,_cur_prj_item):
        _prj_obj = _cur_prj_item.data(QtCore.Qt.UserRole)
        self._ui.set_description(_prj_obj)


    def save_default(self):
        SP_py_toolkit.write_json(sp._DEFAULT_INFO_PATH_, sp._DEFAULT_INFO_DICT_)


    def load_default(self):
        _res = SP_py_toolkit.read_json(sp._DEFAULT_INFO_PATH_)
        sp._DEFAULT_INFO_DICT_ = _res









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    try:
        _engine = SPController()
        _engine.run()
    except:
        traceback.print_exc()
    sys.exit(app.exec_())
