import RPi.GPIO as GPIO
import time
import pandas
import csv
print("正在启动中--------------------")
GPIO.setmode(GPIO.BCM)
print("模式启动!!!!!!!!")


MAX_UNCHANGE_COUNT = 100

STATE_INIT_PULL_DOWN = 1
STATE_INIT_PULL_UP = 2
STATE_DATA_FIRST_PULL_DOWN = 3
STATE_DATA_PULL_UP = 4
STATE_DATA_PULL_DOWN = 5


def temperature(f):
    tfile = open(f)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temperature = temperature / 1000
    print(temperature)
    return temperature

def D11_temp_humidity(t):
    DHTPIN = t
    GPIO.setup(DHTPIN, GPIO.OUT)
    GPIO.output(DHTPIN, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(DHTPIN, GPIO.LOW)
    time.sleep(0.02)
    GPIO.setup(DHTPIN, GPIO.IN, GPIO.PUD_UP)

    unchanged_count = 0
    last = -1
    data = []
    while True:
        current = GPIO.input(DHTPIN)
        data.append(current)
        if last != current:
            unchanged_count = 0
            last = current
        else:
            unchanged_count += 1
            if unchanged_count > MAX_UNCHANGE_COUNT:
                break

    state = STATE_INIT_PULL_DOWN

    lengths = []
    current_length = 0

    for current in data:
        current_length += 1

        if state == STATE_INIT_PULL_DOWN:
            if current == GPIO.LOW:
                state = STATE_INIT_PULL_UP
            else:
                continue
        if state == STATE_INIT_PULL_UP:
            if current == GPIO.HIGH:
                state = STATE_DATA_FIRST_PULL_DOWN
            else:
                continue
        if state == STATE_DATA_FIRST_PULL_DOWN:
            if current == GPIO.LOW:
                state = STATE_DATA_PULL_UP
            else:
                continue
        if state == STATE_DATA_PULL_UP:
            if current == GPIO.HIGH:
                current_length = 0
                state = STATE_DATA_PULL_DOWN
            else:
                continue
        if state == STATE_DATA_PULL_DOWN:
            if current == GPIO.LOW:
                lengths.append(current_length)
                state = STATE_DATA_PULL_UP
            else:
                continue
    if len(lengths) != 40:
        print("Data not good, skip")
        return False

    shortest_pull_up = min(lengths)
    longest_pull_up = max(lengths)
    halfway = (longest_pull_up + shortest_pull_up) / 2
    bits = []
    the_bytes = []
    byte = 0

    for length in lengths:
        bit = 0
        if length > halfway:
            bit = 1
        bits.append(bit)
    # print("bits: %s, length: %d" % (bits, len(bits)))
    for i in range(0, len(bits)):
        byte = byte << 1
        if (bits[i]):
            byte = byte | 1
        else:
            byte = byte | 0
        if ((i + 1) % 8 == 0):
            the_bytes.append(byte)
            byte = 0
    # print(the_bytes)
    checksum = (the_bytes[0] + the_bytes[1] + the_bytes[2] + the_bytes[3]) & 0xFF
    if the_bytes[4] != checksum:
        print("Data not good, skip")
        return False

    return [the_bytes[0], the_bytes[2]]

def light( t ):
    x = 0
    pin_pqrs = t
    GPIO.setup(pin_pqrs, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    status = GPIO.input(pin_pqrs)
    if status == False:
        print('能见度正常')
        x = '亮'
    else:
        print('哇塞，好黑')
        x = '黑'
    return x

def camera():
    pass

def sound_record():
    pass

# def record_csv(D11=17,l=22,f="/sys/bus/w1/devices/28-01201cd1596c/w1_slave"):
#     print("开始检测数据")
#     i = 0
#     a = {}
#     try:
#         while True:
#             time.sleep(1)
#             a['时间'] = time.strftime("%Y%m%d %X", time.localtime())
#             result = D11_temp_humidity(D11)
#             if result:
#                 a['温度1'] = temperature(f)
#                 x, y = result
#                 a['温度2'] = x
#                 a['湿度'] = y
#                 a['亮度'] = light(l)
#             with open("htl.csv", "a", encoding="utf-8") as file:
#                 writer = csv.writer(file)
#                 for i in a:
#                     writer.writerow(i)
#     except:
#         GPIO.cleanup()


def main():
    pass

if __name__ == '__main__':
    main()

