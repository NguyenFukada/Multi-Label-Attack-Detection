import pandas as pd

# Đọc dữ liệu từ file CSV vào DataFrame
df = pd.read_csv('f3.csv')

# Trộn lẫn các hàng
df_shuffled = df.sample(frac=1).reset_index(drop=True)

# Lưu kết quả vào file CSV mới
df_shuffled.to_csv('f3-draft.csv', index=False)
