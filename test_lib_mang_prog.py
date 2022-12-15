#!/usr/bin/python3 

import unittest
from  library_mang_sys import User_login,shelf,software

class TestingSoftware(unittest.TestCase):
    def test_borrow(self):
        self.assertTrue(software.borrow_book(('Harry Potter')))
        self.assertFalse(software.borrow_book('Animal Stories'))
        self.assertRaises(KeyError,software.borrow_book,'Test Book')
    def test_return(self):
        r1 = software.return_book(('Animal Stories'))
        self.assertRaises(KeyError , software.return_book , 'Harry Potter')
        self.assertEqual(r1 , True)
        self.assertRaises(KeyError , software.return_book, 'Test Book')
    def test_reserve(self):
        self.assertRaises(KeyError , software.borrow_book ,'Harry Potter')
        self.assertFalse(software.borrow_book('Animal Stories'))
        self.assertRaises(KeyError , software.borrow_book , 'Test Book')

    def test_remove_book(self):
        self.assertRaises(KeyError, shelf.remove_book,'Any Book' )
        self.assertTrue(shelf.remove_book('Harry Potter'))
    
    def test_get_book_count(self):
        r1 = shelf.get_book_count('Fiction' , '1')
        r2 = shelf.get_book_count('Motivation', '1')
        r3 = shelf.get_book_count(None, '2')
        r4 = shelf.get_book_count('Erotica' , '1')
        self.assertEqual(r1 , 2)
        self.assertEqual(r2 , 1)
        self.assertEqual(r4, 0)
        self.assertEqual(r3, 4)
    def test_populate_book(self):
        self.assertRaises(FileNotFoundError ,  shelf.populate_book , 'Any_random.xlsx')


if __name__ == '__main__':
    unittest.main()
