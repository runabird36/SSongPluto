'''

Write all path information


'''

import sys
import os
script_path = os.path.dirname(os.path.abspath( __file__ ))
# _main_path = "Z:/backstage/multi/GiantSubmitter"
script_path = script_path.replace('\\', '/')
_main_path = script_path
sys.path.append(_main_path+'/icons')
sys.path.append(_main_path+'/model')
sys.path.append(_main_path+'/toolkit')
sys.path.append(_main_path+'/toolkit/GP_video_tool')
sys.path.append(_main_path+'/view')
sys.path.append(_main_path+'/view/custom_view')

sys.path.append(_main_path+'/donwload/certs')







hide_icon = _main_path+'/icons/hideAsset.png'
max_icon = _main_path+'/icons/max.png'
close_icon = _main_path+'/icons/closeAsset.png'
folder_gif_icon = _main_path +'/icons/folder_icon.gif'
loading_gif_icon = _main_path +'/icons/loading2.gif'
clear_gif_icon = _main_path +'/icons/check_check_jump.gif'












_ROOT_PATH_ = ''
_DEFAULT_INFO_DICT_ = {}
_DEFAULT_INFO_PATH_ = _main_path + '/DEFAULT_INFO.json'


def set_root_path(_path):
    global _DEFAULT_INFO_DICT_
    _DEFAULT_INFO_DICT_['ROOT'] = _path

def get_root_path():
    global _DEFAULT_INFO_DICT_
    return _DEFAULT_INFO_DICT_.get('ROOT')
