def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    #debug_pretty_print_list(blocks)
    blocks = [block.strip() for block in blocks]
    while "" in blocks:
        blocks.remove("")
    
    #debug_pretty_print_list(blocks)
    return blocks