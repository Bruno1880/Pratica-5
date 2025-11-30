[Unit]
Description= parte_1
After=multi-user.target
[Service]
ExecStart=/home/sel/8294/Parte_1_Botao_LED.py
ExecStop=/home/sel/8294/Parte_2_Controle_PWM.py
user=SEL
[Install]