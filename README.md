# 📱 Gujarati Text Extractor (OCR + NLP) — Android App
This is an Android mobile application that lets you capture or upload handwritten Gujarati text images, extracts the text using advanced OCR technology, and performs basic Natural Language Processing (NLP) operations on the recognized text.

## 📌 App Features
✅ Capture or upload handwritten Gujarati text images

✅ Extract readable Gujarati text using OCR

✅ Process and clean up the extracted text

✅ Display results clearly within the app

✅ Lightweight and easy-to-use offline app interface

## 📥 How to Use
### 📥 Install the APK file on your Android phone**

*Download the provided **gujarati_OCR.apk** file*

If prompted, allow installation from unknown sources

**📡 Important: Ensure your mobile and PC are connected to the same Wi-Fi or network**

The app sends the image to a Python server running on your PC for OCR processing

The server processes the image and sends back the extracted text

### 🖥️ On your PC:

Run the provided Python server script

*main.exe*

The server will listen for incoming image uploads via the app

📸 Open the app, and either:

Capture a new image of handwritten Gujarati text

Select an existing image from your gallery

📝 The app will process the image, send it to the PC, extract the text, and display it on your screen

## 🎯 Requirements
Android 7.0 (Nougat) or later

Camera permission (for capturing images)

Storage permission (for picking images from gallery)

PC with Python server running and connected to the same network

## 📡 Network Requirement
⚠️ Important:

The Android device and PC must be connected to the same Wi-Fi or local network

The Python server must be running on the PC before using the app

You will need to set the correct IP address of the PC in the app (matching your local network IP)

## Testing
You can just test this project from the terminal as well.

just redirect to the directory **Test**

run `python test_api.py`


## 📚 Disclaimer
This app uses offline OCR and NLP services on your local network

No personal data is collected or shared outside your network

## 📖 About the Project
This app was developed as part of a project to demonstrate Gujarati handwritten OCR technology combined with basic text processing for academic and demonstration purposes.

## 🖊️ Author
Pratham Bhanushali
NFSU | M.Tech Artificial Intelligence and Data Science (Specialization in Cyber Security) | 2025
