## Test Plan: Dự đoán loài hoa Iris với thuật toán KNN

### Kế hoạch kiểm thử đã được phê duyệt:
1.  **Thực thi script chính:** Chạy `python iris_knn.py`.
2.  **Xác minh đầu ra:**
    *   Kiểm tra xem script có chạy mà không có lỗi nào không.
    *   Xác nhận rằng script in ra độ chính xác cho mỗi giá trị `k` (từ 1 đến 10).
    *   Xác minh rằng script in ra giá trị "best k".
3.  **Xác minh tạo biểu đồ:** Xác nhận rằng một biểu đồ matplotlib được tạo và hiển thị.

### Kết quả thực thi (Sau khi sửa lỗi import):

**1. Thực thi script chính:**
```bash
python3 iris_knn.py
```
**Output:**
```
5 dòng đầu tiên của dữ liệu Iris:                                                                                                                                                                                 
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  species                                                                                                                              
0                5.1               3.5                1.4               0.2        0                                                                                                                              
1                4.9               3.0                1.4               0.2        0                                                                                                                              
2                4.7               3.2                1.3               0.2        0                                                                                                                              
3                4.6               3.1                1.5               0.2        0                                                                                                                              
4                5.0               3.6                1.4               0.2        0                                                                                                                              
Độ chính xác với k=1: 1.00                                                                                                                                                                                        
Độ chính xác với k=2: 1.00                                                                                                                                                                                        
Độ chính xác với k=3: 1.00                                                                                                                                                                                        
Độ chính xác với k=4: 1.00                                                                                                                                                                                        
Độ chính xác với k=5: 1.00                                                                                                                                                                                        
Độ chính xác với k=6: 1.00                                                                                                                                                                                        
Độ chính xác với k=7: 0.97                                                                                                                                                                                        
Độ chính xác với k=8: 1.00                                                                                                                                                                                        
Độ chính xác với k=9: 1.00                                                                                                                                                                                        
Độ chính xác với k=10: 1.00                                                                                                                                                                                       
                                                                                                                                                                                                                  
Giá trị k tốt nhất dựa trên độ chính xác trên tập kiểm tra là: 1
```
**Kết quả:** PASS

**2. Xác minh đầu ra:**
*   Script chạy mà không có lỗi: PASS
*   Script in ra độ chính xác cho mỗi giá trị `k`: PASS
*   Script in ra giá trị "best k": PASS

**3. Xác minh tạo biểu đồ:**
*   Biểu đồ matplotlib được tạo và hiển thị: PASS (Kiểm tra trực quan)
