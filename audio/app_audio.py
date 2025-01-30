from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Path for uploading audio files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'wav'}

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    result = None

    if request.method == 'POST':
        if 'audio_file' not in request.files:
            message = "No file part"
        else:
            audio_file = request.files['audio_file']
            if audio_file.filename == '':
                message = "No selected file"
            elif audio_file and allowed_file(audio_file.filename):
                # Save the file
                filename = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
                audio_file.save(filename)
                
                # Here you can add your deepfake detection logic.
                # For now, let's assume it detects a deepfake (You can replace this with your actual logic).
                result = "Deepfake"  # Replace with your detection model output.
                message = "Success"
            else:
                message = "Invalid file type. Only .wav files are allowed."
    
    return render_template('test.html', message=message, result=result)

if __name__ == '__main__':
    app.run(debug=True)
