import os
from timeout_utils import time_limit, TimeoutException

def file_generator(path, exclude_dirs):
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_dirs]
        yield root, files

def process_file(file_path, search_function):
    try:
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(32768)  # 32KBずつ読み込む
                if not chunk:
                    break
                if search_function(chunk):
                    return True  # 検索条件に合致した場合
        return False  # ファイル全体を読んで条件に合致しなかった場合
    except Exception as e:
        print(f"ファイルアクセスエラー: {file_path}")
        print(f"エラー詳細: {str(e)}")
        return False

def count_files(path, exclude_dirs, search_function):
    file_count = 0
    dir_count = 0
    timeout_files = 0

    try:
        for root, files in file_generator(path, exclude_dirs):
            dir_count += 1
            print(f"現在のディレクトリ: {root} (処理済みディレクトリ: {dir_count})")
            
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with time_limit(5):  # 各ファイルの処理に5秒のタイムアウトを設定
                        if process_file(file_path, search_function):
                            file_count += 1
                        if file_count % 1000 == 0:
                            print(f"現在のファイル数：{file_count}", end='\r')
                except TimeoutException:
                    print(f"ファイル処理タイムアウト: {file_path}")
                    timeout_files += 1
    except TimeoutError:
        print("全体処理がタイムアウトしました")
    except KeyboardInterrupt:
        print("\nプログラムが中断されました。")
    finally:
        print(f"\n処理したディレクトリ数: {dir_count}")
        print(f"タイムアウトしたファイル数: {timeout_files}")
        return file_count