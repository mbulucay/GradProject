import cv2

# Load the image
image = cv2.imread('colorscale_jet.jpg')

# Ensure the image was successfully loaded
if image is not None:
    # Display the image
    cv2.imshow('Image', image)
    cv2.waitKey(0)

    # Get the coordinates of the pixel to pick
    x = 50  # X coordinate of the pixel
    y = 15  # Y coordinate of the pixel

    # Get the color value of the pixel at the specified coordinates
    b, g, r = image[y, x]  # OpenCV uses BGR order

    # Print the color values
    print('B:', b)
    print('G:', g)
    print('R:', r)

    # Close the image window
    cv2.destroyAllWindows()
else:
    print('Failed to load the image.')
