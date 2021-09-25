import cv2 as cv
import sys
class main:
    def __init__(self,path) -> None:
            swap_face=self.staticFace(path)
            self.detectAndSwap(frame,swap_face)
    def detectAndSwap(self,frame,swap_face):
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_gray = cv.equalizeHist(frame_gray)
        faces = face_cascade.detectMultiScale(frame_gray)
        for (x,y,w,h) in faces:
            swap_face=cv.resize(swap_face,(w,h),interpolation=cv.INTER_CUBIC)
            frame = cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0))
            frame[y:y+h,x:x+w]=swap_face
        cv.imshow('Capture - Face detection', frame)

    def staticFace(self,img_path):
        img=cv.imread(img_path)
        img_grey=cv.equalizeHist(cv.cvtColor(img,cv.COLOR_BGR2GRAY))
        swap_face = face_cascade.detectMultiScale(img_grey)
        x,y,w,h=swap_face.reshape(-1)
        return img[y:y+h,x:x+w]


face_cascade_name = 'cascades/haarcascade_frontalface_alt.xml'
face_cascade = cv.CascadeClassifier()
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    sys.exit('Error loading..')
camera_device = 0
cap = cv.VideoCapture(camera_device)
if not cap.isOpened:
    print('Camera Error')
while True:
    ret, frame = cap.read()
    if frame is None:
        sys.exit('--(!) No captured frame -- Break!')
    ob=main('assets/face2.jpeg')
    if cv.waitKey(10) == 27:
        break