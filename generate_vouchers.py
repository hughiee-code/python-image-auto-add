from PIL import Image
import os

# File background
background_path = 'image (1).jpg'
# Folder chứa các ảnh barcode đã tải
barcode_folder = 'downloaded_images'
# Folder đầu ra
output_folder = 'output_vouchers'
os.makedirs(output_folder, exist_ok=True)

# Vị trí và kích thước chèn ảnh barcode vào (có thể thay đổi tùy theo layout)
barcode_box = (478, 143, 780, 251)  # (left, top, right, bottom)

# Load ảnh nền mẫu
background_template = Image.open(background_path)

# Duyệt từng file barcode trong folder
for filename in os.listdir(barcode_folder):
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        continue

    # Mở background mới mỗi lần để giữ nguyên gốc
    bg = background_template.copy()

    # Mở ảnh barcode
    barcode_path = os.path.join(barcode_folder, filename)
    barcode_img = Image.open(barcode_path).convert("RGBA")

    # Resize barcode để vừa với vị trí dán
    width = barcode_box[2] - barcode_box[0]
    height = barcode_box[3] - barcode_box[1]
    barcode_resized = barcode_img.resize((width, height))

    # Dán barcode vào nền
    bg.paste(barcode_resized, barcode_box[:2], barcode_resized)

    # Lưu ảnh mới
    output_path = os.path.join(output_folder, f'voucher_{filename}')
    bg.save(output_path)

    print(f'✅ Tạo xong: {output_path}')
