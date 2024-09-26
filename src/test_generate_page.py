import unittest
from generate_page import (extract_title)


class TestMarkdownToHTML(unittest.TestCase):

    # TESTS FOR markdown_to_block

    def test_md_title_extract(self):
        md = "# This is a h1 title\n\n## This is a h2 title"
        test = extract_title(md)

        self.assertEqual(test, 'This is a h1 title')

    def test_raise_md_title_extract(self):
        md = "## This is a h2 title"
        
        with self.assertRaises(ValueError):
            extract_title(md)
       

if __name__ == "__main__":
    unittest.main()
