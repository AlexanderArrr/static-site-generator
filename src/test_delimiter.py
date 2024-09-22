import unittest

from textnode import TextNode, textnode_to_htmlnode
from delimiter import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq_0(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], '`', 'code')
        node_0 = TextNode("This is text with a ", "text")
        self.assertEqual(new_nodes[0], node_0)
    
    def test_eq_1(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], '`', 'code')
        node_1 = TextNode("code block", "code")
        self.assertEqual(new_nodes[1], node_1)

    def test_eq_2(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], '`', 'code')
        node_2 = TextNode(" word", "text")
        self.assertEqual(new_nodes[2], node_2)

    def test_multiple_bolds(self):
        node = TextNode("This is **a text** with **bold words**", "text")
        new_nodes = split_nodes_delimiter([node], '**', 'bold')
        node_3 = TextNode("bold words", 'bold')
        self.assertEqual(new_nodes[3], node_3)

    def test_italic(self):
        node = TextNode("This is a text with *italic* words", 'text')
        new_nodes = split_nodes_delimiter([node], '*', 'italic')
        node_1 = TextNode('italic','italic')
        self.assertEqual(new_nodes[1], node_1)

#    def test_missing_closing_delimiter(self):
#        node = TextNode("This is text with a `code block word", "text")
#        self.assertRaises(BaseException, split_nodes_delimiter([node], '`', 'code'))

if __name__ == "__main__":
    unittest.main()