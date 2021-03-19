import unittest
import function

class TestCalc(unittest.TestCase):
  def test_Create_task(self):
    self.assertEqual('登録したい内容を記入してください！', function.Create_task())   
 
  
if __name__ == '__main__':
    unittest.main()