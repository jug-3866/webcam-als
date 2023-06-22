# webcam-als
Ambient Light Sensor through a webcam/camera. ~~This will probably be written in another langauge because python is slow/uses almost 8% CPU on my laptop.~~ After changing to the DSHOW back-end, the CPU usage is less than 0.5%!!!
## Some Windows Laptops don't come with ambient light sensors like Macs.
I learned this from having to constantly adjust the brightness on my laptop when moving around. Frustrated, I decided to make this script.
## How does it work?
- Turn off auto exposure and choose an exposure
- Take an image and examine the relative brightness and put it on a scale from 0 to 1
- Use the relative brightness to set the screen brightness
- Loop!
