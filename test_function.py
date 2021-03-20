import unittest
import function

class TestCalc(unittest.TestCase):

  task = ''
  blank_task = ''

  def setUpClass():
      print('*** 全体前処理 ***')
      TestCalc.task = 'お昼を食べる'
      TestCalc.blank_task = ''

  def tearDownClass():
      print('*** 全体後処理 ***')
 
 
  def setUp(self):
      print('+ テスト前処理')
 
 
  def tearDown(self):
      print('+ テスト後処理')

  def test_cheak_input_blenk(self):
    print('test_cheak_input_blenkのテスト開始')
    self.assertEqual(True, function.cheak_input_blenk(TestCalc.blank_task))   
    print('test_cheak_input_blenkのテスト終了')

  def test_cheak_input(self):
    print('test_cheak_input_blenkのテスト開始')
    self.assertEqual(False, function.cheak_input_blenk(TestCalc.task))   
    print('test_cheak_input_blenkのテスト終了')
  
if __name__ == '__main__':
    unittest.main()