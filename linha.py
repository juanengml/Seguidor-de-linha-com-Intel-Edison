import cv2
import numpy as np

LimiarBinarizacao = 125
AreaContornoLimiteMin = 50000
 

class FollowLine(object):
    def __init__(self,frame):
        self.frame = frame

    def TrataImagem(self):
        img = self.frame

        height = np.size(img,0)
        width= np.size(img,1)
        QtdeContornos = 0
        DirecaoASerTomada = 0
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        FrameBinarizado = cv2.threshold(gray,LimiarBinarizacao,255,cv2.THRESH_BINARY)[1]
        FrameBinarizado = cv2.dilate(FrameBinarizado,None,iterations=2)
        FrameBinarizado = cv2.bitwise_not(FrameBinarizado)
        cnts, algo  = cv2.findContours(FrameBinarizado.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
        #print("CNTS: ",cnts,"\nalgo: ",algo)
        cv2.drawContours(img,cnts,-1,(255,0,255),3)
        for c in cnts:
            #print "C:",c
            if cv2.contourArea(c) < AreaContornoLimiteMin:
                continue
                QtdeContornos = QtdeContornos + 1
            (x, y, w, h) = cv2.boundingRect(c)   #x e y: coordenadas do vertice superior esquerdo
                                                 #w e h: respectivamente largura e altura do retangulo
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            CoordenadaXCentroContorno = (x+x+w)/2
            CoordenadaYCentroContorno = (y+y+h)/2
            PontoCentralContorno = (CoordenadaXCentroContorno,CoordenadaYCentroContorno)
            cv2.circle(img, PontoCentralContorno, 1, (0, 0, 0), 5)
            DirecaoASerTomada = CoordenadaXCentroContorno - (width/2)   #em relacao a linha central
        cv2.line(img,(width/2,0),(width/2,height),(255,0,0),2)
        if (QtdeContornos > 1 and QtdeContorno < 0):
                  cv2.line(img,PontoCentralContorno,(width/2,CoordenadaYCentroContorno),(231,255,0),1)
        cv2.imwrite('blah.jpg',img)
        
        #cv2.imshow('Analise de rota',img)
        #cv2.waitKey(10)
        return DirecaoASerTomada, QtdeContornos
