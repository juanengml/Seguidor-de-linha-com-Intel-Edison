import motores
from time import sleep

robot = motores.Robot(True)
TEMPO = 0.8

while True:
  data = open("data.txt").read().split()[0]
  print(data)
  if int(data) > 108 and int(data) < 277:
     print "Direita: ",data
     robot.left()
     sleep(TEMPO)
     robot.stop()
     sleep(1)

  if int(data) < -77 and int(data) > -263:
     print "Esquerda: ",data
     robot.right()
     sleep(TEMPO)
     robot.stop()
     sleep(1)
  if int(data) > -76 and int(data) < 107:
     print "Meio"
     robot.run()
     sleep(TEMPO)
     robot.stop()
     sleep(1)
  if int(data) == 0:
     print "PARADO"
     robot.stop()

  sleep(TEMPO)
  print("Novo Loop")
