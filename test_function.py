import unittest
import function
import sql
import os
from task_design_document import task_document


class TestCalc(unittest.TestCase):

  border = '------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
  blank = ''

  def setUpClass():
      print('*** 全体前処理 ***')
      print(TestCalc.border)
      sql.get_tasks()
      print(TestCalc.border)
 
  def setUp(self):
      print('+ テスト前処理')

  def tearDown(self):
      print('+ テスト後処理')

  def tearDownClass():
      print('*** 全体後処理 ***')
      sql.delete_like_task_db(TestCalc.task)
      os.system('mysql.server stop')
      print('Mysql停止')


  # 単体テスト
  # def test_Create_task_1(self):
  #   print(TestCalc.blank)
  #   print('test_Create_taskのテスト開始')
  #   print('案内通りにTaskを入力してください')
  #   self.assertEqual(True, task_document.Create_task())   
  #   print('test_Create_taskのテスト終了')
  #   print(TestCalc.blank)
  
  # def test_Create_task_2(self):
  #   print(TestCalc.blank)
  #   print('test_Create_taskのテスト開始')
  #   print('Taskを空白で入力してください')
  #   self.assertEqual(False, task_document.Create_task())   
  #   print('test_Create_taskのテスト終了')
      # print(TestCalc.blank)


  # def test_Create_task_3(self):
  #   print(TestCalc.blank)
  #   print('test_Create_taskのテスト開始')
  #   print('入力確認で[y]以外を入力してください')
  #   self.assertEqual(False, task_document.Create_task())   
  #   print('test_Create_taskのテスト終了')
  #   print(TestCalc.blank)


  def test_Delete_task(self):
    print(TestCalc.blank)
    print('test_cheak_input_blenkのテスト開始')
    self.assertEqual(False, function.Delete_task())   
    print('test_cheak_input_blenkのテスト終了')
    print(TestCalc.blank)

  def test_Delete_task(self):
    print(TestCalc.blank)
    print('test_Delete_taskのテスト開始')
    self.assertEqual(1, function.Delete_task())   
    print('test_Delete_taskのテスト終了')
    print(TestCalc.blank)

  # def test_task_app_end_judgment_2(self):
  #   print('task_app_end_judgmentのテスト開始')
  #   self.assertEqual(2, function.task_app_end_judgment())   
  #   print('task_app_end_judgmentのテスト終了')

  # def test_get_tasks(self):
  #   print('test_get_tasksのテスト開始')
  #   self.assertEqual(True, sql.get_tasks())   
  #   print('test_get_tasksのテスト終了')


  # # # 結合テスト
  # def test_Create_task_1(self):
  #   print('test_Create_taskのテスト開始')
  #   self.assertEqual(True, function.Create_task(TestCalc.task))   
  #   print('test_Create_taskのテスト終了')

  # def test_Create_task_2(self):
  #   print('test_Create_taskのテスト開始')
  #   self.assertEqual(False, function.Create_task(TestCalc.task))   
  #   print('test_Create_taskのテスト終了')

  # # # 結合テスト
  # def test_Edit_task_1(self):
  #   print('test_Create_taskのテスト開始')
  #   self.assertEqual(True, function.Create_task(TestCalc.task))   
  #   print('test_Create_taskのテスト終了')

  # def test_Edit_task_2(self):
  #   print('test_Create_taskのテスト開始')
  #   self.assertEqual(False, function.Create_task(TestCalc.task))   
  #   print('test_Create_taskのテスト終了')

  
if __name__ == '__main__':
    unittest.main()