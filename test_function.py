"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
<Read me>
このファイルはTestに関する処理が書かれています。
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import unittest
import function
import sql
import os
from task_design_document import task_document
from sql import task_db

class TestCalc(unittest.TestCase):

  border = '------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
  blank = ''

  def setUpClass():
      print('*** 全体前処理 ***')
 
  def setUp(self):
      print('+ テスト前処理')

  def tearDown(self):
      print('+ テスト後処理')

  def tearDownClass():
      print('*** 全体後処理 ***')
      os.system('mysql.server stop')
      print('Mysql停止')


  # 単体テスト
  # def test_Create_task_1(self):
  #   print(TestCalc.blank)
  #   print('test_Create_taskのテスト開始')
  #   print('案内通りにTaskを入力してください')
  #   self.assertEqual(True, task_db.task_document.Create_task())   
  #   print('test_Create_taskのテスト終了')
  #   print(TestCalc.blank)
  
  # def test_Create_task_2(self):
  #   print(TestCalc.blank)
  #   print('test_Create_taskのテスト開始')
  #   print('Taskを空白で入力してください')
  #   self.assertEqual(False, task_db.task_document.Create_task())   
  #   print('test_Create_taskのテスト終了')
      # print(TestCalc.blank)


  # def test_Create_task_3(self):
  #   print(TestCalc.blank)
  #   print('test_Create_taskのテスト開始')
  #   print('入力確認で[y]以外を入力してください')
  #   self.assertEqual(False, task_db.task_document.Create_task())   
  #   print('test_Create_taskのテスト終了')
  #   print(TestCalc.blank)


  def test_Delete_task_1(self):
    sql.create_demo_task_db()
    print(TestCalc.border)
    sql.get_tasks()
    print(TestCalc.border)
    print(TestCalc.blank)
    print('test_Delete_task_1のテスト開始')
    self.assertEqual(True, task_db.task_document.Delete_task())   
    print('test_Delete_task_1のテスト終了')
    print(TestCalc.blank)

  def test_Delete_task_2(self):
    print(TestCalc.blank)
    print('test_Delete_task_2のテスト開始')
    self.assertEqual(False, task_db.task_document.Delete_task())   
    print('test_Delete_task_2のテスト終了')
    print(TestCalc.blank)

  
if __name__ == '__main__':
    unittest.main()