import unittest

from textnode import TextNode, textnode_to_htmlnode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text MODE", "bold")
        self.assertNotEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_type_url_not_eq(self):
        node = TextNode("This is a text node", "bold", "http://test.com")
        node2 = TextNode("This is a text node", "normal", "http://test.com")
        self.assertNotEqual(node, node2)

    def test_html_conversion_eq(self):
        node = TextNode("HTML Conversion String", 'text')
        node = textnode_to_htmlnode(node)
        node2 = TextNode("HTML Conversion String", 'text')
        node2 = textnode_to_htmlnode(node2)
        self.assertEqual(node, node2)
    
    def test_html_conversion_not_eq(self):
        node = TextNode("HTML Conversion String", 'bold')
        node = textnode_to_htmlnode(node)
        node2 = TextNode("HTML Conversion String", 'text')
        node2 = textnode_to_htmlnode(node2)
        self.assertNotEqual(node, node2)

    def test_html_conversion_link(self):
        node = TextNode("Link zu Boot", 'link', 'http://www.boot.dev/')
        node = textnode_to_htmlnode(node)
        self.assertEqual(node.to_html(), '<a href="http://www.boot.dev/">Link zu Boot</a>')

    def test_html_conversion_image(self):
        node = TextNode("Alt Text", 'image', 'dir/image.jpg')
        node = textnode_to_htmlnode(node)
        self.assertEqual(node.to_html(), '<img src="dir/image.jpg" alt="Alt Text"></img>')



if __name__ == "__main__":
    unittest.main()