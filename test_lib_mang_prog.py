#!/usr/bin/python3 

import unittest
from  library_mang_sys import User_login,shelf,software

class TestingSoftware(unittest.TestCase):
    def test_borrow(self):
        self.assertTrue(software.borrow_book(('Harry Potter')))
        self.assertFalse(software.borrow_book('Animal Stories'))
        self.assertRaises(KeyError,software.borrow_book,'Test Book')
    def test_return(self):
        borrowed='Animal Stories'
        self.assertRaises(TypeError , software.return_book , 'Harry Potter')
        self.assertTrue(software.return_book((borrowed)))
        self.assertTrue(software.return_book(('Test Book')))
    def test_reserve(self):
        self.assertRaises(KeyError , software.borrow_book ,'Harry Potter')
        self.assertFalse(software.borrow_book('Animal Stories'))
        self.assertRaises(KeyError , software.borrow_book , 'Test Book')

    def test_remove_book(self):
        self.assertRaises(KeyError, shelf.remove_book,'Any Book' )
        self.assertTrue(shelf.remove_book('Harry Potter'))


if __name__ == '__main__':
    unittest.main()
