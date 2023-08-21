import time
import picamera
import keyboard

# Initialize the camera
camera = picamera.PiCamera()

# Set the resolution (optional)
camera.resolution = (1920, 1080)

# Function to stop the loop when the Esc key is pressed
def stop_capture(e):
    raise KeyboardInterrupt()

# Bind the Esc key to the function
keyboard.on_press_key("esc", stop_capture)

try:
    while True:
        # Capture a photo
        filename = time.strftime("photo_%Y%m%d%H%M%S.jpg")
        camera.capture(filename)
        print(f"Captured {filename}")

        # Wait for a brief moment before taking the next photo
        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped by user.")

finally:
    # Release the camera resources
    camera.close()
