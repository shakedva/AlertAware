import time
import picamera
import keyboard


class ContinuousPhotoCapture:
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1920, 1080)
        self.running = False

    def capture_photos(self, photos_per_second):
        self.running = True

        # Display instructions for stopping the loop
        print("Press any key to stop capturing.")

        try:
            while self.running:
                start_time = time.time()

                for i in range(3):
                    filename = time.strftime("photo_%Y%m%d%H%M%S.jpg")
                    self.camera.capture(filename)
                    print(f"Captured {filename}")

                elapsed_time = time.time() - start_time
                if elapsed_time < 1:
                    time.sleep(1 - elapsed_time / photos_per_second)

                if keyboard.is_pressed():
                    print("Capture stopped by user.")
                    break

        finally:
            self.camera.close()


if __name__ == "__main__":
    capture_instance = ContinuousPhotoCapture()
    capture_instance.capture_photos(photos_per_second=3)
