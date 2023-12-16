# AlertAware

Authors:
- Shaked Vaknin
- Moshe Namdar
- Raed Barhoum

## Dangers of Employee Fatigue

- Threat to workplace safety and productivity
- Reduces alertness
- Slows reaction times
- Accidents and injuries
- Poor decision-making
- Decreased concentration

## The Solution: Real-Time Fatigue Detection

- Raspberry Pi with a high-resolution camera

- The camera captures images of employees' faces as they go about their tasks.
- The algorithms analyze facial features, focusing on closed eyes and signs of tiredness.
- Upon detecting signs of fatigue, AlertAware triggers instant alerts and shuts down dangerous machines.

## Process

### 1. Neural Network Training
- Train a neural network using a dataset of closed and open eyes.

### 2. Controller Initialization

### 3. Image Capture and Processing
1. Capture images of the employee's face using the Raspberry Pi camera.
2. Eye Cropping: Crop the eyes from the captured images.

### 4. Decision-Making
- The cropped eye images are fed into the trained neural network for analysis.
- The neural network analyzes the cropped eye images, and based on its decision, the system determines if the eyes are open or closed.

### 5. Telegram Bot Integration
- If closed eyes are detected, a message is sent to a Telegram bot through a POST API request.