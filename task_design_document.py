"""
このファイルはユーザーが入力したタスクを受け取るようのクラスです。
このクラス自体には受け取るだけの機能しかありませんが敬承を使い機能の拡充を行っております。
"""

from sql import create_task_db
from sql import delete_task_db
from sql import edit_task_db

class task_document:

    task_create = 'タスクを登録します'
    app_self = 'ようこそ！\nこのアプリはTodoアプリです。行わなくてはいけないことをぜひ記入してください'
    current_task = '現在抱えているタスクはこちらです'
    blank = ''
    border = '----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
    introduction = '・タスクを登録する際は1を押してください\n・タスクを編集する際は2を押してください\n・タスクを削除する際は3を押してください\n・アプリを終了する際はqを押してください'
    task_create = 'タスクを登録します'


    # コンストラクト
    # def __init__(self):
    #   pass

    def blank():
        print('')

    def input_task():
        input_task = input('登録したいTaskを入力してください')
        return input_task

    # Change String to int
    def input_type_change_int(string):
        return int(string)

    # Cheak input blank
    def cheak_input_blenk(task_string):
        if not task_string:
            return True
        else:
            return False

    # Task登録処理
    def Create_task():
        task_document.blank()
        input_task = input('登録したいTaskを入力してください')
        task_document.blank()
        if task_document.cheak_input_blenk(input_task):
                print('**********空白では登録できません********************入力をやり直してください**********')
                print('登録を中止します')
                return False
        else:
            print(f'登録する内容は「{input_task}」でお間違え無いですか？')
            your_select = input('お間違いなければ「y」を入力してください')
            if your_select == 'y':
                print('登録を開始します')
                create_task_db(input_task)
                print('登録が成功しました')
                return True
            else:
                return False
                    