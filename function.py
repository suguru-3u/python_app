"""
    このファイルはTodoアプリの登録,編集、削除機能について書いてあるファイルです。
    各機能はMysqlと接続するためにsqlファイルのメソッドをimportしている。
"""

from sql import create_task_db
from sql import delete_task_db
from sql import edit_task_db

class task_app_function:

   
    blank = ''
   


    # アプリ終了判定機能
    def task_app_end_judgment():
        print(task_app_function.blank)
        print('アプリを終了します。よろしいですか?')
        task_app_end_select = input('終了する場合はyを入力してください')
        if task_app_end_select == 'y':
            print('アプリを終了します。')
            return 1
        else:
            print('アプリを継続します')
            return 2