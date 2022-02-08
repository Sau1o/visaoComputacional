import cv2

rastreador = cv2.TrackerMIL_create()

video = cv2.VideoCapture('race.mp4')
ok,frame = video.read()

bbox = cv2.selectROI(frame)

ok = rastreador.init(frame, bbox)

while True:
    ok,frame = video.read()

    if not ok:
        break

    ok, bbox = rastreador.update(frame)

    if ok:
        (x,y,w,h) = [int(v) for v in bbox]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2,1)
    else:
        cv2.putText(frame,'ERRO',(100,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv2.imshow('Rastreamento', frame)
    if cv2.waitKey(1) & 0XFF == 27:
        break