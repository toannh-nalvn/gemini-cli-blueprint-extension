## Plan: Dự đoán loài hoa Iris với thuật toán KNN

### 1. Chuẩn bị môi trường và cấu trúc dự án
*   Tạo file `iris_knn.py` để chứa mã nguồn chính.
*   Tạo file `requirements.txt` để liệt kê các thư viện cần thiết.
*   Tạo file `README.md` để hướng dẫn sử dụng và mô tả dự án.

### 2. Cài đặt các thư viện cần thiết
*   Sử dụng `pip install pandas scikit-learn matplotlib seaborn` để cài đặt các thư viện.

### 3. Tải và chuẩn bị dữ liệu
*   Trong `iris_knn.py`, tải tập dữ liệu Iris bằng `sklearn.datasets.load_iris()`.
*   Chuyển đổi dữ liệu thành Pandas DataFrame.
*   Chia dữ liệu thành tập huấn luyện (training set) và tập kiểm tra (test set) với tỷ lệ 80/20, sử dụng `train_test_split`.

### 4. Xây dựng và huấn luyện mô hình KNN
*   Khởi tạo mô hình `KNeighborsClassifier`.
*   Thực hiện vòng lặp để thử nghiệm các giá trị `k` khác nhau (ví dụ: từ 1 đến 10).
*   Huấn luyện mô hình KNN trên tập dữ liệu huấn luyện cho mỗi giá trị `k`.

### 5. Đánh giá mô hình
*   Dự đoán trên tập dữ liệu kiểm tra cho mỗi mô hình KNN đã huấn luyện.
*   Tính toán độ chính xác (Accuracy Score) cho mỗi giá trị `k` bằng `accuracy_score`.

### 6. Trực quan hóa kết quả
*   Sử dụng `matplotlib` và `seaborn` để vẽ biểu đồ thể hiện mối quan hệ giữa giá trị `k` và độ chính xác của mô hình.
*   Xác định và hiển thị giá trị `k` tối ưu dựa trên biểu đồ.

### 7. Hoàn thiện tài liệu
*   Cập nhật `requirements.txt` với các thư viện đã sử dụng.
*   Cập nhật `README.md` với mô tả dự án, hướng dẫn cài đặt, cách chạy và giải thích kết quả.
