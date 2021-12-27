# -*- coding: utf-8 -*-

'''

controller all model, view, and anything else


'''


import sys

from PyQt5 import QtWidgets

import SP_path_module as sp

import SP_main_view

import SP_py_toolkit


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
        self.set_default_info()
        _root_path = sp.get_root_path()
        print(_root_path)
        if _root_path is not None:
            self.set_root_info_in_tool(_root_path)


    def _show(self):
        self._ui.show()


    def set_link(self):
        self._ui.SP_root_dir_btn.clicked.connect(self.select_root_dir)


    def run(self):
        self._setup()
        self._show()




    def set_default_info(self):
        _res = SP_py_toolkit.read_json(sp._DEFAULT_INFO_PATH_)
        sp._DEFAULT_INFO_DICT_ = _res


    def select_root_dir(self):
        '''
        - check default info (root) by txt
        - if there is no default info, set path by user input
        '''
        try:
            _sel_path = self._ui.get_selectedpath()
            self.set_root_info_in_tool(_sel_path)
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






    def save_default(self):
        SP_py_toolkit.write_json(sp._DEFAULT_INFO_PATH_, sp._DEFAULT_INFO_DICT_)





    # def set_uiInfo(self):
    #     print 'Query Clear!'
    #     cur_status_gif = self._ui.GP_status_lb.movie()
    #     cur_status_gif.stop()
    #     self.set_progress('CLEAR')
    #
    #     self._ui.set_completer_words(self._info_model.user_list)
    #     self._ui._completer.activated.connect(self.add_tag_with_completer)
    #
    #     self._ui.set_prj_cbWidget(self._info_model.prj_list, self._info_model.All_tasks_dict)
    #     # if str(self._ui.GP_prj_cb.currentText()) == 'Select Project':
    #     #     # self.cur_prj_fps = '24'
    #     #     return
    #     # else:
    #     default_prj = self._info_model.prj_list[0]
    #     default_task_list = self._info_model.All_tasks_dict[default_prj]
    #     self.set_fps_defaultCC(default_task_list)from PyQt5 import QtCore, QtGui, QtWidgets
    #
    #     self.is_queried = True
    #     # self._ui.show_info_in_widget(self._info_model.All_tasks_dict, self._info_model.task_count)
    #




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    try:
        _engine = SPController()
        _engine.run()
    except:
        traceback.print_exc()
    sys.exit(app.exec_())
