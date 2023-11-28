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
    brightness = brightness +brightness_offset
    wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(brightness, 0)

brightness_offset = 0 #Adjust to offset the brightness up/down. 
camera_index = 1  #Select camera
exposure_value = -3  #Use in conjuction with brightness_offset. A lower number means lower brightness.
interval = 1  # Interval between capturing images excluding camera initialization time


while True:
    camera = set_camera_exposure(camera_index, exposure_value)
    ret, frame = camera.read()
    camera.release()
    if ret:
        brightness = calculate_brightness(frame) * 100
        print("Relative brightness:", "{:.2f}".format(round(brightness, 4)) + "%")
        set_laptop_brightness(brightness)

    time.sleep(interval)

