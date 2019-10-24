import cv2
from PIL import Image
import pytesseract
import re
import numpy as np


def capture_food():
    url = 'http://192.168.0.154:8080/video'
    cap = cv2.VideoCapture(url)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if frame is not None:
            cv2.imshow('frame', gray)
            cv2.imwrite(filename='saved_img.jpg', img=frame)
        q = cv2.waitKey(1)
        if q == ord("q"):
            break
    cv2.destroyAllWindows()
    im = Image.open("saved_img.jpg")

    text = pytesseract.image_to_string(im, lang='spa')
    return text


def find_text(text):
    result = re.findall(r'E-\d+', text)
    result_2 = re.findall(r'E\d+', text)
    return result, result_2


def get_homogenic_data(result, result_2):
    values = []
    for value in result:        
        values.append(value)
    for value in result_2:       
        values.append(value)
    for value in values:
        if "E-" in value:
            values = [item.replace('E-','E') for item in values]
            values = values.apply(lambda item: item.str.strip())           
        else:
            return values


def get_allergies_dataframe(df, values):
    allergies = df[df['id'].isin(values)]
    return allergies

