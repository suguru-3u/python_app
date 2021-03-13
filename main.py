# coding:utf-8
from time import sleep

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
introduction = '・タスクを登録する際は1を押してください。\n・タスクを編集する際は2を押してください\n・タスクを削除する際は3を押してください'
task_create = 'タスクを登録します'

# Task変数
tasks = ['日報を書く','日報を提出']

print(blank)

print(app_self)
print(current_task)

# Change String to int
def input_type_change_int(string):
    return int(string)

# Create task
def Create_task():
    print(task_create)
    input_task_create = input('登録したい内容を記入してください！') 
    tasks.append(input_task_create)

# Edit task
def Edit_task():
    print('Task内容を変更します。')
    input_task_edit = input('変更したいTaskの番号を入力してください')
    print(f'「{tasks[int(input_task_edit)]}」のTaskでお間違いないですか?')
    input_yours_edit_select = input('間違いなければyを入力してください')
    if input_yours_edit_select == 'y':
        edit_task = input('変更内容を教えてください')
        print('Task内容を変更します')
        tasks.pop(int(input_task_edit))
        tasks.insert(int(input_task_edit), edit_task)

# Delte task
def Delete_task():
    print('Taskを削除します')
    input_task_del = input('削除したいTaskの番号を入力してください')
    input_task_del = input_type_change_int(input_task_del)
    tasks.pop(input_task_del)


#タスクの表示
while True:
    sleep(3)
    print(blank)
    print(border)
    for i , task in enumerate(tasks):
        print(f'{i}:{task}')
    print(border)
    print(blank)
    select = input(introduction)
    if select == '1' :
        Create_task()
    elif select == '2':
        Edit_task()
    elif select == '3':
        Delete_task()
    else:
        print('1じゃありません')
        break
