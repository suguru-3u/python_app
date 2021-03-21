"""
このファイルはユーザーが入力したタスクを受け取るようのクラスです。
このクラス自体には受け取るだけの機能しかありませんが敬承を使い機能の拡充を行っております。
"""

class task_design_document:

    task_create = 'タスクを登録します'
    app_self = 'ようこそ！\nこのアプリはTodoアプリです。行わなくてはいけないことをぜひ記入してください'
    current_task = '現在抱えているタスクはこちらです'
    blank = ''
    border = '----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
    introduction = '・タスクを登録する際は1を押してください\n・タスクを編集する際は2を押してください\n・タスクを削除する際は3を押してください\n・アプリを終了する際はqを押してください'
    task_create = 'タスクを登録します'


    # コンストラクト
    def __init__(self,task,number,change_task):
        self.task = task
        self.task_number = number
        self.change_task = change_task


    # Task登録処理
    def Create_task():
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