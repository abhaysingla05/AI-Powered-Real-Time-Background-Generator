import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
import time
import requests

# Custom FPS implementation
class FPS:
    def __init__(self):
        self.previous_time = time.time()

    def update(self, frame):
        current_time = time.time()
        fps = 1 / (current_time - self.previous_time)
        self.previous_time = current_time
        cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        return frame

# Function to fetch an image from Pollinations.AI based on a prompt
def fetch_image_from_pollinations(prompt, output_path="GeneratedBackground.jpg"):
    print(f"Fetching image for prompt: {prompt}")
    url = f"https://image.pollinations.ai/prompt/{prompt}"
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print("Image fetched and saved successfully.")
            return output_path
        else:
            print(f"Failed to fetch image. Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error while fetching image: {e}")
        return None

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set frame width
cap.set(4, 480)  # Set frame height

segmentor = SelfiSegmentation()
fpsReader = FPS()

# Load background images
background_folder = "BackgroundImages"
listImg = os.listdir(background_folder)
imgList = [cv2.imread(f'{background_folder}/{imgPath}') for imgPath in listImg if cv2.imread(f'{background_folder}/{imgPath}') is not None]

indexImg = 0

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read from camera")
        break

    imgOut = segmentor.removeBG(img, imgList[indexImg])
    if img is None or imgOut is None:
        print("Error: One of the images is None")
        break

    imgStack = cvzone.stackImages([img, imgOut], 2, 1)  # Stack images side-by-side
    imgStack = fpsReader.update(imgStack)

    cv2.imshow("image", imgStack)
    key = cv2.waitKey(1)

    if key == ord('a') and indexImg > 0:
        indexImg -= 1
    elif key == ord('d') and indexImg < len(imgList) - 1:
        indexImg += 1
    elif key == ord('p'):  # Generate a new background image based on a prompt
        prompt = input("Enter prompt for background generation: ")
        generated_path = fetch_image_from_pollinations(prompt)
        if generated_path:
            new_img = cv2.imread(generated_path)
            if new_img is not None:
                new_img = cv2.resize(new_img, (640, 480))  # Ensure it matches the frame size
                imgList.append(new_img)
                print("New background added.")
                indexImg = len(imgList) - 1  # Switch to the new background
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
