# video and image display
import cv2

# video capture from webcam example
cap = cv2.VideoCapture("Resources/test_video.mp4")
# cap = cv2.VideoCapture(0)
cap.set(3, 640)     # width
cap.set(4, 480)     # height
cap.set(10, 100)    # brightness

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# It is for removing/deleting created GUI window from screen
# and memory
cv2.destroyAllWindows()

# show image example
# To read image from disk, we use
# cv2.imread function, in below method,
img = cv2.imread("Resources/test_image.png", cv2.IMREAD_COLOR)

# Creating GUI window to display an image on screen
# first Parameter is windows title (should be in string format)
# Second Parameter is image array
cv2.imshow("Cute Kitens", img)

# To hold the window on screen, we use cv2.waitKey method
# Once it detected the close input, it will release the control
# To the next line
# First Parameter is for holding screen for specified milliseconds
# It should be positive integer. If 0 pass an parameter, then it will
# hold the screen until user close it.
cv2.waitKey(0)

# It is for removing/deleting created GUI window from screen
# and memory
cv2.destroyAllWindows()
