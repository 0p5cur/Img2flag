# Script OCR - Made by opscur
import cv2
import pytesseract
from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='Effectuer OCR sur une image.')
parser.add_argument('-f', '--file', type=str, help='Chemin de l\'image à traiter')

args = parser.parse_args()

if args.file is None:
    print("Veuillez spécifier le chemin de l'image avec l'argument -f image_path.")
else:
    image_path = args.file

    image = cv2.imread(image_path)

    if image is None:
        print("L'image n'a pas pu être chargée correctement.")
    else:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        ascii_characters = pytesseract.image_to_string(Image.fromarray(gray_image))

        ascii_characters = "".join(filter(lambda x: x.isascii(), ascii_characters))

        ascii_characters = ascii_characters.replace('\n', ' ')

        ascii_characters = ''.join(ascii_characters.split())

        print("Caractères ASCII extraits :")
        print(ascii_characters)
