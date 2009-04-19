import unittest
import os
import glob
from proxyjs.javascript import *

class TestExtractor(unittest.TestCase):
	fixtures = ''
	def test_simple_string(self):
		raw = "<html>\n<head></head>\n<body>\n<script runat=\"proxy\">Mixer('test.html');</script>\n</body>\n</html>"
		parser = Extractor(raw)
		self.assertEqual(len(parser.data), 5)
		
	def parse_and_compare(self, src, save_result = False):
		raw = open(src, 'r').read()
		target = src + '.parsed.js'
		parser = Extractor(raw)
		
		if save_result:
			open(target, 'w').write(parser.js())
		
		target = open(target, 'r').read()
		
		self.assertEqual(parser.js(), target)

	def test_files(self):
		for f in glob.glob(TestExtractor.fixtures + '*.html'):
			self.parse_and_compare(f)

class TestExecution(unittest.TestCase):
	def test_simple_js(self):
		result = Runner().run_js('"kurt rocks";')
		self.assertEqual(result, 'kurt rocks')
	
	def test_longer_js(self):
		result = Runner().run_js('var blah = "kurt rocks";\nblah;')
		self.assertEqual(result, 'kurt rocks')

	def test_complex_return(self):
		result = Runner().run_js('var complex = { "kurt" : "rocks", "when" : ["mon", "tues", "fri"] };\ncomplex;')
		self.assertEqual(result.kurt, "rocks")
		self.assertEqual(len(result.when), 3)
