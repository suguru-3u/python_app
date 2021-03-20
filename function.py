"""
    このファイルはTodoアプリの登録,編集、削除機能について書いてあるファイルです。
    各機能はMysqlと接続するためにsqlファイルのメソッドをimportしている。
"""

from sql import create_task_db
from sql import delete_task_db
from sql import edit_task_db


# 説明文
app_self = 'ようこそ！\nこのアプリはTodoアプリです。行わなくてはいけないことをぜひ記入してください'
current_task = '現在抱えているタスクはこちらです'
blank = ''
border = '-----------------------------------------------------------------------------------------'
introduction = '・タスクを登録する際は1を押してください\n・タスクを編集する際は2を押してください\n・タスクを削除する際は3を押してください\n・アプリを終了する際はqを押してください'
task_create = 'タスクを登録します'

# Cheak input blenk
def cheak_input_blenk(task_string):
    if not task_string:
        print('**********空白では登録できません**********\n**********入力をやり直してください**********')
        return True
    else:
        return False

# Create task
def Create_task(task_string):
    print(blank)
    print(task_create)
    print(f'登録する内容は「{task_string}」でお間違え無いですか？')
    yours_select = input('お間違いなければ「y」を入力してください')
    if yours_select == 'y':
        print('登録を開始します')
        create_task = create_task_db(task_string)
        return True
    else:
        print('登録を中止します')
        return False

# Edit task
def Edit_task():
    print(blank)
    print('Task内容を変更します。')
    try:
        input_task_edit = input('変更したいTaskの番号を入力してください')
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
            edit_task_db(edit_task,input_task_edit)

# Delte task
def Delete_task():
    print(blank)
    print('Taskを削除します')   
    input_task_del = input('削除したいTaskの番号を入力してください')
    input_task_del = input_type_change_int(input_task_del)
    delete_task_db(input_task_del)
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