import unittest
from proxyjs.proxy import *

class TestBasics(unittest.TestCase):
	def test_request(self):
		r = Request()