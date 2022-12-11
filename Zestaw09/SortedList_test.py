# Marlena Gryt
# Python 2022/2023
# Zd 9.4
# Lista powiazana podwojnie - posortowana

from SortedList import *
import unittest

class TestSortedList(unittest.TestCase):

    def setUp(self): 
        self.list1 = SortedList()
        self.list1.insert(Node(4)) 
        self.list1.insert(Node(2))
        self.list1.insert(Node(1))
        self.list2 = SortedList()
        self.list3 = SortedList()
        self.list3.insert(Node(0)) 
        self.list3.insert(Node(3))

    def test_is_empty(self):
        self.assertEqual(self.list1.is_empty(), False)    
        self.assertEqual(self.list2.is_empty(), True)
        self.assertEqual(self.list3.is_empty(), False)    

    def test_clear(self):
        self.assertEqual(self.list1.clear(), None)
        self.assertEqual(self.list2.clear(), None)    
        self.assertEqual(self.list3.clear(), None)
        
    def test_insert(self):
        self.list1.insert(Node(0))
        self.assertEqual(self.list1.data_list(), [4, 2, 1, 0])  
        self.list1.insert(Node(5))
        self.assertEqual(self.list1.data_list(), [5, 4, 2, 1, 0])   
        self.list1.insert(Node(3))
        self.assertEqual(self.list1.data_list(), [5, 4, 3, 2, 1, 0]) 
       
    def test_remove(self): 
        self.assertEqual(self.list1.remove().data, 4) 
        self.assertEqual(self.list1.data_list(), [2, 1]) 
        self.assertEqual(self.list1.remove().data, 2) 
        self.assertEqual(self.list1.data_list(), [1])  
        self.assertEqual(self.list1.remove().data, 1) 
        self.assertEqual(self.list1.data_list(), []) 
        with self.assertRaises(ValueError):
            self.list1.remove()

    def test_merge(self):
        self.assertEqual(self.list1.merge(self.list2).data_list(), [4, 2, 1]) 
        self.assertEqual(self.list1.merge(self.list3).data_list(), [4, 3, 2, 1, 0]) 

if __name__ == '__main__':
    unittest.main()    




# [Running] python -u "c:\Users\PC\Desktop\Python\SortedList_test.py"
# .....
# ----------------------------------------------------------------------
# Ran 5 tests in 0.000s

# OK

# [Done] exited with code=0 in 0.116 seconds