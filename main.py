from machine import Pin
import time

# Defina o pino para o LED
led_pin = 2  # Substitua pelo pino correto

# Configuração do pino como saída
led = Pin(led_pin, Pin.OUT)

# Função para fazer o LED piscar
def piscar_led(tempo):
    led.value(1)
    time.sleep(tempo)
    led.value(0)
    time.sleep(tempo)

# Loop principal
while True:
    piscar_led(0.5)