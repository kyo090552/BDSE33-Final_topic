import pandas as pd
import os

# 指定存放CSV文件的資料夾路徑
folder_path = r'./雙北區域資料'  # 確保使用r來避免轉義字符的問題

# # 使用glob模塊找出匹配指定模式的所有CSV文件路徑
# csv_files = glob.glob(folder_path + "/*.csv")


# 初始化一個空的列表來存儲每個文件的DataFrame
dfs = []

# 遍歷找到的CSV文件路徑，讀取每個文件，並將其追加到列表中
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.csv'):
            csv_path = os.path.join(root, file)
            print(csv_path)
            df = pd.read_csv(csv_path)

            df = df.drop('id', axis=1)

            print('ok')
            dfs.append(df)

# 使用concat合併所有DataFrame
all_data = pd.concat(dfs, ignore_index=True)

# 刪除重複行
# 指定要檢查重複值的列名
columns_to_check = ['name', 'star', 'comment', 'class']
# 刪除指定列重複的行，keep='first'表示保留第一次出現的行
all_data = all_data.drop_duplicates(subset=columns_to_check, keep='first')

# 留下 class 特定的值
selected_values = ['冰品飲料店', '無酒精飲料店', '珍珠奶茶', '果汁', '飲料', '飲品分銷商']
filtered_df = all_data[all_data['class'].isin(selected_values)]

# 拆分 coordinate 
filtered_df[['latitude', 'longitude']] = filtered_df['coordinate'].str.split(',', expand=True)
# expand=True允許將拆分的結果作為多個列添加到DF中，而不只是一個列表或Series。

# 删除原始 coordinate 列
filtered_df.drop('coordinate', axis=1, inplace=True)
# inplace=True直接修改原始DF

# 顯示合併後的數據
# print(filtered_df)

# 如果需要，可以將合併後的DataFrame存儲到新的CSV文件中
filtered_df.to_csv('./merged_data.csv', index=False, encoding='utf-8-sig')

