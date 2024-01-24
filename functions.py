from PIL import Image
import numpy as np
from skimage.feature import hog

def img_transform(uploaded_file):
    # Cargar la imagen
    image = Image.open(uploaded_file).convert('L')  # Convertir a escala de grises

    # Redimensionar la imagen a 150x150
    image = image.resize((150, 150))

    # Convertir la imagen a un array de NumPy
    image_np = np.array(image)

    # Extraer características HOG
    features_hog, img_hog = hog(image_np, pixels_per_cell=(8, 8), visualize = True)

    # Normalizar 'img_hog' para que esté en el rango [0, 255] si es necesario
    if img_hog.min() < 0 or img_hog.max() > 1:
        img_hog = (img_hog - img_hog.min()) / (img_hog.max() - img_hog.min())  # Normalizar a [0, 1]
        img_hog = (img_hog * 255).astype(np.uint8)  # Escalar a [0, 255] y convertir a enteros

    
    return features_hog, image, img_hog