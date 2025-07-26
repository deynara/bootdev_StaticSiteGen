from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text" #This is a paragraph of text.
    BOLD = "bold" #This is a **bold** word.
    ITALIC = "italic" #This is an _italic_ word.
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.type = text_type
        self.url = url

    def __eq__ (self, other):
        return (self.text == other.text
        and self.type == other.type
        and self.url == self.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.type.value}, {self.url})"

def textnode_to_htmlnode(textnode):
    match textnode.type:
        case TextType.TEXT:
            leaf = LeafNode(None, textnode.text)
        case TextType.BOLD:
            leaf = LeafNode("b", textnode.text)
        case TextType.ITALIC:
            leaf = LeafNode("i", textnode.text)
        case TextType.CODE:
            leaf = LeafNode("code", textnode.text)
        case TextType.LINK:
            leaf = LeafNode("a", textnode.text, {"href": textnode.url})
        case TextType.IMAGE:
            leaf = LeafNode("img", "", {"src": textnode.url, "alt": textnode.text})
        case _:
            raise Exception("Unknown texttype: ", textnode.type)
    return leaf