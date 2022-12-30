import cv2 
# open a camera for image processing 

def camera(src=0):
    cam = cv2.VideoCapture(src)
    while True:
        status, img = cam.read()
        if not status:
            break
        # action 
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
       # cv2.imshow('video', img)
        #cv2.imshow('video', grey)
        #cv2.imshow('video', rgb)
        # stiching into one window
        cv2.imshow('video', cv2.hconcat([img, rgb]))
        if cv2.waitKey(1) == 27:
            break
    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera()