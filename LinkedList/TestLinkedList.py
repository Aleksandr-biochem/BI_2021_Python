import unittest
from LinkedList import LinkedList, LinkedListItem


# Test cases to test LinkedList methods
class TestLinkedList(unittest.TestCase):

    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.linkedlist = LinkedList()

    # Each test method starts with the keyword test_
    def test_add_and_get_item(self):  # test adding and geting number at different positions
        self.assertEqual(len(self.linkedlist), 0)
        self.linkedlist.add(4)
        self.assertEqual(len(self.linkedlist), 1)
        self.linkedlist.add(6)
        self.assertEqual(len(self.linkedlist), 2)
        self.assertEqual([self.linkedlist[0], self.linkedlist[1]], [4, 6])
        self.linkedlist.add(5, 0)
        self.assertEqual(len(self.linkedlist), 3)
        self.assertEqual([self.linkedlist[0], self.linkedlist[1]], [5, 4])
        self.linkedlist.add(7, 1)
        self.assertEqual(len(self.linkedlist), 4)
        self.assertEqual([self.linkedlist[0], self.linkedlist[1], self.linkedlist[2]], [5, 7, 4])
        self.linkedlist.add(200)
        self.assertEqual(len(self.linkedlist), 5)
        self.assertEqual([self.linkedlist[3], self.linkedlist[4]], [6, 200])
        with self.assertRaises(IndexError):
            self.linkedlist.add(0, 7)

    def test_extend(self):  # test extending the list
        self.linkedlist.extend([1, 2, 3])
        self.assertEqual(len(self.linkedlist), 3)
        self.assertEqual([self.linkedlist[0], self.linkedlist[1], self.linkedlist[2]], [1, 2, 3])
        self.linkedlist.extend([7, 8], 1)
        self.assertEqual(len(self.linkedlist), 5)
        self.assertEqual([self.linkedlist[0], self.linkedlist[1], self.linkedlist[2],
                          self.linkedlist[3], self.linkedlist[4]], [1, 7, 8, 2, 3])
        self.linkedlist.extend([9, 10], 0)
        self.assertEqual(len(self.linkedlist), 7)
        self.assertEqual([self.linkedlist[0], self.linkedlist[1], self.linkedlist[2],
                          self.linkedlist[3], self.linkedlist[4],
                          self.linkedlist[5], self.linkedlist[6]], [9, 10, 1, 7, 8, 2, 3])
        with self.assertRaises(IndexError):
            self.linkedlist.extend([1, 2], 8)

    def test_length(self):  # test length
        self.assertEqual(len(self.linkedlist), 0)
        self.linkedlist.extend([1, 2, 3, 4, 5])
        self.assertEqual(len(self.linkedlist), 5)

    def test_first_last(self):
        self.linkedlist.extend([1, 2, 3])
        self.assertEqual(self.linkedlist.first(), 1)
        self.assertEqual(self.linkedlist.last(), 3)

    def test_in_search(self):  # test searching value with in
        self.assertFalse(2 in self.linkedlist)
        self.linkedlist.extend([1, 2, 3])
        self.assertTrue(2 in self.linkedlist)
        self.assertFalse(5 in self.linkedlist)

    def test_pop(self):
        self.linkedlist.extend([1, 2, 3, 4, 5])
        self.assertEqual(len(self.linkedlist), 5)
        self.linkedlist.pop()
        self.assertEqual(len(self.linkedlist), 4)
        self.assertEqual([self.linkedlist[0], self.linkedlist[1],
                          self.linkedlist[2], self.linkedlist[3]], [1, 2, 3, 4])
        self.linkedlist.pop(0)
        self.assertEqual(len(self.linkedlist), 3)
        self.assertEqual([self.linkedlist[0], self.linkedlist[1], self.linkedlist[2]], [2, 3, 4])
        self.linkedlist.pop(1)
        self.assertEqual(len(self.linkedlist), 2)
        self.assertEqual([self.linkedlist[0], self.linkedlist[1]], [2, 4])
        self.linkedlist.pop()
        self.linkedlist.pop()
        self.assertEqual(len(self.linkedlist), 0)
        with self.assertRaises(IndexError):
            self.linkedlist.pop()

    def test_remove_last_ccurence(self):
        self.linkedlist.extend([1, 2, 3, 2, 5])
        self.linkedlist.remove_last_occurence(2)
        self.assertEqual(len(self.linkedlist), 4)
        self.assertEqual([self.linkedlist[0], self.linkedlist[1],
                          self.linkedlist[2], self.linkedlist[3]], [1, 2, 3, 5])
        self.linkedlist.remove_last_occurence(7)
        self.assertEqual(len(self.linkedlist), 4)
        self.assertEqual([self.linkedlist[0], self.linkedlist[1],
                          self.linkedlist[2], self.linkedlist[3]], [1, 2, 3, 5])


if __name__ == "__main__":
    unittest.main()
