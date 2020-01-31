import cv2

windowName = "Pokedex"
cv2.namedWindow(windowName)
cam = cv2.VideoCapture(0)

if cam.isOpened():
    rval, frame = cam.read()
else:
    rval = False

while rval:
    cv2.imshow(windowName, frame)
    rval, frame = cam.read()
    key = cv2.waitKey(20)
    if key == 27:  # exit on ESC
        break

cam.release()
cv2.destroyWindow(windowName)