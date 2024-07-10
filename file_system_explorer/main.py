import os
import time
from file_utils import count_files
from timeout_utils import time_limit, TimeoutException

def search_content(chunk):
    # ここに検索したい内容を記述
    return '検索したい文字列' in chunk

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("このスクリプトはroot権限で実行する必要があります。")
        print("'sudo python3 main.py' もしくはルートユーザーで実行してください。")
        exit(1)

    excluded_directories = [
        '/proc',
        '/dev',
        '/sys',
        '/run'
    ]

    start_time = time.time()
    total_files = 0
    
    try:
        with time_limit(600):  # 10分後にタイムアウト
            total_files = count_files('/', excluded_directories, search_content)  # ルートディレクトリから開始
    except TimeoutException:
        print("\n全体処理がタイムアウトしました。")
    except KeyboardInterrupt:
        print("\nプログラムが中断されました。")
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        print(f"\n調べたファイル数：{total_files}")
        print(f"要した時間：{elapsed_time:.2f}秒")