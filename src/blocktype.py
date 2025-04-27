from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(md):
    # Strip leading/trailing whitespace for the block
    md_stripped = md.strip()

    # Handle headings
    if md_stripped.startswith("#"):
        count = 0
        for char in md_stripped:
            if char == "#":
                count += 1
            else:
                break
        if 1 <= count <= 6 and md_stripped[count] == " ":
            return BlockType.HEADING

    # Handle code blocks
    elif md_stripped.startswith("```") and md_stripped.endswith("```"):
        return BlockType.CODE

    # Split into lines and check for other block types
    lines = md_stripped.split("\n")

    # Check for quotes
    if all(line.strip().startswith(">") for line in lines if line.strip()):
        return BlockType.QUOTE

    # Check for unordered lists - any line that isn't empty should start with "- "
    if lines and lines[0].strip().startswith("- "):
        if all(line.strip().startswith("- ") or line.strip() == "" for line in lines):
            return BlockType.UNORDERED_LIST

    # Check for ordered lists - any non-empty line should start with a digit followed by period and space
    if (
        lines
        and lines[0].strip()
        and lines[0].strip()[0].isdigit()
        and ". " in lines[0].strip()
    ):
        # Check if all non-empty lines follow the pattern: digit(s) + period + space
        if all(
            (
                line.strip() == ""
                or (
                    len(line.strip()) > 0
                    and line.strip()[0].isdigit()
                    and ". " in line.strip()
                )
            )
            for line in lines
        ):
            return BlockType.ORDERED_LIST

    # Default to paragraph
    return BlockType.PARAGRAPH
