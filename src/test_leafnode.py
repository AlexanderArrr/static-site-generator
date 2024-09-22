import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(value="Test text")
        node2 = LeafNode(value="Test text")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = LeafNode(tag="p", value="test")
        node2 = LeafNode(tag="a", value="test")
        self.assertNotEqual(node, node2)


    def test_to_html(self):
        node = LeafNode(tag='a', value='test', props={"href": "http://test.com",})
        test_str = node.to_html()
        print(test_str)
        self.assertEqual(test_str, f'<a href="http://test.com">test</a>')

    def test_to_html_no_tag(self):
        node = LeafNode("Test string")
        test_str = node.to_html()
        self.assertEqual(test_str, f'Test string')   

    def test_to_html_no_props(self):
        node = LeafNode("Test string", tag='p')     
        test_str = node.to_html()
        self.assertEqual(test_str, f'<p>Test string</p>')


if __name__ == "__main__":
    unittest.main()