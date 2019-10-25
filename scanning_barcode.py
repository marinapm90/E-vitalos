import cv2
from PIL import Image
from pyzbar.pyzbar import decode
import requests
import json


def capture_barcode():
    url = 'http://192.168.20.143:8080/video'
    cap = cv2.VideoCapture(url)
    lastcode = ""

    while True:

        _, frame = cap.read()

        frame = cv2.flip(frame, 1) 

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 

        barcodes = decode(gray)    

        for barcode in barcodes:

            (x, y, w, h) = barcode.rect

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            barcodeType = barcode.type
            barcodeData = barcode.data.decode("utf-8")

            datatext = f"Data: {barcodeData}"
            datatype = f"Type: {barcodeType}"
            cv2.putText(frame, datatext, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
            cv2.putText(frame, datatype, (x,y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)

            if barcodeData != lastcode:
               lastcode = barcodeData

        cv2.imshow("original", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return barcodeData


def nutri_score(barcodeData):
    url_api = "https://world.openfoodfacts.org/api/v0/product/" + barcodeData + ".json"

    response = requests.get(url_api)

    contenant = response.content
    res = json.loads(contenant)
    nutri_score = res.get('product').get('nutrition_grades')

    nutri_score = nutri_score.upper()
    return res.get('product').get('nutrient_levels'), "Nutri-Score:" + " " + nutri_score





