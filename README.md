# Seguidor-de-linha-com-Intel-Edison
Usando OpenCV para fazer um robô seguidor de linha com interface web usando flask

## EMBARCADO UTILIZADO

![edison](https://static.electronicsweekly.com/news/wp-content/uploads/sites/16/2014/11/RS283-2-Intel_Edison_board_Arduino.png)

--- 

#### Esse seguidor de linha é bem simples, estou usando alguns filtros para tratar imagem e poder ter as entradas para acionar o motores.

### INSTALL LIB 
terminal_2_@terminal_2_$ opkg install opencv 
<br>
<img src="https://upload.wikimedia.org/wikipedia/commons/3/32/OpenCV_Logo_with_text_svg_version.svg" width="200" height="100">
<br>
terminal_2_@terminal_2_$ pip install flask
<br>
<img src="https://i0.wp.com/pythonprogramming.altervista.org/wp-content/uploads/2019/06/flask1.png?fit=438%2C245&ssl=1"  width="200" height="100">




#### INSTRUÇÕES 

 Com a placa conectada basta digitar os comandos a baixo
 
 terminal_1_@terminal_1_$ python webvision.py
  
 terminal_2_@terminal_2_$ python engine.py
 

