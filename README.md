# file_system_explorer
特定の内容を含むファイルを検索できるソフトウェア

このプロジェクトは、Linuxファイルシステムをスキャンし、アクセス可能なファイルの数をカウントするPythonスクリプトです。また、特定の内容を含むファイルを検索することもできます。

## 特徴

- ルートディレクトリから再帰的にファイルをスキャン
- 特定のディレクトリ（/proc, /dev, /sys, /run）を除外
- 個々のファイル処理と全体の処理にタイムアウトを設定
- 処理したディレクトリ数、ファイル数、タイムアウトしたファイル数を報告
- カスタム検索関数を使用して、特定の内容を含むファイルを検索可能

## 使用方法

このスクリプトはroot権限で実行する必要があります：

## ファイル構成

- `main.py`: メインスクリプト。プログラムのエントリーポイント。
- `file_utils.py`: ファイル処理関連の関数を含むモジュール。
- `timeout_utils.py`: タイムアウト処理関連の関数を含むモジュール。

## カスタム検索

main.py 内の `search_content` 関数を編集することで、特定の内容を検索できます。例：

```python
def search_content(chunk):
    return b'検索したい文字列' in chunk
