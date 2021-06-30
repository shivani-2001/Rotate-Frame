import cv2
import numpy as np

video = cv2.VideoCapture('number_plate_blur.avi')
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter('final.avi', cv2.VideoWriter_fourcc(*'FMP4'), 25, (width, height))

while True:
    ret, frame = video.read()
    if ret==True:
        image = cv2.rotate(frame, cv2.ROTATE_180)
        writer.write(image)
        cv2.imshow("Application", image)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        break

video.release()
writer.release()
cv2.destroyAllWindows()
