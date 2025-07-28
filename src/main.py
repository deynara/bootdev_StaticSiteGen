from textnode import TextNode, TextType, textnode_to_htmlnode
from htmlnode import *
from markdown import *
from markdown_blocks import *
from debughelper import *

def main():
    print("Starting main.py")
    md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item

> This is a quote.
> This is also a quote.

```
This is code
```

> This is a single quote.

> That's a different quote.
But this is no quote

# Heading 1

1. Item 1
2. Item 2
3. Item 3

## Heading 2
"""
    blocks = markdown_to_blocks(md)
    #debug_pretty_print_list(blocks, "Blocks")
    for block in blocks:
        typ = block_to_block_type(block)
        print (block, "\n", typ, "\n")
    #print(md)
if __name__ == "__main__":
    main()