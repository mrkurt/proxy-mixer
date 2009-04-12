import unittest
import os
from proxyjs.parser import *

class TestParser(unittest.TestCase):
	fixtures = ''
	def test_simple_string(self):
		raw = "<html>\n<head></head>\n<body>\n<script runat=\"proxy\">Mixer('test.html');</script>\n</body>\n</html>"
		parser = Parser(raw)
		self.assertEqual(len(parser.data), 5)
		
	def test_files(self):
		raw = open(TestParser.fixtures + 'page.html', 'r').read()
		parser = Parser(raw)
		
		#target = open(TestParser.fixtures + 'page.html.parsed.js', 'w').write(parser.js())
		print parser.js()