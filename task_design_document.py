"""
このファイルはユーザーが入力したタスクを受け取るようのクラスです。
このクラス自体には受け取るだけの機能しかありませんが敬承を使い機能の拡充を行っております。
"""

from sql import create_task_db
from sql import delete_task_db
from sql import edit_task_db
from sql import edit_search_task_db

class task_document:

    task_create = 'タスクを登録します'
    app_self = 'ようこそ！\nこのアプリはTodoアプリです。行わなくてはいけないことをぜひ記入してください'
    current_task = '現在抱えているタスクはこちらです'
    blank = ''
    border = '----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
    introduction = '・タスクを登録する際は1を押してください\n・タスクを編集する際は2を押してください\n・タスクを削除する際は3を押してください\n・アプリを終了する際はqを押してください'
    task_create = 'タスクを登録します'

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

    # Task削除処理
    def Delete_task():
        task_document.blank()
        print('Taskを削除します')   
        input_task_del_number = input('削除したいTaskの番号を入力してください')
        if task_document.cheak_input_blenk(input_task_del_number):
            print('**********空白では登録できません********************入力をやり直してください**********')
            print('削除を中止します')
            return False
        else:
            input_task_del = task_document.input_type_change_int(input_task_del_number)
            delete_task_db(input_task_del)
            print('削除に成功しました！')
            return True

    # Task編集処理
    def Edit_task():
        print(blank)
        print('Task内容を変更します。')
        input_task_edit_number = input('変更したいTaskの番号を入力してください')
        if task_document.cheak_input_blenk(input_task_del_number):
             print('**********空白では登録できません********************入力をやり直してください**********')
            print('削除を中止します')
            return False
        else:
            edit_search_task = edit_search_task_db
            print(edit_search_task)
            # print(f'登録する内容は「{input_task}」でお間違え無いですか？')
            # input_yours_edit_select = input('間違いなければyを入力してください')
            # if input_yours_edit_select == 'y':
            #     edit_task = input('変更内容を教えてください')
            #     print('Task内容を変更します')
            #     edit_task_db(edit_task,input_task_edit)
                        