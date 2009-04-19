import re
import spidermonkey

class Extractor:
	__js_block = re.compile(r"(<script.+?runat=\"proxy\".*?>)(.*?)(</script>)", re.S)
	__script_start = re.compile(r"<script.+?runat=\"proxy\".*?>")
	__script_src = re.compile(r"src=\"([^\"]+)\"")
	__script_end = "</script>"
	
	def __init__(self, raw):
		self.data = Extractor.__js_block.split(raw)
		
	def js(self):
		js = ''
		in_script = False
		for i in range( len ( self.data ) ):
			t = self.data[i]
			if(t == Extractor.__script_end):
				in_script = False
			elif(t.startswith("<script") and Extractor.__script_start.match(t)):
				in_script = True
				js += self.__extract_js_includes(t)
			elif(in_script):
				js += t + '\n'
			else:
				js += 'Mixer.append_raw_from_array(' + str(i) + ');\n'
		return js
		
	def __extract_js_includes(self, chunk):
		js = ''
		for s in Extractor.__script_src.findall(chunk):
			js += '// Including: ' + s
		return js

class Runner:
	__runtime = spidermonkey.Runtime()
	def __init__(self, raw = None):
		if raw:
			self.__extractor = Extractor(raw)

	def run_js(self, js = None):
		if not js and self.__extractor:
			js = self.__extractor.js()
		ctx = Runner.__runtime.new_context()
		return ctx.execute(js)