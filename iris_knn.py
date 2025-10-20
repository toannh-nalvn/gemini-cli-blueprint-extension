import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. Tải dữ liệu Iris
iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['species'] = iris.target

# Hiển thị 5 dòng đầu tiên của dữ liệu
print("5 dòng đầu tiên của dữ liệu Iris:")
print(data.head())

# 2. Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X = data.drop('species', axis=1)
y = data['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Áp dụng thuật toán K-Nearest Neighbors (KNN)
# Thử nghiệm với các giá trị k khác nhau
k_values = range(1, 11)
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)
    print(f"Độ chính xác với k={k}: {accuracy:.2f}")

# 4. Vẽ biểu đồ so sánh độ chính xác với các giá trị k khác nhau
plt.figure(figsize=(10, 6))
plt.plot(k_values, accuracies, marker='o')
plt.title('Độ chính xác của mô hình KNN với các giá trị k khác nhau')
plt.xlabel('Giá trị k')
plt.ylabel('Độ chính xác')
plt.xticks(k_values)
plt.grid(True)
plt.show()

# 5. Giải thích về sự lựa chọn giá trị k tốt nhất
best_k = k_values[accuracies.index(max(accuracies))]
print(f"\nGiá trị k tốt nhất dựa trên độ chính xác trên tập kiểm tra là: {best_k}")
