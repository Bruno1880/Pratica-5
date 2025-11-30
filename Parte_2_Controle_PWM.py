import RPi.GPIO as GPIO #importa a biblioteca porém com o apelido GPIO
from  time import sleep #importa a função sleep da biblioteca time

LED_PIN = 18 #configura o pino 18 para o LED
GPIO.setmode(GPIO.BOARD) # mapeamento pelo canal do chip Broadcom ( SOC )
GPIO.setup(LED_PIN, GPIO.OUT) # configurando o LED_PIN como saída

pwm = GPIO.PWM(LED_PIN, 100) # configurando o pwm para 100 Hz no LED_PIN
pwm.start(0) #inicializa o pwm na frequência 0

print("comeco")

try:
	while True:
		for dc in range(101): #vai alterando o duty cycle de 0 a 100
			pwm.ChangeDutyCycle(dc) #duty cycle alterando conforme a variável dc recebe os valores do range através do for
			sleep(1) #para por 1 segundo
except KeyboardInterrupt: #se ctrl + C for pressionado encerra o programa e mostra a mensagem
	print("Programa finalizado")
finally:
	pwm.stop() #para o pwm
	GPIO.cleanup() #limpa os GPIOs
	print("As GPIO foram limpas") #mostra a mensagem