import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trigger = 26
echo = 16

# Definisikan pin untuk tiga lampu
lamp_pin_1 = Ganti Dek
lamp_pin_2 = Ini Lagi
lamp_pin_3 = ini Juga

# Inisialisasi GPIO untuk masing-masing lampu
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(lamp_pin_1, GPIO.OUT)
GPIO.setup(lamp_pin_2, GPIO.OUT)
GPIO.setup(lamp_pin_3, GPIO.OUT)

GPIO.output(trigger, GPIO.LOW)

def get_range():
    # Fungsi untuk mengukur jarak, seperti sebelumnya

try:
    while True:
        jarak = get_range()
        print('Jarak terukur: %.2f Cm' % jarak)

        if jarak < 8:
            # Nyalakan semua lampu jika jarak kurang dari 8 cm
            GPIO.output(lamp_pin_1, GPIO.HIGH)
            GPIO.output(lamp_pin_2, GPIO.HIGH)
            GPIO.output(lamp_pin_3, GPIO.HIGH)
        else:
            # Matikan semua lampu jika jarak lebih dari atau sama dengan 8 cm
            GPIO.output(lamp_pin_1, GPIO.LOW)
            GPIO.output(lamp_pin_2, GPIO.LOW)
            GPIO.output(lamp_pin_3, GPIO.LOW)

        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
