from docx import Document
from fpdf import FPDF

# Create a new PDF
class PDF(FPDF):
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, ln=True, align='L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# Create PDF object
pdf = PDF()
pdf.add_page()

# Chapter 4 Content
pdf.chapter_title('Chapter 4: Technical Requirements')
chapter4_text = """
4.1 Introduction
The AI-Driven Crop Disease Prediction and Management System is designed to assist farmers by providing early detection of crop diseases, enabling timely interventions, and promoting better yield management through actionable insights. By combining Machine Learning (ML), Deep Learning (DL), mobile development, and cloud technologies, the system ensures that farmers receive real-time, accurate, and personalized information directly on their mobile devices.
This chapter details the technical languages, frameworks, tools, and hardware/software requirements crucial for the system’s development, training, deployment, and maintenance.

4.2 Coding Languages Used
Frontend Development:
• React Native: Cross-platform mobile applications.
• JavaScript: For dynamic functionality.
• HTML5 & CSS3: Inspired JSX syntax and inline styling.

Backend Development:
• Python: For backend logic and AI inference.
• FastAPI: For fast and scalable APIs.

AI/ML Model Development:
• TensorFlow 2.x and Keras: CNN model construction.
• scikit-learn: Data preprocessing and evaluation.

Example Code:
from fastapi import FastAPI
import tensorflow as tf

app = FastAPI()
MODEL = tf.keras.models.load_model('Model_2.h5')

4.3 Tools and Software Required
• Android Studio, Expo Go, MongoDB Atlas, TensorFlow, OpenWeatherMap API, Heroku/AWS, Firebase Cloud Messaging (future).

4.4 Hardware Requirements
• Intel i5/i7, 8 GB RAM, 250 GB SSD, Smartphones.

4.5 Software Requirements
• Windows 10/11, Linux, macOS Monterey, Android/iOS devices, Visual Studio Code, Android Studio, MongoDB Compass.
"""
pdf.chapter_body(chapter4_text)

# Chapter 6 Content
pdf.chapter_title('Chapter 6: Technical Implementation')
chapter6_text = """
6.1 Technologies Used
Mobile App: React Native with Expo Framework
Backend Server: Python with FastAPI Framework
Database: MongoDB Atlas
Model Training: TensorFlow 2.x and Keras APIs
Cloud Hosting: Heroku/AWS EC2
APIs: OpenWeatherMap API, Google Maps API

6.2 Machine Learning Model Implementation
- Dataset loading using TensorFlow
- CNN model architecture with Conv2D, MaxPooling, Dense layers
- Early stopping during training
- Model saved in .h5 format

6.3 Backend API Implementation
- FastAPI server setup
- POST /predict endpoint for disease prediction

6.4 Complete Workflow
1. User registers crop.
2. System fetches weather data.
3. User uploads image.
4. Backend predicts disease.
5. Results displayed in app.

6.5 Frontend Implementation
- React Native application with Expo
- User flow from Splash ➔ Language ➔ Login ➔ Dashboard ➔ Crop Registration ➔ Disease Detection
- Image upload to backend
- Weather fetching with OpenWeatherMap API

6.6 Advantages
- High model accuracy (>92%)
- Instant prediction
- Cloud scalability
- Farmer-focused design

6.7 Future Enhancements
- Push notifications
- Dataset expansion
- Multilingual results
- Disease stage detection
"""
pdf.chapter_body(chapter6_text)

# Save the PDF
pdf_output_path = '/mnt/data/AI_Crop_Disease_Project_Report.pdf'
pdf.output(pdf_output_path)

pdf_output_path