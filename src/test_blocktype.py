import unittest
from blocktype import block_to_block_type, BlockType


class TestBlockType(unittest.TestCase):

    def test_paragraph(self):
        paragraph = "This is a simple paragraph with text."
        type_of_block = block_to_block_type(paragraph)
        self.assertEqual(type_of_block, BlockType.PARAGRAPH)

    def test_heading(self):
        heading = "# Heading Level 1"
        type_of_block = block_to_block_type(heading)
        self.assertEqual(type_of_block, BlockType.HEADING)

    def test_code(self):
        code = "```\ndef hello():\n    return 'world'\n```"
        type_of_block = block_to_block_type(code)
        self.assertEqual(type_of_block, BlockType.CODE)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
