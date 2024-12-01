
# AI-Powered Real-Time Background Generator

## Project Overview
This project is a Python-based application that uses advanced computer vision and AI techniques to enable real-time video background removal and replacement. It integrates prompt-based dynamic image generation, allowing users to customize their backgrounds with ease. The project is designed for applications such as video conferencing, live streaming, and virtual events.

---

## Features
- **Real-Time Background Removal**: Uses `cvzone` and `mediapipe` for efficient background segmentation.
- **Prompt-Based Image Generation**: Dynamically generate backgrounds using the Pollinations.AI API.
- **Custom Background Upload**: Users can upload their own images as backgrounds.
- **Dynamic Background Effects**: Easily switch between multiple backgrounds with keyboard controls.
- **Performance Optimization**: Optimized for real-time use with threading and efficient libraries.

---

## Technologies Used
- **Languages**: Python 3.10
- **Libraries**: 
  - `OpenCV`: For image processing.
  - `cvzone`: Simplifies background removal.
  - `mediapipe`: Efficient segmentation and face detection.
  - `requests`: To integrate the Pollinations.AI API.
- **APIs**: Pollinations.AI for text-to-image generation.

---

## Setup Instructions

### 1. Prerequisites
- Python 3.10 or higher installed on your machine.
- Basic knowledge of Python and virtual environments.

### 2. Clone the Repository
```bash
git clone https://github.com/abhaysingla05/AI-Powered-Real-Time-Background-Generator.git
cd AI-Powered-Real-Time-Background-Generator
3. Create and Activate Virtual Environment
Create a virtual environment:

bash
Copy code
python -m venv env
Activate the virtual environment:

Windows:
bash
Copy code
env\Scripts\activate
macOS/Linux:
bash
Copy code
source env/bin/activate
4. Install Dependencies
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
5. Run the Application
Start the background generator:

bash
Copy code
python BackgroundRemover.py
Usage
Keyboard Controls
p: Generate a new background using a custom text prompt.
a: Navigate to the previous background.
d: Navigate to the next background.
q: Quit the application.
Text Prompt Example
When prompted to input a background generation prompt, you can use phrases like:

"Sunset over the mountains"
"Futuristic cityscape at night"
"Underwater coral reef"
Folder Structure
bash
Copy code
AI-Powered-Real-Time-Background-Generator/
│
├── BackgroundRemoval.py      # Main application script
├── requirements.txt          # Required dependencies
├── README.md                 # Project documentation
├── BackgroundImages/         # Folder containing static background images
├── GeneratedBackground.jpg   # Dynamically generated background
└── env/                      # Local virtual environment (excluded from Git)
Future Enhancements
Gesture Control: Implement hand gesture recognition for switching backgrounds.
Voice Commands: Add support for voice-controlled background management.
AR/VR Integration: Extend compatibility for AR/VR environments.
Virtual Background Videos: Enable users to set videos as dynamic backgrounds.
Contributing
Contributions are welcome! If you'd like to contribute to this project:

Fork the repository.
Create a feature branch (git checkout -b feature-name).
Commit your changes (git commit -m "Add feature-name").
Push to the branch (git push origin feature-name).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or support, feel free to reach out:

Name: Abhay Sharma
Email: abhisharma588600@gmail.com
GitHub: abhaysingla05