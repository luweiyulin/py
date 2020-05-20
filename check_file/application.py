
#! /usr/bin env python3
# -- coding:utf-8 --


from queue import Queue
from worker_check import WorkerCheck
from worker_out import WorkerOut


class Application:
    def __init__(self):
        self.queue = Queue()
        self.workerCheck = WorkerCheck(queue=self.queue, debug=True)
        self.workerOut = WorkerOut(queue=self.queue, debug=True)

    def run(self):
        print("-- Application::run start")
        self.workerOut.start()
        self.workerCheck.start()

        self.workerCheck.join()
        self.workerOut.join()
        print("-- Application::run stop")
