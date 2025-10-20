# Research Findings: Dự đoán loài hoa Iris (hoa diên vĩ) với Machine Learning

## 1. Giới thiệu
Bài toán dự đoán loài hoa Iris (diên vĩ) là một bài toán kinh điển trong lĩnh vực học máy, thường được sử dụng để giới thiệu các khái niệm cơ bản về phân loại. Mục tiêu là xây dựng một mô hình có khả năng phân loại chính xác loài hoa Iris dựa trên các đặc điểm hình thái của nó.

## 2. Tập dữ liệu Iris
*   **Nguồn gốc:** Tập dữ liệu Iris là một tập dữ liệu nổi tiếng, bao gồm 150 mẫu từ ba loài hoa Iris khác nhau: Setosa, Versicolor và Virginica.
*   **Đặc điểm (Features):** Mỗi mẫu có bốn đặc điểm:
    *   Chiều dài đài hoa (sepal length)
    *   Chiều rộng đài hoa (sepal width)
    *   Chiều dài cánh hoa (petal length)
    *   Chiều rộng cánh hoa (petal width)
*   **Cách tải:** Có thể tải từ trang web của UCI hoặc sử dụng trực tiếp từ thư viện `scikit-learn` trong Python.

## 3. Các bước thực hiện dự đoán loài hoa Iris bằng Machine Learning

### 3.1. Tải và chuẩn bị dữ liệu
*   Sử dụng thư viện `sklearn.datasets` để tải tập dữ liệu Iris.
*   Chuyển đổi dữ liệu thành DataFrame của Pandas để dễ dàng thao tác và phân tích.
*   Chia dữ liệu thành tập huấn luyện (training set) và tập kiểm tra (test set), thường là 80% cho huấn luyện và 20% cho kiểm tra.

### 3.2. Tiền xử lý dữ liệu (nếu cần)
*   Kiểm tra dữ liệu để đảm bảo không có giá trị thiếu hoặc bất thường.
*   Chuẩn hóa dữ liệu có thể cần thiết cho một số thuật toán.

### 3.3. Trực quan hóa dữ liệu
*   Sử dụng các biểu đồ như biểu đồ cặp (pair plots) với thư viện Seaborn để hiểu mối quan hệ giữa các đặc điểm và loài hoa. Điều này giúp nhận biết các mẫu có thể chỉ ra sự tách biệt giữa các loài.

### 3.4. Chọn thuật toán Machine Learning
Có nhiều thuật toán phân loại có thể được áp dụng cho bài toán này, bao gồm:
*   **K-Nearest Neighbors (KNN):** Phân loại dựa trên việc xem xét k hàng xóm gần nhất.
*   **Logistic Regression:** Thuật toán phân loại tuyến tính.
*   **Support Vector Machine (SVM):** Phương pháp hiệu quả trong bài toán phân lớp dữ liệu.
*   **Naïve Bayes:** Thuật toán dựa trên định lý Bayes.
*   **Random Forest:** Thuật toán học tập tổng hợp sử dụng nhiều cây quyết định.
*   **Decision Tree:** Thuật toán phân loại dựa trên cấu trúc cây.

### 3.5. Huấn luyện mô hình
*   Áp dụng thuật toán đã chọn lên tập dữ liệu huấn luyện.

### 3.6. Đánh giá mô hình
*   Sử dụng tập dữ liệu kiểm tra để đánh giá hiệu suất của mô hình.
*   Các chỉ số đánh giá phổ biến bao gồm:
    *   **Độ chính xác (Accuracy Score):** Tỷ lệ giữa số lượng dự đoán chính xác và tổng số mẫu trong tập kiểm tra.
*   Nhiều thuật toán như Naïve Bayes, Random Forest và KNN đều cho độ chính xác cao (trên 95%).

## 4. Ví dụ triển khai (Python và scikit-learn)
Một ví dụ điển hình sẽ bao gồm các bước sau:
1.  Tải dữ liệu Iris.
2.  Chia dữ liệu thành tập huấn luyện và tập kiểm tra.
3.  Áp dụng một thuật toán phân loại (ví dụ: KNN).
4.  Huấn luyện mô hình.
5.  Đánh giá mô hình và tính toán độ chính xác.
6.  Trực quan hóa kết quả (ví dụ: biểu đồ độ chính xác với các giá trị k khác nhau cho KNN).
