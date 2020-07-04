from selenium import webdriver
import time
import pyautogui
import sys

IS_PY2 = sys.version_info < (3, 0)

if IS_PY2:
    from Queue import Queue
else:
    from queue import Queue

from threading import Thread

class Worker(Thread):
    """ Thread executing tasks from a given tasks queue """
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as e:
                # An exception happened in this thread
                print(e)
            finally:
                # Mark this task as done, whether an exception happened or not
                self.tasks.task_done()


class ThreadPool:
    """ Pool of threads consuming tasks from a queue """
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """ Add a task to the queue """
        self.tasks.put((func, args, kargs))

    def map(self, func, args_list):
        """ Add a list of tasks to the queue """
        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):
        """ Wait for completion of all the tasks in the queue """
        self.tasks.join()

keys = [
  {"72":True,"82":True,"s":3300,"e":3900,"c":"곰"},
  {"80":True,"84":True,"s":3900,"e":4200,"c":"세"},
  {"65":True,"75":True,"s":4200,"e":4500,"c":"마"},
  {"70":True,"76":True,"s":4500,"e":4850,"c":"리"},
  {"75":True,"82":True,"s":4850,"e":5300,"c":"가"},
  {"71":True,"75":True,"s":5350,"e":5700,"c":"한"},
  {"76":True,"87":True,"s":5700,"e":6000,"c":"집"},
  {"68":True,"80":True,"s":6000,"e":6300,"c":"에"},
  {"68":True,"76":True,"s":6300,"e":6550,"c":"있"},
  {"68":True,"74":True,"s":6550,"e":6800,"c":"어"},
  {"68":True,"75":True,"s":6800,"e":7200,"c":"아"},
  {"16":True,"75":True,"81":True,"s":7200,"e":7500,"c":"빠"},
  {"72":True,"82":True,"s":7500,"e":7800,"c":"곰"},
  {"68":True,"74":True,"s":7800,"e":8200,"c":"엄"},
  {"65":True,"75":True,"s":8200,"e":8500,"c":"마"},
  {"72":True,"82":True,"s":8500,"e":8800,"c":"곰"},
  {"68":True,"79":True,"s":8800,"e":9200,"c":"애"},
  {"76":True,"82":True,"s":9200,"e":9600,"c":"기"},
  {"72":True,"82":True,"s":9600,"e":10000,"c":"곰"},
  {"68":True,"75":True,"s":10500,"e":10850,"c":"아"},
  {"16":True,"75":True,"81":True,"s":10850,"e":11250,"c":"빠"},
  {"72":True,"82":True,"s":11250,"e":11750,"c":"곰"},
  {"68":True,"77":True,"s":11750,"e":12100,"c":"은"},
  {"16":True,"69":True,"78":True,"s":12100,"e":12500,"c":"뚱"},
  {"16":True,"69":True,"78":True,"s":12500,"e":13000,"c":"뚱"},
  {"71":True,"79":True,"s":13000,"e":13600,"c":"해"},
  {"68":True,"74":True,"s":13900,"e":14300,"c":"엄"},
  {"65":True,"75":True,"s":14300,"e":14800,"c":"마"},
  {"72":True,"82":True,"s":14800,"e":15300,"c":"곰"},
  {"68":True,"77":True,"s":15300,"e":15700,"c":"은"},
  {"75":True,"83":True,"s":15700,"e":16100,"c":"날"},
  {"16":True,"76":True,"84":True,"s":16100,"e":16550,"c":"씬"},
  {"71":True,"79":True,"s":16550,"e":17000,"c":"해"},
  {"68":True,"79":True,"s":17300,"e":17800,"c":"애"},
  {"76":True,"82":True,"s":17800,"e":18200,"c":"기"},
  {"72":True,"82":True,"s":18200,"e":18700,"c":"곰"},
  {"68":True,"77":True,"s":18700,"e":19050,"c":"은"},
  {"74":True,"83":True,"s":19050,"e":19300,"c":"너"},
  {"65":True,"78":True,"s":19300,"e":19550,"c":"무"},
  {"76":True,"78":True,"82":True,"s":19550,"e":19800,"c":"귀"},
  {"68":True,"85":True,"s":19800,"e":20000,"c":"여"},
  {"68":True,"74":True,"78":True,"s":20000,"e":20500,"c":"워"},
  {"68":True,"77":True,"s":20800,"e":21200,"c":"으"},
  {"16":True,"77":True,"84":True,"s":21200,"e":21600,"c":"쓱"},
  {"68":True,"77":True,"s":21600,"e":22000,"c":"으"},
  {"16":True,"77":True,"84":True,"s":22000,"e":22400,"c":"쓱"},
  {"75":True,"87":True,"s":22400,"e":22900,"c":"잘"},
  {"71":True,"75":True,"s":22900,"e":23400,"c":"한"},
  {"69":True,"75":True,"s":23400,"e":24400,"c":"다"}
]

pool = ThreadPool(10)

driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)
driver.get('file:///C:/Users/%EC%8B%A0%EB%8F%99%EB%A0%AC/Desktop/dist/index.html')
driver.find_element_by_tag_name('button').click()

def key_press(kkk):
    if int(kkk) != 16:
        pyautogui.keyDown(chr(int(kkk)).lower())
        pyautogui.keyUp(chr(int(kkk)).lower())
    else:
        pyautogui.keyDown('shift')
        pyautogui.keyUp('shift')
    print("key:",kkk)

ss = time.time()
bm = 0
bs = 0
pyautogui.click(500, 500)
for i,key in enumerate(keys):
    s = key.get("s",0)
    e = key.get("e",0)
    c = key.get("c","")
    k = dict(key)
    k.pop("s")
    k.pop("e")
    k.pop("c")
    m = (s + e) / 2
    #time.sleep((s-bs) / 1000.0)
    time.sleep((m-bm) / 1000.0)
    print(k.keys(), s, e, c, "".join(chr(int(kkk)) for kkk in k.keys()))
    for kkk in k.keys():
        pool.add_task(key_press, kkk)
    ee = time.time()
    print(ee-ss)

    bm = m
    bs = s
