import sys
import cv2
import numpy as np

#------------------------- Inicio de los métodos ----------------------------

# Aplicar Umbralización de Otsu a la imagen e invertirla al mismo tiempo
def image_thresholding(image):
  #ret = retVal, representa el valor de umbralización calculado por el método de Otsu
  ret, th = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
  return th


#Etiquetar la image 
def image_labeling(image):
  edge = cv2.Canny(image, 100, 200)
  return edge

#Localizar el contorno de la imagen 
def find_contour(image): 
  _, contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  return contours


#Crear archivo .mat 
def create_file(file_name, contours):

  file = open(f"./files/{file_name}.m", "w") 
  
  for row in range(len(contours)):
    file.write(f"Cont{row} = [")
    # Almacena las coordenadas de X
    for col in range(len(contours[row])):
      x = contours[row][col].item(0)
      if(col == (len(contours[row]) - 1)):
        file.write(f'{x}; ')
      else: 
        file.write(f'{x}, ')

    # Almacena las coordenadas de Y
    for _col in range(len(contours[row])):
      y = contours[row][_col].item(1)
      if(_col == (len(contours[row]) - 1) ):
        file.write(f'{y}];\n')
      else: 
        file.write(f'{y}, ')

  file.close() 
  print('file created!')



#------------------------- Final de los métodos ----------------------------


# validar los argumentos (MAIN)
if len(sys.argv) > 1:
  # Obtener la imagen por argumento y completar la ruta relativa
  image = f"./images/{sys.argv[1]}"

  try:
    # Cargar la imagen
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    #Aplicación de métodos para el procesamiento de las imagenes
    img_thresholding = image_thresholding(img)
    img_labeling = image_labeling(img_thresholding)
    contours = find_contour(img_labeling)

    # Archivo .mat
    file_name, extension = (sys.argv[1]).split('.')
    create_file(file_name, contours)
 
  except:
    print('-La imagen ingresada no existe-')

else:
  print('Introducir argumento <<imagen.ext>>')

