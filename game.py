import pyautogui
from PIL import ImageGrab, ImageOps
from numpy import *
import time


class RexBot:
    def __init__(self, restart, dino):
        self.restart = restart
        self.dino = dino

    def restart_game(self):
        pyautogui.click(self.restart)

    def jump(self):
        pyautogui.keyDown('space')
        time.sleep(0.05)
        pyautogui.keyDown('space')
    
    def grab_image(self):
        box = (self.dino[0] + 35, self.dino[1], self.dino[0] + 75, self.dino[1] + 30)
        image = ImageGrab.grab(box)     
        gray_image = ImageOps.grayscale(image)
        arr = array(gray_image.getcolors())
        return arr.sum()
    
def main():
    time.sleep(3)
    bot = RexBot((959, 448), (726, 453))
    bot.restart_game()
    while True:
        if bot.grab_image() != 1447:          
            bot.jump()


if __name__ == '__main__':
    main()