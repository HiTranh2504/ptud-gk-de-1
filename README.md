# 🏆 Thi giữa kỳ - Phát triển Ứng dụng (PTUD)

## 📝 **Thông tin sinh viên**
- **Họ và Tên:** Đường Chí Trung
- **MSSV:** 22655141
- **STT:** 66
- **Môn học:** Phát triển Ứng dụng (PTUD)
- **Nội dung:** Xây dựng ứng dụng Blog với Django

---

## 📌 **Mô tả bài làm**
### 🅰 **Xây dựng ứng dụng Blog**
Ứng dụng Blog cho phép người dùng thực hiện các chức năng sau:
- Xem danh sách bài viết.
- Viết bài mới.
- Chỉnh sửa và xóa bài viết (theo quyền hạn).
- Bình luận trên bài viết.

### 🅱 **Áp dụng Layout 1: Single Column (Một cột)**
Layout Single Column (Một cột) là một cách tổ chức giao diện phổ biến cho các trang blog, nơi nội dung chính được hiển thị trong một cột dọc, giúp người dùng tập trung vào bài viết mà không bị phân tâm bởi quá nhiều yếu tố xung quanh.
Ứng dụng sử dụng **Layout 1**, trong đó:
  1. Trải nghiệm đọc tốt hơn
  2. Tương thích tốt với thiết bị di động
  3. Dễ dàng điều hướng và quản lý nội dung
  4. Cải thiện tốc độ tải trang
  5. Dễ dàng mở rộng và nâng cấp giao diện

### 🅳 **Thực hiện Option 1: Viết thêm trang dashboard thể hiện thông tin trang blog của mình**
Chức năng Dashboard giúp người dùng dễ dàng theo dõi tổng quan hoạt động trên blog. Trang này sẽ hiển thị thống kê quan trọng và trạng thái blog một cách trực quan.
Chức năng **phân loại user** thành các nhóm quyền hạn:
📌 Dashboard sẽ bao gồm các thông tin sau:
📄 Tổng số bài viết: Hiển thị tổng số bài đã đăng.
✍️ Số bài viết của tôi: Tổng số bài do người dùng đăng tải.
💬 Tổng số bình luận: Thống kê tổng số bình luận trên blog.
📊 Hiển thị bài viết: Hiển thị danh sách bài viết user đã đăng.
🔥 Thông tin chi tiết: Hiển thị chi tiết người đăng, ngày đăng và thời gian đăng.

💡 **Admin có thể thay đổi quyền của User từ trang quản trị.**  
---

## 🚀 **Hướng dẫn cài đặt và chạy ứng dụng**
### 1️⃣ **Clone repository**
Mở terminal hoặc command prompt và chạy lệnh:
```sh
https://github.com/HiTranh2504/ptud-gk-de-1.git
```

### 2️⃣ **Tạo môi trường ảo (`venv`)**
```sh
 python -m venv venv
```

### 3️⃣ **Kích hoạt môi trường ảo**
- **Windows:**
  ```sh
  ./venv/Scripts/Activate.ps1
  ```
- **Mac/Linux:**
  ```sh
  source venv/bin/activate
  ```

### 4️⃣ **Cài đặt dependencies**
```sh
 pip install -r requirements.txt
```

### 5️⃣ **Thiết lập database**
```sh
 python manage.py makemigrations
 python manage.py migrate
```

### 6️⃣ **Chạy ứng dụng**
```sh
 python manage.py runserver
```

Sau đó, mở trình duyệt và truy cập **[http://127.0.0.1:8000](http://127.0.0.1:8000)** để sử dụng ứng dụng.
