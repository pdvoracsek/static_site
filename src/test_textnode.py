import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a test node", TextType.ITALIC, "http://example.com")
        node2 = TextNode("This is a Test node", TextType.ITALIC, "http://example.com")
        self.assertNotEqual(node, node2)

    def test_eq_w_url(self):
        node = TextNode("Testing 123", TextType.LINK, "http://testing123.com")
        node2 = TextNode("Testing 123", TextType.LINK, "http://testing123.com")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
