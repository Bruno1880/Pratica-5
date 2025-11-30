import RPi.GPIO as GPIO #importa a biblioteca porém com o apelido GPIO
import time # importa a biblioteca time

# Configura os pinos
LED_PIN = 18      # GPIO 18 para LED
BOTAO_PIN = 15    # GPIO 17 para botão

# Configuração da identificação dos pinos
GPIO.setmode(GPIO.BCM) # mapeamento pelo canal do chip Broadcom (SOC) interno
GPIO.setup(LED_PIN, GPIO.OUT) #configura o LED_PIN como saída
GPIO.setup(BOTAO_PIN, GPIO.IN, GPIO.PUD_UP) #configura o BOTAO_PIN como entrada e deixa ele em pull-up

# Estado inicial do LED
GPIO.output(LED_PIN, GPIO.LOW)

print("Programa iniciado: Pressione o botão para acender o LED") #mostra a mensagem na tela indicar que o programa iniciou

print("Pressione Ctrl+C para sair") #mostra mensagem para indicar como parar o programa

try:
	while True:
		estado_button = GPIO.input(BOTAO_PIN) #variavel para armazenar o estado do botão
		if estado_button == GPIO.LOW:  # Botão pressionado
			GPIO.output(LED_PIN, GPIO.HIGH)    # Acende LED
		else:  # Botão solto
			GPIO.output(LED_PIN, GPIO.LOW)     # Apaga LED
		time.sleep(1)  # delay de 1 segundo

except KeyboardInterrupt:
	print("\nPrograma finalizado pelo usuário")

finally:	#quando o programa finalizar executa o que estiver abaixo
	GPIO.cleanup() # Limpa os pinos GPIO
	print("As GPIO foram limpas") #mostra a mensagem que as GPIO foram limpas