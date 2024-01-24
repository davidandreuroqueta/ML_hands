console.log("hola")
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const captureButton = document.getElementById('capture');


// Solicitar acceso a la cámara
if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
    .then(function(stream) {
        video.srcObject = stream;
    })
    .catch(function(error) {
        console.log("Error al acceder a la cámara:", error);
    });
}

// Capturar la foto
captureButton.addEventListener('click', function() {
    // Dibujar la imagen actual del video en el canvas
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    // Convertir la imagen a Base64 (si es necesario para tu aplicación)
    var imageData = canvas.toDataURL('image/png');

    // Aquí puedes enviar 'imageData' a tu servidor o procesarlo
    // Por ejemplo, mostrándolo en consola o en un elemento <img>
    console.log(imageData);
    // Suponiendo que tienes un elemento <img id="photo">
    document.getElementById('photo').src = imageData;
});