# DeepDetect: A Multi-Modal Framework for Comprehensive Deepfake Detection

**DeepDetect** is a comprehensive deepfake detection framework that leverages multiple modalities—audio, video, and image—to identify manipulated media. This project combines state-of-the-art models for detecting deepfakes across different formats, using machine learning and deep learning techniques.

### Key Features:
- **Audio Detection**: Utilizes MFCC (Mel Frequency Cepstral Coefficients) features combined with Support Vector Machines (SVM) for detecting deepfakes in audio.
- **Video Detection**: Applies Convolutional Neural Networks (CNN) and Recurrent Neural Networks (RNN) models for detecting deepfakes in video.
- **Image Detection**: Uses CNN models to classify deepfakes in images.
- **User Interfaces**:
  - **Audio Interface**: Flask with HTML/CSS
  - **Image Interface**: Streamlit
  - **Video Interface**: React and Flask

### Technologies Used:
- **Python**
- **Machine Learning**: SVM, CNN, RNN
- **Deep Learning**: PyTorch, Torchvision
- **Web Development**: Flask, Streamlit, React
- **Libraries**: OpenCV, pyttsx3, gTTS, librosa

### Getting Started:
To get started, clone the repository and set up the environment as follows:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/DeepDetect.git
   cd DeepDetect
   
2. Install required libraries:
Make sure you have Python 3.6+ installed and use pip to install the dependencies:
   ```bash
    pip install -r requirements.txt

3. Download the pre-trained models:
The models used for image and video detection are available in the following links:

### NOTE
Download the `.pth` file for **Image detection** and the `.pt` file for **Video detection** from [this link](your-drive-link).


