

import SP_prj_model
import os, time

_PRJ_HUB_ = []

def is_git_project(_check_tar_dir):
    if '.git' in os.listdir(_check_tar_dir):
        return True
    else:
        for _dir in os.listdir(_check_tar_dir):
            check_fullpath = '/'.join([_check_tar_dir, _dir])
            if os.path.isfile(check_fullpath) == True:
                continue
            if '.git' in os.listdir(check_fullpath):
                return True
        return False



def get_last_modification_time(_dir):
    _m_time = os.path.getmtime(_dir)
    _formatting_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(_m_time))
    return _formatting_time



def collect_prj_info(_root_path):
    global _PRJ_HUB_
    for _dir in os.listdir(_root_path):
        check_path = '/'.join([_root_path, _dir])
        _is_git = is_git_project(check_path)
        _last_time = get_last_modification_time(check_path)


        _prj = SP_prj_model.ProjectModel()
        _prj.name = _dir
        _prj.path = check_path
        _prj.is_git = _is_git
        _prj.latest_date = _last_time






aa = r'D:\work'
collect_prj_info(aa)
