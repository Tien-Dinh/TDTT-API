# [LAB - 1] API

## 1. Thông tin sinh viên
* **Họ và tên:** Đinh Võ Thủy Tiên
* **MSSV:** 24120148
* **Môn học:** Tư duy tính toán
* **Lớp học:** CQ2024/3

## 2. Thông tin mô hình trên Hugging Face
* **Bài toán:** Tóm tắt văn bản.
* **Mô hình lựa chọn:** `facebook/bart-large-cnn`.
* **Liên kết:** [Ở đây](https://huggingface.co/facebook/bart-large-cnn)
* **Mô tả chức năng API:** Hệ thống nhận dữ liệu đầu vào là một đoạn văn bản dài bằng tiếng Anh (tối thiểu 50 ký tự). Sau đó, API sẽ gọi đến Hugging Face Inference API để xử lý và trả về một bản tóm tắt ngắn gọn, giữ nguyên được ý chính của đoạn văn bản gốc.

## 3. Hướng dẫn cài đặt
  **Yêu cầu:** đã cài đặt Python 3.9 trở lên.
1. Mở terminal tại thư mục chứa dự án và chạy lệnh cài đặt thư viện:
   ```bash
   pip install -r requirements.txt
   ```
2. Tạo một file .env tại thư mục gốc và thêm Access Token của Hugging Face:
   ```bash
   HF_TOKEN=hf_chuoi_token_cua_ban_o_day
   ```
## 4. Hướng dẫn chạy chương trình
  Khởi động máy chủ API bằng uvicorn
   ```bash
   uvicorn main:app --reload
   ```
## 5. Hướng dẫn gọi API và ví dụ request/response
  Bạn có thể kiểm thử API bằng cách chạy file script có sẵn:
  ```bash
  python test_api.py
  ```
  Ví dụ request/response đúng định dạng:
  * Endpoint: POST /predict
  * Request (.JSON):
  ```bash
  {
      "text": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris..."
  }
  ```
  * Response (.JSON): 

  ```bash
  {
    "original_length": 560,
    "summary_text": "The Eiffel Tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building. During its construction, it surpassed the                           Washington Monument to become the tallest man-made structure in the world."
  }
  ```
## 6. Liên kết video demo
