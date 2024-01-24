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
    features_hog = hog(image_np, pixels_per_cell=(8, 8))

    return features_hog