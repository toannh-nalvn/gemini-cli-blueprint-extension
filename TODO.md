## TODO List: Dự đoán loài hoa Iris với thuật toán KNN

*   **[setup]** Tạo file `iris_knn.py`.
*   **[setup]** Tạo file `requirements.txt`.
*   **[setup]** Tạo file `README.md`.
*   **[environment]** Cài đặt các thư viện cần thiết: `pip install pandas scikit-learn matplotlib seaborn`.
*   **[data_prep]** Trong `iris_knn.py`:
    *   Tải tập dữ liệu Iris.
    *   Chuyển đổi dữ liệu thành Pandas DataFrame.
    *   Chia dữ liệu thành tập huấn luyện và tập kiểm tra (80/20).
*   **[model_dev]** Trong `iris_knn.py`:
    *   Khởi tạo mô hình `KNeighborsClassifier`.
    *   Thực hiện vòng lặp để thử nghiệm các giá trị `k` từ 1 đến 10.
    *   Huấn luyện mô hình KNN trên tập huấn luyện cho mỗi giá trị `k`.
*   **[evaluation]** Trong `iris_knn.py`:
    *   Dự đoán trên tập kiểm tra cho mỗi mô hình.
    *   Tính toán độ chính xác (Accuracy Score) cho mỗi giá trị `k`.
*   **[visualization]** Trong `iris_knn.py`:
    *   Vẽ biểu đồ mối quan hệ giữa giá trị `k` và độ chính xác.
    *   Xác định và hiển thị giá trị `k` tối ưu.
*   **[documentation]** Cập nhật `requirements.txt` với các thư viện đã sử dụng.
*   **[documentation]** Cập nhật `README.md` với mô tả dự án, hướng dẫn cài đặt, cách chạy và giải thích kết quả.
