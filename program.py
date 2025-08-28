import pandas as pd
import requests
import os
from urllib.parse import urlparse

# Đường dẫn tới file Excel (bạn có thể sửa lại)
excel_file = 'Book1.xlsx'
sheet_name = 0  # Hoặc tên sheet nếu cần

# Tên cột chứa link ảnh (mặc định lấy cột đầu tiên)
column_name = None  # để tự động lấy cột đầu

# Tạo thư mục lưu ảnh nếu chưa tồn tại
output_folder = 'downloaded_images'
os.makedirs(output_folder, exist_ok=True)

# Đọc file Excel
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Tự động xác định cột nếu chưa được chỉ định
if column_name is None:
    column_name = df.columns[0]

# Duyệt từng dòng để tải ảnh
for index, url in enumerate(df[column_name]):
    if pd.isna(url):
        continue
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Lấy tên file từ URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = f'image_{index}.jpg'
        
        # Lưu ảnh
        file_path = os.path.join(output_folder, filename)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✅ Tải xong: {filename}")
    except Exception as e:
        print(f"❌ Lỗi dòng {index + 1}: {e}")