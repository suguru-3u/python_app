# coding:utf-8
from time import sleep
import MySQLdb
import os
import sql.py

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

# 説明変数
app_self = 'ようこそ！\nこのアプリはTodoアプリです。行わなくてはいけないことをぜひ記入してください'
current_task = '現在抱えているタスクはこちらです'
blank = ''
border = '-----------------------------------------------------------------------------------------'
introduction = '・タスクを登録する際は1を押してください\n・タスクを編集する際は2を押してください\n・タスクを削除する際は3を押してください\n・アプリを終了する際はqを押してください'
task_create = 'タスクを登録します'

# Change String to int
def input_type_change_int(string):
    return int(string)

# Cheak input blenk
def cheak_input_blenk(yuor_input):
    if not yuor_input:
        return True
    else:
        return False

# Create task
def Create_task():
    print(blank)
    print(task_create)
    input_task_create = input('登録したい内容を記入してください！') 
    if cheak_input_blenk(input_task_create):
        print('**********空白では登録できません**********\n**********入力をやり直してください**********')
    else:
        print('登録します')
        sql.create_task_db(input_task_create)

# Edit task
def Edit_task():
    print(blank)
    print('Task内容を変更します。')
    try:
        input_task_edit = input('変更したいTaskの番号を入力してください')
        # print(f'「{tasks[int(input_task_edit)]}」のTaskでお間違いないですか?')
    except IndexError:
        print(blank)
        print('**********存在する登録番号を入力してください**********')
    except ValueError:
        print(blank)
        print('**********空白で入力しないでください**********')
    else:
        input_yours_edit_select = input('間違いなければyを入力してください')
        if input_yours_edit_select == 'y':
            edit_task = input('変更内容を教えてください')
            print('Task内容を変更します')
            # tasks.pop(int(input_task_edit))
            # tasks.insert(int(input_task_edit), edit_task)

# Delte task
def Delete_task():
    print(blank)
    print('Taskを削除します')
    try:
        input_task_del = input('削除したいTaskの番号を入力してください')
        input_task_del = input_type_change_int(input_task_del)
        sql.tasks.pop(input_task_del)
    except IndexError:
        print(blank)
        print('**********存在する登録番号を入力してください**********')
    except ValueError:
        print(blank)
        print('**********空白で入力しないでください**********')
    else:
        print('削除に成功しました！')

# End judgment
def task_app_end_judgment():
    print(blank)
    print('アプリを終了します。よろしいですか?')
    task_app_end_select = input('終了する場合はyを入力してください')
    if task_app_end_select == 'y':
        print('アプリを終了します。')
        return 1
    else:
        print('アプリを継続します')
        return 2


#Main function
print(blank)
print(app_self)
print(current_task)
while True:
    try:
        sleep(3)
        print(blank)
        print(border)
        # for i , task in enumerate(tasks):
        #     print(f'番号{i}:「{task}」')
        print(border)
        print(blank)
        select = input(introduction)
        if select == '1' :
            Create_task()
        elif select == '2':
            Edit_task()
        elif select == '3':
            Delete_task()
        elif select == 'q':
            end_judgment = task_app_end_judgment()
            if end_judgment == 1:
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
        
