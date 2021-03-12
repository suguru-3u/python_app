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

app_self = 'ようこそ！\nこのアプリはTodoアプリです。行わなくてはいけないことをぜひ記入してください'
current_task = '現在抱えているタスクはこちらです'

print(app_self)
sleep(3)
print(current_task)
