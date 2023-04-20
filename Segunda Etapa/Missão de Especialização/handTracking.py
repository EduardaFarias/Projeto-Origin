import cv2      # Importando a biblioteca OpenCv
import mediapipe as mp      # Importando a biblioteca mediaPipe

# Essa variável vai abrir nossa webcam, passei como parâmetro a câmera 1
video = cv2.VideoCapture(0) 

# vamos usar a solução hands para ter o mapeamento da mão, assim, vou criar a variável 
# hand, que vai ser resposável pelas configurações do mediapipe
hand = mp.solutions.hands

# Aqui eu estou configurando o número de mãos que o algoritmo irá reconhecer
# Nesse caso ele irá receber apenas 1 mão
Hand = hand.Hands(max_num_hands = 1)

# Variável de configuração, essa váriavel é responsável por desenhar
# as ligações entre os pontos das mãos

mpDraw = mp.solutions.drawing_utils

## Loop para li8gar a câmera
while True:
    check, img = video.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    handsPoints = results.multi_hand_landmarks
    h, w = img.shape
    pontos = []
    if handsPoints:
        for points in handsPoints:
            mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)
            for id,cord in enumerate(points.landmark):
                cx, cv = int(cord.x*w), int(cord.y*h)
                #cv2.putText(img,str(id),(cx,cy+10), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)
                pontos.append(cx,cy)
        dedos = [8,12,16,20]
        contador = 0
        if points:
            if pontos[4][0] < pontos[2][0]:
                contador += 1
            for x in dedos:
                if pontos[x][1] < pontos[x-2][1]:
                    contador += 1
        cv2.rectangle(img,(80,10),(200,100),(255,0,0),-1)
        cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SIMPLEX,4(255,255,255),5)


    cv2.imshow("Imagem", img)
    cv2.waitKey(1)




