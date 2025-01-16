from textnode import TextNode
from textnode import TextType

def main():
    node = TextNode("blahblah", TextType.BOLD, "https://example.com")
    print(node)

main()