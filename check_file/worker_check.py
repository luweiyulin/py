
#! /usr/bin env python3
# -- coding:utf-8 --


import threading
import os


class WorkerCheck (threading.Thread):
    def __init__(self, queue, file="", prefix="", debug=False):
        threading.Thread.__init__(self)
        self.queue = queue
        # self.file = file if file != "" else "F:/dep/code/python/jdm/check_file/data/test/target/change.txt"
        self.file = file if file != "" else "C:/Users/mysteryyun/Desktop/test/target"

        # self.prefix = prefix if prefix != "" else "F:/dep/code/python/jdm/check_file/data/test/Python_master"
        self.prefix = prefix if prefix != "" else "C:/Users/mysteryyun/Desktop/test/Python_master"

        self.debug = debug

    def run(self):
        print("-- WorkerCheck::run start")

        with open(self.file) as f:
            for line in f:
                line = line.strip('\r\n \t')
                if self.debug:
                    print("-- WorkerCheck line |", line)

                if os.path.exists(os.path.join(self.prefix, line)):
                    self.queue.put([1, line])
                else:
                    self.queue.put([2, line])

            f.close()

        self.queue.put([99, ""])
        print("-- WorkerCheck::run stop")
