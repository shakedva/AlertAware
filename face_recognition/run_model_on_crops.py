from keras.models import load_model
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

OPEN_LABEL: str = 'Open_Eyes'
CLOSED_LABEL: str = 'Closed_Eyes'
crop_images = []
DEFAULT_BASE_DIR: str = 'resources'
CROPS_PATH = DEFAULT_BASE_DIR + "/crops"
best_model = load_model('bestModel.h5')


for filename in os.listdir(CROPS_PATH):
    if filename.endswith(".jpg"):
        image_path = os.path.join(CROPS_PATH, filename)
        img = Image.open(image_path).resize((64, 64)).convert('L')  # Convert to grayscale
        img = np.array(img)
        img = (img - np.min(img)) / (np.max(img) - np.min(img))
        img = img / 255.0
        img = np.expand_dims(img, -1)
        crop_images.append(img)

crop_images = np.array(crop_images)

open_count = 0
close_count = 0
for img in crop_images:
    result = best_model.predict(np.expand_dims(img, 0))
    plt.imshow(img.squeeze(), cmap='gray')
    plt.axis('off')
    plt.show()

    if result > 0.5:
        open_count += 1
        # print(OPEN_LABEL)
        # plt.text(5, 5, OPEN_LABEL, color='green', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))
    else:
        close_count += 1
        # print(CLOSED_LABEL)
        # plt.text(5, 5, CLOSED_LABEL, color='red', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

print(f"{OPEN_LABEL}: {open_count}")
print(f"{CLOSED_LABEL}: {close_count}")