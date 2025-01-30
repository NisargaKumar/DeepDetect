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
Download the `.pth` file for **Image detection** and the `.pt` file for **Video detection** from [this link](https://drive.google.com/drive/folders/1LBowbYcON1L3uyqagmD1fQAjStxd8T27?usp=drive_link).

![Screenshot (11)](https://github.com/user-attachments/assets/16bba869-3f88-4bc6-90f8-9dd65e13d469)
![Screenshot (12)](https://github.com/user-attachments/assets/299dd0d7-5fbe-4687-8a9f-96060e4bfe01)
![Screenshot (14)](https://github.com/user-attachments/assets/51969967-a22f-46a2-9bdb-540e533c5a86)
