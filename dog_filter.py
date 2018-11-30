import cv2

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
filename='C:/Users/kusha/PycharmProjects/Filters_cv/images/gs.JPG'
img=cv2.imread(filename)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
fl=face.detectMultiScale(gray,1.09,7)
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

for (x, y, w, h) in fl:
    frame = put_dog_filter(dog, img, x, y, w, h)

cv2.imshow('image',frame)
cv2.waitKey(20000)& 0xff
cv2.destroyAllWindows()