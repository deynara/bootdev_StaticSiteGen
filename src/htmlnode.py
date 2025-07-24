class HTMLNode:
    def __init__(self, tag=None , value=None, child=None, props=None):
        self.tag = tag
        self.value = value
        self.children = child
        self.props = props
    
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, props: {self.props})"
    
    def props_to_html(self):
        if self.props is None:
            return ""
        Dic = self.props
        DicString = ""
        quote = '"'
        for key in Dic:
            DicString += f" {key}: {quote}{Dic[key]}{quote}"
        return DicString