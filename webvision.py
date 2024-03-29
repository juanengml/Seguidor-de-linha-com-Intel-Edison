from flask import Flask, Response
import cv2
import linha
import os
import motores

bot = motores.Robot(True)

class Camera(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def get_frame(self):
	ret, frame = self.cap.read()
        line = linha.FollowLine(frame)
        data = line.TrataImagem()
        direcao =  int(data[0])
        os.system("echo '%s' > data.txt"  % (direcao))
	#cv2.imwrite('blah.jpg',frame)
	return open('blah.jpg', 'rb').read()


app = Flask(__name__)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
