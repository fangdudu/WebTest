# encoding = utf-8

import threading
import time

# 创建一个线程子类
from concurrent.futures.thread import ThreadPoolExecutor


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)  # 线程的初始化
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        moyu_time(self.name, self.counter, 10)
        print("退出线程：" + self.name)


def moyu_time(name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s 开始摸鱼 %s" % (name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        counter -= 1


if __name__ == '__main__':
    pool = ThreadPoolExecutor(20)
    for i in range(1, 5):
        pool.submit(moyu_time('xiaoshuaib' + str(i), 1, 3))
