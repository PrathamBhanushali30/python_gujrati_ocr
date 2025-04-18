import cv2

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # denoised = cv2.GaussianBlur(gray, (5, 5), 0)
    # _, thresh = cv2.threshold(denoised, 150, 255, cv2.THRESH_BINARY)
    output_path = image_path.replace('.png', '_preprocessed.png')
    cv2.imwrite(output_path, gray)
    return output_path