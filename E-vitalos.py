from scrapping_web import * 
from scanning_ingredients import *
from scanning_barcode import *
import argparse
import pprint




def main_1():
    additives = get_table_additives()
    texto = capture_food()
    print("================================================================================================================================")
    print(texto)
    print("================================================================================================================================")
    resultado_1, resultado_2 = find_text(texto)
    valores = get_homogenic_data(resultado_1, resultado_2)
    allergies = get_allergies_dataframe(additives, valores)
    print(allergies)
    
def main_2():
    print("================================================================================================================================")
    barcodeData = capture_barcode()
    nutri = nutri_score(barcodeData)
    print("================================================================================================================================")
    pprint.pprint(nutri)
    print("================================================================================================================================")

parser = argparse.ArgumentParser()
parser.add_argument("-i","--ingredients",help="Take a picture of ingredients",action="store_true")
parser.add_argument("-b","--barcode",help="Take a picture of barcode",action="store_true")

args=parser.parse_args()


if __name__=="__main__":
    if args.ingredients:
        main_1()

    elif args.barcode:
        main_2()









