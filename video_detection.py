
import cv2

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
hat=cv2.imread('C:/Users/kusha/PycharmProjects/Filters_cv/Filters/hat.png')
glass=cv2.imread('C:/Users/kusha/PycharmProjects/Filters_cv/Filters/glasses.png')
dog=cv2.imread('C:/Users/kusha/PycharmProjects/Filters_cv/Filters/dog.png')

def put_dog_filter(dog, fc, x, y, w, h):
    face_width = w
    face_height = h

    dog = cv2.resize(dog, (int(face_width * 1.5), int(face_height * 1.95)))
    for i in range(int(face_height * 1.75)):
        for j in range(int(face_width * 1.5)):
            for k in range(3):
                if dog[i][j][k] < 235:
                    fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = dog[i][j][k]
    return fc

def put_hat(hat, fc, x, y, w, h):
    face_width = w
    face_height = h

    hat_width = face_width + 1
    hat_height = int(0.50 * face_height) + 1

    hat = cv2.resize(hat, (hat_width, hat_height))

    for i in range(hat_height):
        for j in range(hat_width):
            for k in range(3):
                if hat[i][j][k] < 235:
                    fc[y + i - int(0.40 * face_height)][x + j][k] = hat[i][j][k]
    return fc


def put_glass(glass, fc, x, y, w, h):
    face_width = w
    face_height = h

    hat_width = face_width + 1
    hat_height = int(0.50 * face_height) + 1

    glass = cv2.resize(glass, (hat_width, hat_height))

    for i in range(hat_height):
        for j in range(hat_width):
            for k in range(3):
                if glass[i][j][k] < 235:
                    fc[y + i - int(-0.20 * face_height)][x + j][k] = glass[i][j][k]
    return fc
global choise

choice = 0
print('enter your choice filter to launch that: 1="put hat & glasses" ,any number="put fog filters" ')
choise= int(input('enter your choice:'))
webcam = cv2.VideoCapture(0)
while True:
    size=4
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    fl = face.detectMultiScale(gray,1.19,7)

    for (x, y, w, h) in fl:
        if choise ==1:
            im = put_hat(hat, im, x, y, w, h)
            im = put_glass(glass, im, x, y, w, h)

        else:
            im = put_dog_filter(dog, im, x, y, w, h)

    cv2.imshow('Hat & glasses',im)
    key = cv2.waitKey(30) & 0xff
    if key == 27:  # The Esc key
       break