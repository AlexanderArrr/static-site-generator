import unittest
from markdown_blocks import (markdown_to_blocks,
                             block_to_block_type,
                             block_type_code,
                             block_type_heading,
                             block_type_ordered_list,
                             block_type_paragraph,
                             block_type_quote,
                             block_type_unordered_list
                            )
from markdown_html import(markdown_to_html_node)


class TestMarkdownToHTML(unittest.TestCase):

    # TESTS FOR markdown_to_block

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
    
    # -------------------------------------------------
    # TESTS FOR block_to_block_type

    def test_headings_block_type(self):
        md = "# This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, block_type_heading)
    
    def test_3_headings_block_type(self):
        md = "### This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, block_type_heading)

    def test_6_headings_block_type(self):
        md = "###### This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, block_type_heading)
    
    def test_7_headings_block_type(self):
        md = "####### This is not a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, block_type_paragraph)

    def test_code_block_type(self):
        md = "```This is\na\ncode block```"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, block_type_code)

    def test_not_code_block_type(self):
        md = "```This is not\na code block``"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, block_type_paragraph)
    
    def test_quote_block_type(self):
        md = "> This is a\n> quote block\n> with 3 lines"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, block_type_quote)

    def test_not_quote_block_type(self):
        md = ">This is not\n> a correct\nquote block"
        self.assertEqual(block_to_block_type(md), block_type_paragraph)

    def test_unordered_list_block_type(self):
        md = md = "* This is\n* an\n* unordered list\n* with 4 entries"
        md2 = "* This is\n* an unordered list"
        md3 = "- This is\n- an unordered\n- list"
        self.assertEqual(block_to_block_type(md), block_type_unordered_list)
        self.assertEqual(block_to_block_type(md2), block_type_unordered_list)
        self.assertEqual(block_to_block_type(md3), block_type_unordered_list)

    def test_not_unordered_list_block_type(self):
        md = "* This is\nnot\n* an unordered list\n* with 3 entries"
        md2 = "* This is\n* not\nan unordered list"
        self.assertEqual(block_to_block_type(md), block_type_paragraph)
        self.assertEqual(block_to_block_type(md2), block_type_paragraph)

    def test_ordered_list_block_type(self):
        md = "1. This is\n2. an ordered\n3. list"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, block_type_ordered_list)

    def test_not_ordered_list_block_type(self):
        md = "1. This is\n2. not\nan ordered list"
        md2 = "1. This is\nn2.not\n3. an ordered list"
        self.assertEqual(block_to_block_type(md), block_type_paragraph)
        self.assertEqual(block_to_block_type(md2), block_type_paragraph)

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.maxDiff = None
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


if __name__ == "__main__":
    unittest.main()
