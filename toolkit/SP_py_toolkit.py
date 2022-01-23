import json, os
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, traceback

def write_json(_path, _data):
    with open(_path, 'w') as out_json:
        json.dump(_data, out_json, indent=4)


def read_json(_path):
    if os.path.exists(_path) == False:
        write_json(_path, {})
    with open(_path, 'r') as in_json:
        _data = json.load(in_json)

    return _data







class WorkerSignals(QtCore.QObject):

    error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal(list)
    progress = QtCore.pyqtSignal(int)
    finished = QtCore.pyqtSignal(int)




class Worker(QtCore.QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''
    def __init__(self, _idx, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self._work_idx = _idx
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()


    def run(self):
        try:

            result = self.fn(*self.args, **self.kwargs)


        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit([self._work_idx, result])  # Return the result of the processing
        finally:
            self.signals.finished.emit(self._work_idx)  # Done




class Pool(QtCore.QObject):
    finished = QtCore.pyqtSignal(str)
    def __init__(self):
        super(Pool, self).__init__()
        self.pool = QtCore.QThreadPool()


        self.job_list = []
        self.job_status_list = []
        self.job_result_list = []

        self.pool.setMaxThreadCount(5)


    def add_job(self, _fn):

        self.job_list.append(_fn)
        self.job_status_list.append(False)
        self.job_result_list.append(None)

    def check_pool_finished(self, _job_idx):
        self.job_status_list[_job_idx] = True

        if False in self.job_status_list:
            pass
            self.finished.emit("Yet")
        else:
            self.finished.emit("Clear")


    def update_job_result_list(self, res_list):

        job_idx = res_list[0]
        job_res = res_list[1]
        self.job_result_list[job_idx] = job_res


    def start_pool(self):
        for _idx, _job in enumerate(self.job_list):
            worker = Worker(_idx, _job)
            worker.signals.finished.connect(self.check_pool_finished)
            worker.signals.result.connect(self.update_job_result_list)

            self.pool.start(worker)
        # self.pool.waitForDone()




    def get_res_list(self):
        return self.job_result_list


    def reset_all(self):
        self.pool.clear()
        self.job_list = []
        self.job_status_list = []
        self.job_result_list = []
