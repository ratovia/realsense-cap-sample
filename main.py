import cv2
import shutil
import threading

def capture_image_async(self):
    thread = threading.Thread(target=self.capture_image)
    thread.daemon = True
    thread.start()

def capture_image(self):
    print("\n\n *** Capture captureImage *** \n\n")
    for i in range(5):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            break

    if not cap.isOpened():
        print("カメラ情報が取得できませんでした。")
        self.captureResult.emit(False)
        return False
    ret, frame = cap.read()
    japan_timezone = pytz.timezone("Asia/Tokyo")
    current_time_japan = datetime.now(japan_timezone)
    filename = current_time_japan.strftime("%Y-%m-%d_%H-%M-%S") + "_capture"
    save_directory = "captured_images"
    if os.path.exists(save_directory):
        shutil.rmtree(save_directory)
    os.makedirs(save_directory)
    self._save_path = os.path.join(save_directory, f"{filename}.jpg")

    if ret:
        cv2.imwrite(self._save_path, frame)

    cap.release()

def main():
    capture_image_async()
    time.sleep(5)
    capture_image_async()
    time.sleep(5)
    capture_image_async()

if __name__ == "__main__":
    main()
