# -*- coding: UTF-8 -*-
import unittest
from sparking import Sparking

class mytest(unittest.TestCase):
  ##初始化工作
  def setUp(self):
    pass
  #退出清理工作
  def tearDown(self):
    pass
  #具体的测试用例，一定要以test开头
  def testsum(self):
    self.assertEqual(Sparking.get_num_of_one(8,5), 2, 'test sum fail')


if __name__ =='__main__':
  unittest.main()