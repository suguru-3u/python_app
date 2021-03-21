"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
<Read me>
このファイルはTaskアプリの登録、削除、編集に関する処理が書かれています。
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from sql import task_db
from function import task_app_function

class task_document:

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
        task_app_function.blank()
        input_task = input('登録したいTaskを入力してください')
        task_app_function.blank()
        if task_document.cheak_input_blenk(input_task):
                print('**********空白では登録できません********************入力をやり直してください**********')
                print('登録を中止します')
                return False
        else:
            print(f'登録する内容は「{input_task}」でお間違え無いですか？')
            your_select = input('お間違いなければ「y」を入力してください')
            if your_select == 'y':
                print('登録を開始します')
                task_db.create_task_db(input_task)
                print('登録が成功しました')
                return True
            else:
                return False

    # Task削除処理
    def Delete_task():
        task_app_function.blank()
        print('Taskを削除します')   
        input_task_del_number = input('削除したいTaskの番号を入力してください')
        if task_document.cheak_input_blenk(input_task_del_number):
            print('**********空白では登録できません********************入力をやり直してください**********')
            print('削除を中止します')
            return False
        else:
            input_task_del = task_document.input_type_change_int(input_task_del_number)
            task_db.delete_task_db(input_task_del)
            print('削除に成功しました！')
            return True

    # Task編集処理
    def Edit_task():
        task_app_function.blank()
        print('Task内容を変更します。')
        input_task_edit_number = input('変更したいTaskの番号を入力してください')
        if task_document.cheak_input_blenk(input_task_edit_number):
            print('**********空白では登録できません********************入力をやり直してください**********')
            print('変更を中止します')
            return False
        else:
            input_task_edit = task_document.input_type_change_int(input_task_edit_number)
            result_edit =  task_db.edit_search_task_db(input_task_edit)
            print(f'変更する内容は「{result_edit[0][1]}」でお間違え無いですか？')
            your_select = input('お間違いなければ「y」を入力してください')
            if your_select == 'y':
                edit_task = input('変更内容を入力してください')
                if task_document.cheak_input_blenk(edit_task):
                    print('**********空白では登録できません********************入力をやり直してください**********')
                    print('変更を中止します')
                    return False
                else:
                    print(f'変更する内容は「{edit_task}」でお間違え無いですか？')
                    your_select = input('お間違いなければ「y」を入力してください')
                    if your_select == 'y':
                        print('変更を開始します')
                        task_db.edit_task_db(edit_task,input_task_edit_number)
                        print('変更が成功しました')
                        return True
                    else:
                        return False
            else:
                print('変更を中止します')
                return False