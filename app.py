import streamlit as st
from functions import img_transform
import joblib
import base64
from PIL import Image
import io
import streamlit.components.v1 as components



camera_html = """
<style>
    #image_data { display: none; }
    /* Aquí puedes añadir estilos adicionales si es necesario */
</style>

<video id="video" width="640" height="480" autoplay></video>
<button id="capture">Capturar Foto</button>
<canvas id="canvas" width="640" height="480" style="display:none;"></canvas>

<script>
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    const captureButton = document.getElementById('capture');
    navigator.mediaDevices.getUserMedia({ video: {
            width: 800, height: 600
            } })

    // Solicitar acceso a la cámara
    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: {
            width: 800, height: 600
            } })
        .then(function(stream) {
            video.srcObject = stream;
        })
        .catch(function(error) {
            console.log("Error al acceder a la cámara:", error);
        });
    }

    document.addEventListener('DOMContentLoaded', (event) => {

        // Capturar la foto
        captureButton.addEventListener('click', function() {
            // Dibujar la imagen actual del video en el canvas
            context.drawImage(video, 0, 0, canvas.width, canvas.height);

            // Convertir la imagen a Base64 (si es necesario para tu aplicación)
            var imageData = canvas.toDataURL('image/png');
            
            // Suponiendo que tienes un elemento <img id="photo">
            document.getElementById('photo').src = imageData;
            console.log(imageData.split(',')[1])

            // Actualizar el campo de entrada oculto con la imagen en base64
            const imageData64 = document.querySelector('input[aria-label="Imagen en base64"]');
            console.log(imageData64)
            imageData64.value = imageData.split(',')[1];  // Remover la parte del prefijo Data URL

            
            // Desencadenar un evento de entrada para que Streamlit detecte el cambio
            const inputEvent = new Event('input', { bubbles: true });
            imageData64.dispatchEvent(inputEvent);
        });
    });
</script>

<!-- Elemento para mostrar la foto capturada -->
<img id="photo" width="640" height="480" />

</div>
"""

# Insertar el código HTML/JavaScript en la aplicación Streamlit
# st.markdown(camera_html, unsafe_allow_html=True)

best_model = joblib.load('./models/SVM_with_rotation.joblib')

# Titulo de la aplicación
st.title('Predicción de Manos')

# Cargando una imagen
uploaded_file = st.file_uploader("Cargar imagen", type=["png", "jpg", "jpeg"])

# components.html(camera_html, height=1000)
# st.markdown(camera_html, unsafe_allow_html=True)

if uploaded_file is not None:
    # Aquí procesarías la imagen y harías la predicción
    # Muestra la imagen
    st.image(uploaded_file, caption='Imagen Cargada', use_column_width=True)
    
    x = img_transform(uploaded_file)
    
    # Realizar la predicción
    prediction = best_model.predict([x])  # Asegúrate de que 'x' es un array bidimensional
    st.write(f"Predicción: {prediction[0]}")  # Mostrar la primera predicción


# Crea un botón en Streamlit que será presionado virtualmente por JavaScript
if st.button('Capturar imagen', key='capture'):
    # Esto se activará cuando se haga clic en el botón de captura en el frontend
    pass

# Utiliza un text_input de Streamlit como el receptor de la imagen en base64
# Lo ocultamos con CSS para que el usuario no lo vea
image_data = st.text_input("Imagen en base64", "", key="image_data")

# Revisa si hay datos en la imagen
if image_data != "":
    print(image_data)
    # Decodificar la imagen
    decoded_image = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(decoded_image))
    # Procesar la imagen con tu modelo o mostrarla
    st.image(image, caption='Imagen Capturada', use_column_width=True)
components.html(camera_html, height=1000)
