import unittest
import function
import sql
import os

class TestCalc(unittest.TestCase):

  task = ''
  blank_task = ''

  def setUpClass():
      print('*** 全体前処理 ***')
      TestCalc.task = 'お昼を食べる'
      TestCalc.blank_task = ''
      sql.get_tasks()
 
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
  def test_cheak_input_blenk(self):
    print('test_cheak_input_blenkのテスト開始')
    self.assertEqual(True, function.cheak_input_blenk(TestCalc.blank_task))   
    print('test_cheak_input_blenkのテスト終了')

  def test_cheak_input(self):
    print('test_cheak_input_blenkのテスト開始')
    self.assertEqual(False, function.cheak_input_blenk(TestCalc.task))   
    print('test_cheak_input_blenkのテスト終了')

  def test_task_app_end_judgment_1(self):
    print('task_app_end_judgmentのテスト開始')
    self.assertEqual(1, function.task_app_end_judgment())   
    print('task_app_end_judgmentのテスト終了')

  def test_task_app_end_judgment_2(self):
    print('task_app_end_judgmentのテスト開始')
    self.assertEqual(2, function.task_app_end_judgment())   
    print('task_app_end_judgmentのテスト終了')

  def test_get_tasks(self):
    print('test_get_tasksのテスト開始')
    self.assertEqual(True, sql.get_tasks())   
    print('test_get_tasksのテスト終了')


  # # 結合テスト
  def test_Create_task_1(self):
    print('test_Create_taskのテスト開始')
    self.assertEqual(True, function.Create_task(TestCalc.task))   
    print('test_Create_taskのテスト終了')

  def test_Create_task_2(self):
    print('test_Create_taskのテスト開始')
    self.assertEqual(False, function.Create_task(TestCalc.task))   
    print('test_Create_taskのテスト終了')

  # # 結合テスト
  def test_Edit_task_1(self):
    print('test_Create_taskのテスト開始')
    self.assertEqual(True, function.Create_task(TestCalc.task))   
    print('test_Create_taskのテスト終了')

  def test_Edit_task_2(self):
    print('test_Create_taskのテスト開始')
    self.assertEqual(False, function.Create_task(TestCalc.task))   
    print('test_Create_taskのテスト終了')

  
if __name__ == '__main__':
    unittest.main()