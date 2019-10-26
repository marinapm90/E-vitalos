# E-VITALOS

[TOC]

Este proyecto consiste en el reconocimiento de texto en imágenes para extraer la información de los aditivos que llevan los alimentos que consumimos y tratar de verificar si se trata de alimentos que pueden causar alergias a una persona que padece esofaguitis eosinofílica.

Los tipos de aditivos que existen están sacados de realizar un **scrapping** de la web [web e-aditivos](https://e-aditivos.com/).

Además a traves del reconocimiento de códigos de barras y con la **conexión de la API** [Food Facts](https://world.openfoodfacts.org/data) extraeremos información nutricional del alimento.



### LIBRERÍAS USADAS

- BeautifulSoup
- Pandas
- Requests
- Numpy
- Opencv
- Pillow
- Pytesseract
- Re
- Pyzbar
- Argparse
- Pprint

### CÁMARA UTILIZADA

Para realizar las fotos utilizaremos la cámara del móvil conectándola a la misma IP que el ordenador, para eso utilizaremos la [APP IP WEBCAM](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=es)

### FUNCIONAMIENTO

Existen 4 archivos diferentes:

- E-vitalos.py
- scrapping_web.py
- scanning_ingredients.py
- scanning_barcode.py

El archivo principal es **E-vitalos.py** el resto contienen las funciones con las que trabaja éste último.
Los demás sirven para recoger las funciones para scrappear la web *(scrapping_web.py)* hacer la foto y devolver un dataframe con los aditivos *(scanning_ingredients.py)* y para recoger la información del código de barras y devolver la información nutricional *(scanning_barcode.py)*

Para realizar una foto de los ingredientes del alimento utilizaremos el comando:

``` python3 E-vitalos.py -i``` o ``` python3 E-vitalos.py --ingredients```

Para cerrar la cámara y hacer la captura haremos click en la letra "Q" 

A continuación nos aparecerán los aditivos que contiene nuestro producto, con la información del origen, categoría, nombre y si es alérgeno o no.

![foto_aditivos](https://raw.githubusercontent.com/marinapm90/E-vitalos/master/outputs/Screenshot%20from%202019-10-26%2002-35-15.png)



Para realizar una foto del código de barras utilizaremos el comando:

```python3 E-vitalos.py -b```  o ```python3 E-vitalos.py --barcode```

Para cerrar la cámara haremos click en la letra "Q"

A continuación nos aparecerá la información nutricional del producto.

![foto_nutricional](https://raw.githubusercontent.com/marinapm90/E-vitalos/master/outputs/Screenshot%20from%202019-10-26%2002-42-23.png)

También podemos utilizar ```python3 E-vitalos.py -h``` o ```python3 E-vitalos --help``` para obtener ayuda.

### PRÓXIMOS PASOS

En versiones futuras el proyecto será **escalable a otros problemas alimenticios** (alergias o intolerancias).

Otra idea para implementar en un futuro es la de **recomendar otros productos** que puedan ser menos perjudiciales.



