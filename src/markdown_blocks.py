from enum import Enum
import re
from debughelper import debug_pretty_print_list

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE ="code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"
    MULTI = "multi" # 



def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in blocks]
    while "" in blocks:
        blocks.remove("")
    return blocks

def block_to_block_type(block):
    pattern = r"#{1,6} "
    #print("Matchtry Heading", re.match(pattern, block))
    if re.match(pattern, block):
        return BlockType.HEADING
    pattern = r"`{3}"

    if re.match(pattern, block) and re.match(pattern, block[:-2]):
        if len(block) < len("123456"):
            #accidental match, block shorter than a code block can be. Example case block is |'''|
            return BlockType.PARAGRAPH
        return BlockType.CODE

    line_list = [block]
    if "\n" in block:
        line_list = block.split("\n")

    pattern = r">"
    if re.match(pattern, line_list[0]):
        if len(line_list) == 1:
            return BlockType.QUOTE
        return multiline_block(pattern, line_list, BlockType.QUOTE)

    pattern = r"- "
    if re.match(pattern, line_list[0]):
        if len(line_list) == 1:
            return BlockType.ULIST
        return multiline_block(pattern, line_list, BlockType.ULIST)
    
    pattern = r"\d\. "
    if re.match(pattern, line_list[0]):
        if len(line_list) == 1:
            return BlockType.OLIST
        return multiline_block(pattern, line_list, BlockType.OLIST, True)

    return BlockType.PARAGRAPH

def multiline_block(pattern, line_list, typ, check_order_sanity = False):
    if re.match(pattern, line_list[0]):
        all_match = True
        for i in range(0, len(line_list)):
            if re.match(pattern, line_list[i]):
                if check_order_sanity:
                    if str(i+ 1) != line_list[i][0]:
                        all_match = False
                        break
                continue
            else:
                all_match = False
                return BlockType.MULTI
        if all_match:
            if check_order_sanity:
                pass
            return typ
    return

