import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(value="Test text")
        node2 = HTMLNode(value="Test text")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode(tag="p", value="test")
        node2 = HTMLNode(tag="a", value="test")
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(tag='p', value='test', props={"href": "http://test.com",})
        print(node.props)
        test_str = node.props_to_html()
        self.assertEqual(test_str, f' href="http://test.com"')


if __name__ == "__main__":
    unittest.main()