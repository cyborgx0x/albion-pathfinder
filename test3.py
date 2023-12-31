from ultralytics import YOLO
# import keyboard
# Load a model
import pyautogui
import math
import time
import random
import requests

pyautogui.FAILSAFE = False
model = YOLO('yolov8n.pt')
model = YOLO('model.pt')

# results = model.predict('screen 1920 0 1920 1080', stream=True, vid_stride=True)
results = model.predict('screen', stream=True, vid_stride=True)
# result = model.predict('capture.png', show=True, stream=True)

image  = pyautogui.screenshot()
fast_server_url = "http://localhost:5000/quick_detect"
# requests.post()


def random_move():
    pyautogui.moveTo(random.choice(range(1, 1920)), random.choice(range(1, 1080)), 2, pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(random.choice(range(1,3)))
 


current_state = dict(
    position = (1,2),
)

target_state = dict(
    position = (None, None)
)


next_state = dict(
    position = (None, None)
)

for i in results:
    
    if len(i.boxes.xyxy) != 0:
        k0,j0 = (1920/2, 1080/2)
        x0,y0 = (1920, 1080)
        nearest = 0
        boxes_data = i.boxes.xyxy

        for index, bbox in enumerate(boxes_data):
            
            if i.boxes.conf[index].item() < 0.7:
                continue
            x1, y1, x2, y2 = bbox[0].item(), bbox[1].item(), bbox[2].item(), bbox[3].item()

            k1,j1 = math.ceil((x1+x2)/2), math.ceil((y1+y2)/2)
            
            if (k1-k0)**2 + (j1-j0)**2 < (x0-k0)**2 + (y0-k0)**2:
                x0,y0=k1,j1
                nearest = index
        '''
        after get the nearest point, move the mouse and click :)
        '''
        print(nearest, x0,y0)
        bbox = i.boxes.xyxy[nearest]
        x1, y1, x2, y2 = bbox[0].item(), bbox[1].item(), bbox[2].item(), bbox[3].item()
    
        pyautogui.moveTo(math.ceil((x1+x2)/2), math.ceil((y1+y2)/2), 1, pyautogui.easeInOutQuad)
        pyautogui.click()
        time.sleep(1)
        # pyautogui.moveTo(math.ceil((1920)/2)+random.choice(range(1, 100)), math.ceil((1080/2)+random.choice(range(1, 100))), 0.9, pyautogui.easeInOutQuad)

        
    # else:
    #     # keyboard.press('a')
    #     time.sleep(3)
    #     random_move()

def count_box():
    return None

def where_i_am():
    '''
    Kiểm tra vị trí hiện tại
    '''
    current_position = None
    return current_position

