# import RPi.GPIO as GPIO
# import record
import time
import csv
from myThread import MyThread
import threading
# ===================================================
# 实验控制量
#
# ==============================================
# ==============================================
# 数据记录线程
# def record_csv(D11=17,l=22,f="/sys/bus/w1/devices/28-01201cd1596c/w1_slave"):
#     print("开始检测数据")
#     i = 0
#     a = {}
#     try:
#         while True:
#             time.sleep(1)
#             a['时间'] = time.strftime("%Y%m%d %X", time.localtime())
#             result = record.D11_temp_humidity(D11)
#             if result:
#                 a['温度1'] = record.temperature(f)
#                 x, y = result
#                 a['温度2'] = x
#                 a['湿度'] = y
#                 a['亮度'] = record.light(l)
#             with open("htl.csv", "a", encoding="utf-8") as file:
#                 writer = csv.writer(file)
#                 for i in a:
#                     writer.writerow(i)
#     except:
#         GPIO.cleanup()
# ===================================================
# 语音对话模块
def loop(x):
    time.sleep(x)
    print("第一个进程，停止结束")

def loop2(x):
    for i in range(2):
        time.sleep(x)
        print("停止:", i)
    print("第二个进程，停止结束")
# ==============================================
# 人脸识别模块

# ==============================================
# 线程控制
funcs = [ loop, loop2]
x = [5, 4]
def main():
    nfuncs = range(len(funcs))
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], x[i], funcs[i].__name__)
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    # for i in nfuncs:
        # threads[i].join()
        # print(threads[i].getResult())
    print("all over!")

if __name__ == "__main__":
    main()