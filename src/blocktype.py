from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(md):
    if md.startswith("#"):
        count = 0
        for char in md:
            if char == "#":
                count += 1
            else:
                break
        if 1 <= count <= 6 and md[count] == " ":
            return BlockType.HEADING
    elif md.startswith("```") and md.endswith("```"):
        return BlockType.CODE
    elif md.startswith(">"):
        lines = md.split("\n")
        all_lines_are_quotes = all(line.startswith(">") for line in lines)
        if all_lines_are_quotes:
            return BlockType.QUOTE
    elif md.startswith("- "):
        lines = md.split("\n")
        all_lines_are_quotes = all(line.startswith("- ") for line in lines)
        if all_lines_are_quotes:
            return BlockType.UNORDERED_LIST
    elif md.startswith("1. "):
        lines = md.split("\n")
        is_ordered_list = True
        for i, line in enumerate(lines):
            expected_start = f"{i+1}. "
            if not line.startswith(expected_start):
                is_ordered_list = False
                break
        if is_ordered_list:
            return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
