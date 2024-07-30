# Paddy Disease Classification Web Application

This project provides a web application for classifying paddy diseases using a trained machine learning model. The application allows users to upload an image of paddy, and it returns the predicted disease label and confidence score. The application is implemented using both Gradio and Flask frameworks.

## Project Structure

- `app.py`: The Flask application script for running the web server and handling image uploads and predictions.
- `templates/`
  - `index.html`: HTML template for the home page where users can upload images.
  - `results.html`: HTML template for displaying the prediction results.
- `model82.h5`: The trained machine learning model used for classification.
- `uploads/`: Directory to temporarily store uploaded images.

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/paddy-disease-classification.git
   cd paddy-disease-classification
