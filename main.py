"""
<Read me>
このアプリはPythonとSQLのみを使用したTodoアプリです。
機能は登録、削除、編集、更新が行えます。データはMySQLに保存しておきます。
このファイルは操作する際にmainで使用するファイルです。
必要なもの
・todoのクラスファイル
・登録、削除、編集、更新機能
・入力チェック機能
"""

# coding:utf-8
from time import sleep
import os
from function import input_task
from function import cheak_input_blenk
from function import Create_task
from function import Edit_task
from function import Delete_task
from function import task_app_end_judgment
from sql import get_tasks


# 説明変数
app_self = 'ようこそ！\nこのアプリはTodoアプリです。行わなくてはいけないことをぜひ記入してください'
current_task = '現在抱えているタスクはこちらです'
blank = ''
border = '-----------------------------------------------------------------------------------------'
introduction = '・タスクを登録する際は1を押してください\n・タスクを編集する際は2を押してください\n・タスクを削除する際は3を押してください\n・アプリを終了する際はqを押してください'
task_create = 'タスクを登録します'

#Main function
print(blank)
print(app_self)
print(current_task)
while True:
    try:
        sleep(3)
        print(blank)
        print(border)
        get_tasks()
        print(border)
        print(blank)
        select = input(introduction)
        if select == '1' :
            if cheak_input_blenk(input_task):
                print('**********空白では登録できません**********\n**********入力をやり直してください**********')
            else:
                Create_task()
        elif select == '2':
            Edit_task()
        elif select == '3':
            Delete_task()
        elif select == 'q':
            end_judgment = task_app_end_judgment()
            if end_judgment == 1:
                os.system('mysql.server stop')
                print('Mysql停止')
                break
            else:
                continue
        else:
            print(blank)
            print('正しく入力してください')
    except KeyboardInterrupt:
        print(blank)
        print(blank)
        print('**********終了する場合はqを入力してください**********')
        
