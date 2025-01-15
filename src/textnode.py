from enum import Enum

class TextType(Enum):
	NORMAL_TEXT = "normal"
	BOLD_TEXT = "bold"
	ITALIC_TEXT = "italic"
	CODE_TEXT = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode(text, text_type, url):
	self.text = text
	self.text_type = text_type
	self.url = url
