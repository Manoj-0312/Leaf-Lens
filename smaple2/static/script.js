// static/script.js
document.addEventListener('DOMContentLoaded', function() {
    var imageInput = document.getElementById('imageInput');
    var imagePreview = document.getElementById('imagePreview');

    imageInput.addEventListener('change', function() {
        var file = this.files[0];
        if (file) {
            var reader = new FileReader();
            reader.onload = function(event) {
                var img = document.createElement('img');
                img.src = event.target.result;
                imagePreview.innerHTML = '';
                imagePreview.appendChild(img);
            }
            reader.readAsDataURL(file);
        } else {
            imagePreview.innerHTML = '';
        }
    });
});
