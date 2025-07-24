from textnode import TextNode, TextType
from htmlnode import HTMLNode

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
    print (test_method)

if __name__ == "__main__":
    main()