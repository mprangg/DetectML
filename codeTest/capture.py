import freenect
import cv2
import os

PathPic = "/home/uawsscu/PycharmProjects/DetectML/pic/"

def createDataSet(nameObject):
    nameObject = PathPic+nameObject+""
    try:
        if not os.path.exists('POS'):
            os.makedirs(nameObject)
    except :
        print "aa"


def get_video():
    array, _ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array


def capTrain(nameDirectory):
    setPath = '/home/uawsscu/PycharmProjects/project3/image/' + nameDirectory + '.jpg'
    while 1:
        print "ok"
        frame = get_video()
        cv2.imshow('RGB image', frame)

        params = list()
        crop_img = frame[120:420, 213:456]  # Crop from x, y, w, h -> 100, 200, 300, 400
        # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
        cv2.imwrite(setPath, crop_img, params)

        break

    cv2.destroyAllWindows()

def capTest():
    setPath = '/home/uawsscu/PycharmProjects/DetectML/codeTest/withImage/w.jpg'
    while 1:
        print "ok"
        frame = get_video()
        cv2.imshow('RGB image', frame)

        params = list()
        crop_img = frame[120:420, 213:456]  # Crop from x, y, w, h -> 100, 200, 300, 400
        # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
        cv2.imwrite(setPath, crop_img, params)

        break

    cv2.destroyAllWindows()

#cap_ture('messigray')
createDataSet("van")