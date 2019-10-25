from scanning_barcode import *

def main():
    barcodeData = capture_barcode()
    nutri = nutri_score(barcodeData)
    print(nutri)

if __name__=="__main__":
    main()
