# Dự đoán loài hoa Iris với thuật toán KNN

## Giới thiệu
Đây là một dự án đơn giản nhằm mục đích dự đoán loài hoa Iris (diên vĩ) sử dụng thuật toán phân loại K-Nearest Neighbors (KNN). Dự án này minh họa các bước cơ bản trong một quy trình học máy, từ tải dữ liệu, tiền xử lý, xây dựng mô hình, đánh giá và trực quan hóa kết quả.

## Cài đặt
Để chạy dự án này, bạn cần cài đặt các thư viện Python sau:

```bash
pip install -r requirements.txt
```

## Cách chạy
Sau khi cài đặt các thư viện, bạn có thể chạy script chính bằng lệnh:

```bash
python iris_knn.py
```

Script sẽ tải dữ liệu Iris, huấn luyện mô hình KNN với các giá trị `k` khác nhau, đánh giá độ chính xác và hiển thị biểu đồ so sánh độ chính xác.

## Kết quả
Chương trình sẽ in ra độ chính xác của mô hình KNN cho từng giá trị `k` và hiển thị một biểu đồ trực quan hóa độ chính xác theo `k`. Biểu đồ này giúp xác định giá trị `k` tối ưu cho bài toán.