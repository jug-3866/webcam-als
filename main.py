import wmi
import cv2
import time

def set_camera_exposure(camera_index, exposure_value):
    camera = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
    camera.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
    camera.set(cv2.CAP_PROP_EXPOSURE, exposure_value)
    return camera
def calculate_brightness(image):
    average_brightness = cv2.mean(image)[0] / 255.0
    return average_brightness
def set_laptop_brightness(brightness):
    brightness = int((brightness * 100)+brightness_bump)
    wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(brightness, 0)

brightness_bump = 0 #Adjust to bump up the brightness or lower if not working
camera_index = 1  #select camera
exposure_value = -5  #Use in conjuction with brightness_bump 
interval = 1  # Interval between capturing images excluiding camera initialization time


while True:
    camera = set_camera_exposure(camera_index, exposure_value)
    ret, frame = camera.read()
    camera.release()
    if ret:
        brightness = calculate_brightness(frame)
        print("Relative brightness:", brightness)
        set_laptop_brightness(brightness)

    camera.set(cv2.CAP_PROP_EXPOSURE, exposure_value)
    time.sleep(interval)

