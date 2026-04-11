# [LAB - 1] API

## 1. Thông tin sinh viên
* **Họ và tên:** Đinh Võ Thủy Tiên
* **MSSV:** 24120148
* **Môn học:** Tư duy tính toán
* **Lớp học:** CQ2024/3

## 2. Thông tin mô hình trên Hugging Face
* **Bài toán:** Tóm tắt văn bản.
* **Mô hình lựa chọn:** `facebook/bart-large-cnn`.
* **Liên kết:** [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn)
* **Mô tả chức năng API:** Hệ thống nhận dữ liệu đầu vào là một đoạn văn bản dài bằng tiếng Anh (tối thiểu 50 ký tự). Sau đó, API sẽ gọi đến Hugging Face Inference API để xử lý và trả về một bản tóm tắt ngắn gọn, giữ nguyên được ý chính của đoạn văn bản gốc.

## 3. Hướng dẫn cài đặt
  **Yêu cầu:** đã cài đặt `Python 3.11.x` trở lên, bản 64-bit Stable.
1. Sao chép Access Token của Hugging Face -> Vào file .env tại thư mục gốc -> Dán vào thay cho `hf_chuoi_token_cua_ban_o_day`:
   ```bash
   HF_TOKEN=hf_chuoi_token_cua_ban_o_day
   ```
2.  Thiết lập môi trường ảo:
* Mở `Terminal` tại thư mục dự án và chạy dòng lệnh:
    ```bash
    # Windows:
    # Kích hoạt venv
    python -m venv venv
    # Vào file venv để xem có thư mục bin hay Scripts rồi chọn dòng lệnh tương ứng
    .\venv\bin\Activate.ps1
    .\venv\Scripts\Activate.ps1
    
    ```
3. Chạy lệnh cài đặt thư viện:
   ```bash
   pip install -r requirements.txt
   ```

## 4. Hướng dẫn chạy chương trình
  Khởi động máy chủ API bằng uvicorn: Vào `Terminal` -> Chạy dòng lệnh:
   ```bash
   uvicorn main:app --reload
   ```
* Hệ thống sẽ hoạt động tại địa chỉ: `http://127.0.0.1:8000`.
* Tài liệu API tương tác (Swagger UI) có sẵn tại: `http://127.0.0.1:8000/docs`.
  + Nhấn GET / -> Try it out -> Execute
  + Nhấn GET /health -> Try it out -> Execute
  + Nhấn POST /predict -> Try it out -> Dán đoạn text cần tóm tắt (không chứa dấu " và xuống hàng) -> Execute

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
      "text": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. 
Its base is square, measuring 125 metres (410 ft) on each side. During its construction, 
the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, 
a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. 
It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, 
it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, 
the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct."
  }
  ```
  * Response (.JSON):
    *  ```original_length```: độ dài gốc của đoạn văn bản đầu vào
    *  ```summary_text```: đoạn văn bản sau khi đã tóm tắt

  ```bash
  {
    "original_length": 749,
    "summary_text": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building. During its construction, it surpassed the Washington Monument to become the tallest man-made structure in the world. Excluding transmitters, it is the second tallest free-standing structure in France after the Millau Viaduct."
  }
  ```
## 6. Liên kết video demo
https://drive.google.com/file/d/1rcq92StkPMxlkqEspTCSjocXRzQ9XhVQ/view?usp=drive_link