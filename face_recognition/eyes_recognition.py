import argparse
from pathlib import Path
from typing import List

import cv2
import dlib
from datetime import datetime

DEFAULT_BASE_DIR: str = 'resources'
LABELED_CSV_NAME: str = 'eyes_labeled.csv'
IMAGE_FORMAT: str = "*.png"
CROPS_PATH = DEFAULT_BASE_DIR + "/crops"
# Load the pre-trained face and facial detection models
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


def detect_and_crop_eyes(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = detector(gray_image)

    for face in faces:
        landmarks = predictor(gray_image, face)

        # Calculate bounding boxes for both eyes
        left_eye_top_left = (landmarks.part(36).x - 10, landmarks.part(37).y - 20)
        left_eye_bottom_right = (landmarks.part(39).x + 10, landmarks.part(41).y + 10)

        right_eye_top_left = (landmarks.part(42).x - 10, landmarks.part(43).y - 20)
        right_eye_bottom_right = (landmarks.part(45).x + 10, landmarks.part(47).y + 10)

        # Crop and resize left eye
        left_eye = image[left_eye_top_left[1]:left_eye_bottom_right[1], left_eye_top_left[0]:left_eye_bottom_right[0]]
        left_eye_resized = cv2.resize(left_eye, (64, 64))

        # Crop and resize right eye
        right_eye = image[right_eye_top_left[1]:right_eye_bottom_right[1], right_eye_top_left[0]:right_eye_bottom_right[0]]
        right_eye_resized = cv2.resize(right_eye, (64, 64))

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Save the cropped and resized eyes
        cv2.imwrite(CROPS_PATH + f"/left_eye_{timestamp}.jpg", left_eye_resized)
        cv2.imwrite(CROPS_PATH + f"/right_eye_{timestamp}.jpg", right_eye_resized)

        # Draw rectangles around the eyes
        cv2.rectangle(image, left_eye_top_left, left_eye_bottom_right, (255, 0, 0), 2)
        cv2.rectangle(image, right_eye_top_left, right_eye_bottom_right, (255, 0, 0), 2)

    # Display the result
    cv2.imshow('Cropped Eyes', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main(argv=None):
    parser = argparse.ArgumentParser("Test eyes detection")
    parser.add_argument('-i', '--image', type=str, help='Path to an image')
    parser.add_argument('-d', '--dir', type=str, help='Directory to scan images in')
    args = parser.parse_args(argv)

    directory_path: Path = Path(args.dir or DEFAULT_BASE_DIR)
    if directory_path.exists():
        file_list: List[Path] = list(directory_path.rglob(IMAGE_FORMAT))

        for image in file_list:
            # Convert the Path object to a string using as_posix() method
            image_path: str = image.as_posix()
            detect_and_crop_eyes(image_path)


if __name__ == "__main__":
    main()
