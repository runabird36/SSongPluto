
from datetime import datetime

class ProjectModel():
    def __init__(self):
        self._name = ""
        self._path = ""
        self._is_git = False
        self._latest_date = ""
        self._latest_date_in_datetime = None
        self._time_passed = None
        self._type = ""


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        self._name = _name


    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, _path):
        self._path = _path

    @property
    def is_git(self):
        return self._is_git

    @is_git.setter
    def is_git(self, _is_git):
        self._is_git = _is_git


    @property
    def latest_date(self):
        return self._latest_date

    @property
    def latest_datetime(self):
        return self._latest_date_in_datetime

    @latest_date.setter
    def latest_date(self, _l_date):
        self._latest_date = _l_date
        self._latest_date_in_datetime = datetime.strptime(_l_date, "%Y-%m-%d %H:%M:%S")


    @property
    def time_passed(self):
        return self._time_passed

    @time_passed.setter
    def time_passed(self, _time_passed):
        self._time_passed = _time_passed


    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, _type):
        self._type = _type
