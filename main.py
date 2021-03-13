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
introduction = 'タスクを登録する際は1を押してください。'
task_create = 'タスクを登録します'

# Task変数
tasks = ['日報を書く','日報を提出']

print(blank)

print(app_self)
print(current_task)

#タスクの表示
while True:
    sleep(3)
    print(blank)
    print(border)
    for i , task in enumerate(tasks):
        print(f'{i}:{task}')
    print(border)
    select = input(introduction)
    if select == '1' :
        print(task_create)
        input_task = input('登録したい内容を記入してください！')
    else:
        print('1じゃありません')
        break
