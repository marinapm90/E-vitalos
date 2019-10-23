import scrapping_web
import scanning_ingredients
import scanning_barcode


def get_table():
    additives = scrapping_web.get_table_additives()
    return additives


def photo_ingredients():
    text = scanning_ingredients.capture_food()
    return text


def finding_text(text):
    result, result_2 = scanning_ingredients.find_text(text)
    return result, result_2


def getting_homogenic_data(result, result_2):
    values = scanning_ingredients.get_homogenic_data(result, result_2)
    return values


def get_dataframe(values):
    allergies = scanning_ingredients.get_allergies_dataframe(values)
    return allergies

def read_barcode():
    barcodeData = scanning_barcode.capture_barcode()
    return barcodeData


def get_nutri_score(barcodeData):
    nutri = scanning_barcode.nutri_score(barcodeData)
    return nutri

def main():
    additives = get_table()
    text = photo_ingredients()
    result, result_2 = finding_text(text)
    values = getting_homogenic_data(result, result_2)
    allergies = get_dataframe(values)
    barcodeData = read_barcode()
    nutri = get_nutri_score(barcodeData)


if __name__=="__main__":
    main()






