import RPi.GPIO as GPIO
import time

# Konfigurasi mode pin BCM dan menghilangkan peringatan GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Definisikan pin trigger dan echo
trigger = 26
echo = 16

# Konfigurasi pin sebagai output (trigger) dan input (echo)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

# Set pin trigger awalnya ke LOW
GPIO.output(trigger, GPIO.LOW)

# Fungsi untuk mengukur jarak


def get_range():
    # Aktifkan trigger selama 10 mikrodetik
    GPIO.output(trigger, True)
    time.sleep(0.00001)
    GPIO.output(trigger, False)

    # Inisialisasi waktu awal dan timeout counter
    timeout_counter = int(time.time())
    start = time.time()

    # Tunggu echo menjadi HIGH (1) atau timeout maksimum 3 detik
    while GPIO.input(echo) == 0 and (int(time.time()) - timeout_counter) < 3:
        start = time.time()

    # Reset timeout counter
    timeout_counter = int(time.time())
    stop = time.time()

    # Tunggu echo menjadi LOW (0) atau timeout maksimum 3 detik
    while GPIO.input(echo) == 1 and (int(time.time()) - timeout_counter) < 3:
        stop = time.time()

    # Hitung waktu yang diperlukan untuk pulsa ultrasonik kembali
    elapsed = stop - start

    # Hitung jarak dalam centimeter menggunakan kecepatan suara
    distance = elapsed * 34320
    distance = distance / 2

    return distance


# Loop tak terbatas untuk mengukur jarak terus-menerus
while True:
    jarak = get_range()
    print('Jarak terukur: %.2f Cm' % jarak)
    time.sleep(1)
