from flask import Flask, request, send_file, render_template
from PIL import Image
import numpy as np
import io

app = Flask(__name__)

def encrypt_image(image):
    pixels = np.array(image)
    encrypted_pixels = (pixels + 50) % 256  # Simple encryption by adding 50 to each pixel value
    return Image.fromarray(encrypted_pixels.astype('uint8'))

def decrypt_image(image):
    pixels = np.array(image)
    decrypted_pixels = (pixels - 50) % 256  # Simple decryption by subtracting 50 from each pixel value
    return Image.fromarray(decrypted_pixels.astype('uint8'))

@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    file = request.files['image']
    image = Image.open(file.stream)
    encrypted_image = encrypt_image(image)
    byte_arr = io.BytesIO()
    encrypted_image.save(byte_arr, format='PNG')
    byte_arr.seek(0)
    return send_file(byte_arr, mimetype='image/png')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    file = request.files['image']
    image = Image.open(file.stream)
    decrypted_image = decrypt_image(image)
    byte_arr = io.BytesIO()
    decrypted_image.save(byte_arr, format='PNG')
    byte_arr.seek(0)
    return send_file(byte_arr, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

'''from flask import Flask, request, send_file, render_template
from PIL import Image
import numpy as np
import io

app = Flask(__name__, template_folder='templates')

def encrypt_image(image):
    pixels = np.array(image)
    encrypted_pixels = (pixels + 50) % 256  # Simple encryption by adding 50 to each pixel value
    return Image.fromarray(encrypted_pixels.astype('uint8'))

def decrypt_image(image):
    pixels = np.array(image)
    decrypted_pixels = (pixels - 50) % 256  # Simple decryption by subtracting 50 from each pixel value
    return Image.fromarray(decrypted_pixels.astype('uint8'))

@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    file = request.files['image']
    image = Image.open(file.stream)
    encrypted_image = encrypt_image(image)
    byte_arr = io.BytesIO()
    encrypted_image.save(byte_arr, format='PNG')
    byte_arr.seek(0)
    return send_file(byte_arr, mimetype='image/png')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    file = request.files['image']
    image = Image.open(file.stream)
    decrypted_image = decrypt_image(image)
    byte_arr = io.BytesIO()
    decrypted_image.save(byte_arr, format='PNG')
    byte_arr.seek(0)
    return send_file(byte_arr, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)'''
