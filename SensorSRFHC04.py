import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trigger = 26
echo = 16

# Definisikan pin untuk tiga lampu
lamp_pin = 4

# Inisialisasi GPIO untuk masing-masing lampu
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(lamp_pin, GPIO.OUT)


GPIO.output(trigger, GPIO.LOW)


def get_range():
    GPIO.output(trigger, True)
    time.sleep(0.00001)
    GPIO.output(trigger, False)
    timeout_counter = int(time.time())
    start = time.time()

    while GPIO.input(echo) == 0 and (int(time.time()) - timeout_counter) < 3:
        start = time.time()
        timeout_counter = int(time.time())

    stop = time.time()

    while GPIO.input(echo) == 1 and (int(time.time()) - timeout_counter) < 3:
        stop = time.time()

    elapsed = stop - start
    distance = elapsed * 34320
    distance = distance / 2
    return distance


try:
    while True:
        jarak = get_range()
        print('Jarak terukur adalah: %.2f Cm' % jarak)

        if jarak < 8:
            for i in range(3):
                GPIO.output(lamp_pin, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(lamp_pin, GPIO.LOW)
                time.sleep(0.5)
        elif 8 <= jarak <= 20:
            for i in range(5):
                GPIO.output(lamp_pin, GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(lamp_pin, GPIO.LOW)
                time.sleep(0.2)
        else:
            GPIO.output(lamp_pin, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
