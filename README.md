# Real-Time Object Tracking with openCV + VLM clips

## Project description
This project implements a **real-time object tracking system** using a webcam. The user selects an object in the first frame, and the system tracks it continuously in real time.

In addition to tracking, this project includes an **extra enhancement using a Vision-Language Model (CLIP)** to classify the tracked object. This helps improve the system by giving semantic understanding of what is being tracked.

---

## Features
- Select any object using a bounding box
- Real-time tracking using OpenCV (CSRT Tracker)
- Object classification using CLIP (VLM)
- Live FPS display
- Simple and interactive interface

---

## Technologies Used
- Python
- OpenCV
- PyTorch
- CLIP (Vision-Language Model)
- PIL (Python Imaging Library)

---

## Project Structure
```
project/
   detect.py
   image-1.png
   README.md


```

---

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/your-username/object-tracker.git
cd object-tracker
```

### 2. Install Dependencies
```bash
pip install opencv-python torch torchvision pillow git+https://github.com/openai/CLIP.git
```

---

## How to Run
```bash
python main.py
```

or just press the run button on the top left

![alt text](image-1.png)
---

## How to Use

1. Run the code  
2. Put the object you want to track in camra view
3. Press Enter to confirm the frame  
4. Draw a bounding box around the object  
5. Press Enter again  

code will then
- Start real time tracking of object  
- Display the object labels 
- Show tracking status and FPS  

### Controls
- Press **G** to Exit program (ps i made it g isntead of q because eyego)

---



### CLIP  (Extra reqirment added to boost the code)
i added an extra feature which is using a **Vision-Language Model (CLIP)**:



The tracked object is processed and encoded  from the img then compared against text labels that where given after that the most similar label is selected  

This elevates the code by adding semantic understanding not just tracking an object.

---



## Output
- Live webcam feed  
- Bounding box tracking the object  
- Predicted object label (e.g., "phone")  
- FPS counter  

---

## Assignment Requirements Covered
This project satisfies the following:
- Select an object using a bounding box  
- Track the selected object in real time  
- Display tracking results in a live video feed  

---

## Author
Meran Alhudaithy