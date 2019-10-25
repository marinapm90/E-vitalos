from scrapping_web import * 
from scanning_ingredients import *
from scanning_barcode import *

def main():
    additives = get_table_additives()
    texto = capture_food()
    print("------------------------------------------------")
    print(texto)
    print("------------------------------------------------")
    resultado_1, resultado_2 = find_text(texto)
    valores = get_homogenic_data(resultado_1, resultado_2)
    allergies = get_allergies_dataframe(additives, valores)
    print(allergies)
    print("------------------------------------------------")
    barcodeData = capture_barcode()
    nutri = nutri_score(barcodeData)
    print(nutri)

if __name__=="__main__":
    main()






