import motores

m = motores.Robot(True)

while True:
  menu = raw_input("CMD: ")
  if menu == "w": m.run()
  if menu == "a": m.left()
  if menu == "d": m.right()
  if menu == "p": m.stop()
  if menu == "s": m.back()
