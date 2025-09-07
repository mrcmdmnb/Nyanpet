import cv2 as cv
import pygame
vol=0.1
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("nyanpet/snd/nyancat.mp3")
pygame.mixer.music.set_volume(vol)
cv.namedWindow("Nyan",cv.WINDOW_NORMAL)
cv.waitKey(1)
cv.resizeWindow("Nyan", 256, 144)
cv.moveWindow("Nyan",1400,700)
i=1
pygame.mixer.music.play()
while True:
    cv.namedWindow("Nyan",cv.WINDOW_NORMAL) 
    img=cv.imread(f"nyanpet/pic/{str(i)}.jpg")
    cv.imshow("Nyan",img)
    key=cv.waitKey(120)
    if key==27:
        cv.destroyAllWindows() 
        pygame.mixer.music.stop()
        break
    if i!=8:  
        i=i+1
    else:
        i=1