from flask import Flask, request, render_template
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model
import os

# Load your trained model (make sure to update the model path)
model = load_model('model82.h5')

app = Flask(__name__)

def predict_image(img_path):
    # Preprocess the image
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Rescale image

    # Make prediction
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)
    class_labels = ['bacterial_leaf_blight', 'bacterial_leaf_streak', 'bacterial_panicle_blight', 'blast', 'brown_spot', 'dead_heart', 'downy_mildew', 'hispa', 'normal', 'tungro']  # Update with your actual class labels

    # Get predicted label and confidence
    predicted_label = class_labels[predicted_class[0]]
    confidence = predictions[0][predicted_class[0]]

    # Return the predicted label and confidence
    return predicted_label, confidence

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file:
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            predicted_label, confidence = predict_image(file_path)
            return render_template('results.html', label=predicted_label, confidence=confidence)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
