# import glob

# import pandas as pd

# forler = './運動設施/*'
# file_paths = glob.glob(folder)
# combined_df = pd.DataFrame()
# dfs = []
# for file_path in file_paths:
#     df = pd.read_csv(file_path)
#     print(f"Successfully read file: {file_path}, Shape: {df.shape}")
#     dfs.append(df)
# combined_df = pd.concat(dfs, ignore_index=True)
# columns_to_check = ['name', 'star', 'comment', 'class']
# all_data = combined_df.drop_duplicates(subset=columns_to_check, keep='first')

# all_data[['latitude', 'longitude']] = all_data['coordinate'].str.split(',', expand=True)
# all_data.drop('coordinate', axis=1, inplace=True)
# try:
#     all_data.to_csv('./雙北運動設施.csv', index=False, encoding='utf-8')
#     print("檔案成功存儲！")
# except Exception as e:
#     print(f"發生錯誤：{e}")

import glob

import pandas as pd

folder = './運動設施/*'
file_paths = glob.glob(folder)
dfs = []

for file_path in file_paths:
    df = pd.read_csv(file_path)
    print(df)
    df = df.drop('id', axis=1)
    print(f"Successfully read file: {file_path}, Shape: {df.shape}")
    dfs.append(df)

if dfs:
    combined_df = pd.concat(dfs, ignore_index=True)
    columns_to_check = ['name', 'star', 'comment', 'class']
    
    # Assuming 'coordinate' column exists
    combined_df[['latitude', 'longitude']] = combined_df['coordinate'].str.split(',', expand=True)
    combined_df.drop('coordinate', axis=1, inplace=True)

    # Drop duplicates based on specified columns
    all_data = combined_df.drop_duplicates(subset=columns_to_check, keep='first')
    all_data.to_csv('./雙北運動設施.csv', index=False, encoding='utf-8-sig')
    print("檔案成功存儲！")
