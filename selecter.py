import cv2
 
# Load ảnh
image = cv2.imread("image (1).jpg")
 
# Dùng hàm chọn ROI bằng chuột
roi = cv2.selectROI("Select ROI", image, fromCenter=False, showCrosshair=True)
 
x, y, w, h = roi
print(f"Vị trí: x={x}, y={y}, width={w}, height={h}")
print(f"Diện tích: {w*h}")
 
# Vẽ khung nếu muốn
cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("ROI", image)
cv2.waitKey(0)
cv2.destroyAllWindows()