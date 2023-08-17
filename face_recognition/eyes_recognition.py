import argparse
from pathlib import Path
from typing import List

import cv2
import dlib

DEFAULT_BASE_DIR: str = 'resources'


# Load the pre-trained face and facial detection models
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


def detect_and_draw(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = detector(gray_image)

    # Loop through detected faces and detect facial landmarks
    for face in faces:
        landmarks = predictor(gray_image, face)

        # Draw a rectangle around the face
        cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 0), 2)

        # Draw circles on the eyes
        for n in range(36, 48):  # Range corresponding to eye landmarks
            x, y = landmarks.part(n).x, landmarks.part(n).y
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

    # Display the result
    cv2.imshow('Face and Eye Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main(argv=None):
    parser = argparse.ArgumentParser("Test eyes detection")
    parser.add_argument('-i', '--image', type=str, help='Path to an image')
    parser.add_argument('-d', '--dir', type=str, help='Directory to scan images in')
    args = parser.parse_args(argv)

    directory_path: Path = Path(args.dir or DEFAULT_BASE_DIR)
    if directory_path.exists():
        # gets a list of all the files in the directory that ends with "_leftImg8bit.png".
        file_list: List[Path] = list(directory_path.rglob('*.png'))

        for image in file_list:
            # Convert the Path object to a string using as_posix() method
            image_path: str = image.as_posix()
            detect_and_draw(image_path)


if __name__ == "__main__":
    main()
