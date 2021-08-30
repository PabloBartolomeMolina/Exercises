import cv2 as cv
import numpy as np


def color_channels():
    image = 'alpine.jpg'
    img = cv.imread(image, cv.IMREAD_UNCHANGED)

    # Matrix to count the color of pixels.
    height, width = img.shape[:2]
    new_img = np.zeros(img.shape)

    # Extract channels.
    (B, G, R) = cv.split(img)
    # Show channels.
    cv.imshow("Display window B", B)
    cv.imshow("Display window G", G)
    cv.imshow("Display window R", R)
    zeros = np.zeros(img.shape[:2], dtype="uint8")
    cv.imshow("Red", cv.merge([zeros, zeros, R]))
    cv.imshow("Green", cv.merge([zeros, G, zeros]))
    cv.imshow("Blue", cv.merge([B, zeros, zeros]))
    k = cv.waitKey(0)

    px = 0
    print(B[0].size)
    img_special = np.zeros(img.shape[:2], dtype="uint8")

    while px < B.size:
        if R[px][0] > G[px][0]:
            img_special[px] = R[px][0]
        px = px + 1
        if px == B[0].size:
            break
