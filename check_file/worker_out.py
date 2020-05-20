
#! /usr/bin env python3
# -- coding:utf-8 --


import threading
import os


class WorkerOut (threading.Thread):
    def __init__(self, queue, mod="", add="", prefix="", debug=False):
        threading.Thread.__init__(self)
        self.queue = queue
        self.mod = mod if mod != "" else "mod.txt"
        self.add = add if add != "" else "add.txt"
        self.prefix = prefix if prefix != "" else "C:/Users/mysteryyun/Desktop/test/target"
        self.debug = debug

    def run(self):
        print("-- WorkerOut::run start")

        mod = open(os.path.join(self.prefix, self.mod), mode="w")
        add = open(os.path.join(self.prefix, self.add), mode="w")

        line = [0, ""]
        while (line[0] != 99):
            line = self.queue.get()
            if self.debug:
                print("-- WorkerOut line |", line)
            
            if line[0] == 1 :
                mod.write(line[1] + "\n")
            elif line[0] == 2:
                add.write(line[1] + "\n")

        mod.close()
        add.close()

        print("-- WorkerOut::run stop")
