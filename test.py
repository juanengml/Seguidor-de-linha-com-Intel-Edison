import cv2
import numpy as np
import linha

camera = cv2.VideoCapture(0)

for p in range(10):
  grad,Frame = camera.read()

grad, Frame = camera.read()

line = linha.FollowLine(Frame)
print(line.TrataImagem())

