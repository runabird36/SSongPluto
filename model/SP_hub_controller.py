

import SP_prj_model
import os, time
from datetime import date

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
    # _m_time = os.path.getmtime(_dir)
    _m_time = max(os.path.getmtime(root) for root,_,_ in os.walk(_dir))
    _formatting_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(_m_time))
    _year = int(time.strftime('%Y', time.localtime(_m_time)))
    _month = int(time.strftime('%m', time.localtime(_m_time)))
    _days = int(time.strftime('%d', time.localtime(_m_time)))


    return _formatting_time, date(_year, _month, _days)



def collect_prj_info(_root_path):
    global _PRJ_HUB_


    # Collect information
    before_sorted = {}
    _today_date = date.today()
    for _dir in os.listdir(_root_path):
        check_path = '/'.join([_root_path, _dir])
        _is_git = is_git_project(check_path)
        _last_time, _last_time_in_date = get_last_modification_time(check_path)


        _prj = SP_prj_model.ProjectModel()
        _prj.name = _dir
        _prj.path = check_path
        _prj.is_git = _is_git
        _prj.time_passed = _today_date - _last_time_in_date
        _prj.latest_date = _last_time

        # print(_dir)
        # print(check_path)
        # print(_is_git)
        # print(_last_time)
        # print('='*50)

        # _PRJ_HUB_.append(_prj)
        before_sorted[_prj.latest_datetime] = _prj

    # Sorting information
    sorted_datetime_list = sorted(before_sorted.keys(), reverse=True)
    for _datetime in sorted_datetime_list:
        _prj_obj = before_sorted.get(_datetime)
        _PRJ_HUB_.append(_prj_obj)






def refresh_data():
    global _PRJ_HUB_
    _PRJ_HUB_ = []

# aa = r'D:\work/work'
# collect_prj_info(aa)
