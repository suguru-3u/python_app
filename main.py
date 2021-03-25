"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
<Read me>
このアプリはPythonとSQLを使用したTodoアプリです。
機能は登録、削除、編集、更新が行えます。データはMySQLに保存しています。
このファイルは操作する際にメインで使用するファイルです。
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# coding:utf-8
import os
from time import sleep
from task_design_document import task_document
from function import task_app_function
from sql import task_db

#メイン処理
task_db.sql_start()
task_app_function.blank()
print(task_app_function.app_self)
print(task_app_function.current_task)
while True:
    try:
        sleep(3)
        task_app_function.blank()
        print(task_app_function.border)
        task_db.get_tasks()
        print(task_app_function.border)
        task_app_function.blank()
        select = input(introduction)
        if select == '1' :
            task_document.Create_task()
        elif select == '2':
            task_document.Edit_task()
        elif select == '3':
            task_document.Delete_task()
        elif select == 'q':
            end_judgment = task_app_function.task_app_end_judgment()
            if end_judgment == 1:
                task_db.sql_stop()
                break
            else:
                continue
        else:
            task_app_function.blank()
            print('正しく入力してください')
    except KeyboardInterrupt:
        task_app_function.blank()
        task_app_function.blank()
        print('**********終了する場合はqを入力してください**********')