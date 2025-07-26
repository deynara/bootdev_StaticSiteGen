from textnode import TextNode, TextType, textnode_to_htmlnode
from htmlnode import *
from markdown import *
from debughelper import *

def main():
    print("Starting main.py")
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line




- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    debug_pretty_print_list(blocks, "Blocks")
    #print(md)
if __name__ == "__main__":
    main()