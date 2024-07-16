import subprocess
import time
import pytesseract
from PIL import Image

def check_if_device_connected() -> bool:
    ret = subprocess.run(["adb", "devices"], capture_output=True)
    out = ret.stdout.decode("utf-8")
    device_list = out.split("\n")[1:-2]
    if len(device_list) == 0:
        return False
    return True

def take_screenshot(out_filename: str):
    subprocess.run(["adb", "shell", "screencap", "//storage//emulated//0//Download//screenshot.png"])
    subprocess.run(["adb", "pull", "//storage//emulated//0//Download//screenshot.png", out_filename])

def main():
    if check_if_device_connected():
        print("Device is connected")
    else:
        print("Device is not connected")
        return
    
    # 戻るキーを押す
    subprocess.run(["adb", "shell", "input", "keyevent", "KEYCODE_BACK"])
    time.sleep(1)

    # スクショを撮る
    take_screenshot("screenshot.png")

    img = Image.open("screenshot.png")
    w, h = img.size
    img = img.crop((0, h / 4, w, h / 4 * 3))

    text = pytesseract.image_to_string(img, lang="eng")

    print(text)


if __name__ == '__main__':
    main()
