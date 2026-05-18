
# Solar Panel Detection Using YOLOv8

AI-powered solar panel detection system built with YOLOv8 and Computer Vision for identifying solar infrastructure from aerial and rooftop imagery.

---

# Overview

This project focuses on building a real-time object detection model capable of identifying solar panels from images captured by drones, satellites, and rooftop surveillance systems.

The model leverages YOLOv8 to automatically localize solar panels using bounding boxes and confidence scores, enabling scalable infrastructure analysis and renewable energy monitoring.

This project explores practical applications of Deep Learning and Computer Vision within the renewable energy sector.


---

# Real-World Applications

- 🛰️ Satellite-based solar panel mapping
-  Drone inspection of solar farms
-  Renewable energy infrastructure monitoring
-  Rooftop solar adoption analysis
-  Automated infrastructure inspection
-  Smart energy analytics systems.
  
  ---

# Detection Pipeline

```text
Data Collection
     ↓
Image Annotation & Preprocessing
     ↓
YOLOv8 Model Training
     ↓
Feature Extraction
     ↓
Object Localization
     ↓
Bounding Box Prediction
     ↓
Solar Panel Detection
     ↓
Model Evaluation & Validation
     ↓
Prediction Visualization
     ↓
Multi-Image & Video Inference
     ↓
Streamlit Deployment
     ↓
Real-Time Webcam Detection
     ↓
Drone Footage Analysis

```
---

# Model Architecture
The detection system is built using YOLOv8 Nano from Ultralytics.
The model leverages transfer learning from pretrained COCO weights and fine-tunes the network on annotated solar panel imagery.
YOLOv8 enables fast and efficient real-time object detection by combining feature extraction, object localization, and bounding box regression into a single unified architecture.

----
## Core Components

- YOLOv8 Nano
- Convolutional Neural Networks (CNNs)
- Transfer Learning
- Bounding Box Regression
- Real-Time Object Detection

-----

## Technologies used

| --- | --- |

- Python → Core programming language 

- YOLOv8 → Object detection framework 

- Ultralytics → YOLO implementation 

- OpenCV  → Image processing 

- Roboflow → Dataset management 

- Google Colab → Model training 

- Streamlit →  Deployment 

