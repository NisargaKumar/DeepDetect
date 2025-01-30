from flask import Flask, render_template
import subprocess
import time
import webbrowser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Main page with buttons

@app.route('/audio')
def audio():
    # Run the Audio Flask app in the background
    process = subprocess.Popen(["python", "audio/app_audio.py"])  # Adjust path if necessary
    time.sleep(5)  # Give it some time to start
    webbrowser.open("http://127.0.0.1:5000", new=2)  # Open in the default browser
    return render_template('message.html', message="Audio Detection is running on 127.0.0.1:5000. It should open automatically in your browser.")

@app.route('/video')
def video():
    # Run the Video Flask app in the background
    process = subprocess.Popen(["python", "video/server.py"])  # Adjust path if necessary
    time.sleep(5)  # Give it some time to start
    webbrowser.open("http://127.0.0.1:3000", new=2)  # Open in the default browser
    return render_template('message.html', message="Video Detection is running on 127.0.0.1:3000. It should open automatically in your browser.")

@app.route('/image')
def image():
    # Run the Streamlit Image Detection app in the background
    process = subprocess.Popen(["streamlit", "run", "image/ui.py"])  # Adjust path if necessary
    time.sleep(5)  # Give it some time to start
    webbrowser.open("http://localhost:8501", new=2)  # Open in the default browser
    return render_template('message.html', message="Image Detection is running on localhost:8501. It should open automatically in your browser.")

if __name__ == '__main__':
    app.run(port=8000)  # Main Flask app running on port 8000
