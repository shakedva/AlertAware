from camera import ContinuousPhotoCapture
from eyes_recognition import DataProcessor
from run_model_on_crops import EyeClassifier
import time
from pathlib import Path
import keyboard

DEFAULT_BASE_DIR: str = 'resources'


class Controller:
    def __init__(self):
        self.camera = ContinuousPhotoCapture()
        self.data_processor = DataProcessor()
        self.detector = EyeClassifier()

    def run(self):
        count_sec = 0
        running = True  # Flag to control the loop
        while running:
            count_sec += 1
            self.camera.capture_photos(photos_to_capture=3)
            # Process the captured images using the data processor
            directory_path: Path = Path(DEFAULT_BASE_DIR)
            self.data_processor.process_data(directory_path)
            self.detector.run()

            # Wait for a second before the next iteration
            time.sleep(2)


controller = Controller()
controller.run()
