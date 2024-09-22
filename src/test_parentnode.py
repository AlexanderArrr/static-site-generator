import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        child_node = LeafNode("Child string")
        node = ParentNode(child_node)
        node2 = ParentNode(child_node)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        child_node = LeafNode("Child string")
        node = ParentNode(child_node, tag="p")
        node2 = ParentNode(child_node, tag="a")
        self.assertNotEqual(node, node2)


    def test_to_html(self):
        child_node = LeafNode("Child string")
        node = ParentNode(child_node, tag='a', props={"href": "http://test.com",})

        test_str = node.to_html()
        self.assertEqual(test_str, f'<a href="http://test.com">Child string</a>')

#    def test_to_html_no_tag(self):
#        child_node = LeafNode("Child string")
#        node = ParentNode(child_node)
#        test_str = node.to_html()
#        self.assertEqual(test_str, f'Child string')   

    def test_to_html_no_props(self):
        child_node = LeafNode("Child string")
        node = ParentNode(child_node, tag='p')     
        test_str = node.to_html()
        self.assertEqual(test_str, f'<p>Child string</p>')


if __name__ == "__main__":
    unittest.main()