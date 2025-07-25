from textnode import TextNode, TextType
from htmlnode import *

def main():
    print("Starting main.py")
    test = HTMLNode(
            "a",
            "It's a link",
            None,
            {
               "href": "https://www.dummyurl.com",
                "target": "_blank",
            })
    
    test_method = test.props_to_html()
    leaf = LeafNode("p", "This is a paragraph of text.")
    parent = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )

    print (parent)
    print(parent.to_html())

if __name__ == "__main__":
    main()