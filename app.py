import streamlit as st
from functions import img_transform
import joblib
import base64
from PIL import Image
import io
import streamlit.components.v1 as components

intro = """
<div>
    <h2>Resumen del Proceso de Preprocesamiento y Entrenamiento del Modelo</h2>
    <p>Este proceso implica desarrollar un modelo predictivo basado en imágenes, utilizando técnicas de procesamiento de imágenes y aprendizaje automático.</p>
    <h3>Preprocesamiento de Imágenes</h3>
    <p>Un total de 400 imágenes se cargan desde archivos JSON, se decodifican a formatos utilizables, se convierten a escala de grises y se redimensionan. Aplicamos el método HOG para extraer características y duplicamos el conjunto de datos utilizando imágenes rotadas.</p>
    <h3>Entrenamiento del Modelo</h3>
    <p>Seleccionamos un clasificador SVC con kernel polinómico y entrenamos el modelo con los datos procesados. Esto permite al modelo hacer predicciones sobre datos no vistos y tener un porcentaje de acierto razonable a pesar de la escasa cantidad de imagenes de entrenamiento.</p>
    <h3>Evaluación del Modelo</h3>
    <p>El modelo entrenado se evalúa con un conjunto de imágenes de prueba, en concreto se ha llegado a conseguir un acierto de 0.72.</p>
    <h3>Prueba el modelo tu mismo</h3>
    <p>Sube una imagen en buenas condiciones lumínicas de tu mano y observa la magia.</p>
</div>
<style>
    .css-1lcbmhc {
        background: linear-gradient(to right, #333333, #4d4d4d) !important;
    }
    .stMarkdown {
        background-color: white;  /* Un gris muy claro como fondo */
        border-radius: 10px;        /* Bordes redondeados */
        padding: 20px;              /* Espaciado interno */
        margin-bottom: 10px;        /* Espaciado entre componentes */
    }
    body {
        font-family: 'Arial', sans-serif;
    }
    img {
        border: 1px solid #ddd;    /* Borde gris claro */
        border-radius: 4px;        /* Bordes ligeramente redondeados */
        padding: 5px;              /* Espaciado alrededor de la imagen */
        box-shadow: 2px 2px 4px #ccc;  /* Sutil sombra */
    }
</style>
"""
# Insertar el código HTML/JavaScript en la aplicación Streamlit

best_model = joblib.load('./models/SVM_with_rotation.joblib')

# Titulo de la aplicación
st.title('Predicción de Manos')
st.markdown(intro, unsafe_allow_html=True)

# Cargando una imagen
uploaded_file = st.file_uploader("Cargar imagen", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Aquí procesarías la imagen y harías la predicción
    # Muestra la imagen    
    x, image, image_hog = img_transform(uploaded_file)
    st.text("Imagen cargada.")
    
    # Crear dos columnas
    col1, col2 = st.columns(2)

    # Mostrar la imagen original en la primera columna
    with col1:
        st.image(image, caption='Imagen Original', use_column_width=True)
        
    # Ahora puedes mostrar la imagen HOG normalizada con Streamlit
    with col2:
        st.image(image_hog, caption='Imagen con HOG', use_column_width=True)   
    # Realizar la predicción
    prediction = best_model.predict([x])  # Asegúrate de que 'x' es un array bidimensional
    st.write(f"Predicción: {prediction[0]}")  # Mostrar la primera predicción