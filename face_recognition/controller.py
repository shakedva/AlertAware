import ContinuousPhotoCapture
import DataProcessor
import EyeClassifier
import time
from pathlib import Path

DEFAULT_BASE_DIR: str = 'resources'


class Controller:
    def __init__(self):
        self.camera = ContinuousPhotoCapture()
        self.data_processor = DataProcessor()
        self.detector = EyeClassifier()

    def run(self):
        while True:
            # Capture photos using the camera
            self.camera.capture_photos()

            # Wait for a second before processing the images
            time.sleep(1)

            # Process the captured images using the data processor
            directory_path: Path = Path(DEFAULT_BASE_DIR)
            self.data_processor.process_data(directory_path)
            self.detector.run()

            # Wait for a second before the next iteration
            time.sleep(1)
