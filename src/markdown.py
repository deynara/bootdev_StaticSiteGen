import re
from textnode import TextType, TextNode
from debughelper import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.type != TextType.TEXT:
            new_nodes.append(node)
        else:
            if node.text.count(delimiter) % 2 != 0: #% = modulo
                raise Exception (f"Invalid Markdown syntax. Node text |{node.text}| contains unmatched delimeter |{delimiter}|")
            split_list = node.text.split(delimiter)
            split_nodes = []
            for i in range(0, len(split_list)):
                if split_list[i] == "":
                    continue
                if i % 2 == 0:
                    part_node = TextNode(split_list[i], TextType.TEXT)
                else:
                    part_node = TextNode(split_list[i], text_type)
                split_nodes.append(part_node)
            new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def split_nodes_link(old_nodes, image = False):
    #print ("Starting to split nodes\n", debug_pretty_print_list(old_nodes), "\n")
    new_nodes = []
    if image:
        mode = TextType.IMAGE
    else:
        mode = TextType.LINK

    for node in old_nodes:
        if node.type != TextType.TEXT:
            new_nodes.append(node)
        else:
            if image:
                matches = extract_markdown_images(node.text)
            else:
                matches = extract_markdown_links(node.text)

            if matches == []:
                #no link in this text
                new_nodes.append(node)
            else:
                remainder = node.text
                split_list = []
                for entry in matches:
                    text = entry[0]
                    url = entry[1]
                    if image:
                        delimiter = f"![{text}]({url})"
                    else:
                        delimiter = f"[{text}]({url})"
                    #print(entry, text, url, delimiter)
                    parts = remainder.split(delimiter, 1)
                    #debug_pretty_print_list(parts, "parts")
                    if parts[0] != "":
                        split_list.append(TextNode(parts[0], TextType.TEXT))
                    split_list.append(TextNode(text, mode, url))
                    remainder = parts[1]
                if remainder != "":
                    split_list.append(TextNode(remainder, TextType.TEXT))
                new_nodes.extend(split_list)
    return new_nodes

def split_nodes_image(old_nodes):
    return split_nodes_link(old_nodes, True)

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    #debug_pretty_print_list(nodes, "origin")
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    #debug_pretty_print_list(nodes, "splitup")
    return nodes