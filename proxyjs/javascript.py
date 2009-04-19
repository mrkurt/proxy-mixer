import re
import os
import spidermonkey

class Extractor:
	__mixer_js_lib = open(os.path.dirname(__file__) + '/../javascript/mixer.js', 'r').read()
	__js_block = re.compile(r"(<script.+?runat=\"proxy\".*?>)(.*?)(</script>)", re.S)
	__script_start = re.compile(r"<script.+?runat=\"proxy\".*?>")
	__script_src = re.compile(r"src=\"([^\"]+)\"")
	__script_end = "</script>"
	
	def __init__(self, raw):
		self.data = Extractor.__js_block.split(raw)
		
	def js(self):
		js = ''
		js_instances = 0
		in_script = False
		for i, t in enumerate(self.data):
			if t == Extractor.__script_end:
				in_script = False
			elif t.startswith("<script") and Extractor.__script_start.match(t):
				in_script = True
				js_instances += 1
				js += self.__extract_js_includes(t)
			elif in_script:
				js += t + '\n'
			else:
				js += 'Mixer.append_raw_from_array(%s);\n' % i
		js = 'var window = {};\n' + Extractor.__mixer_js_lib + '\n' + js
		js += '\nMixer.output;'
		return js
		
	def __extract_js_includes(self, chunk):
		js = ''
		for s in Extractor.__script_src.findall(chunk):
			js += '// Including: ' + s
		return js

class Runner:
	__runtime = spidermonkey.Runtime()
	__result_handlers = {
		'raw' : lambda c, d : d[c.index],
		'include' : lambda c, d : '<p><strong>Including: %s</strong></p>' % c.src
	}
	
	def __init__(self, raw = None):
		if raw:
			self.__extractor = Extractor(raw)

	def run_js(self, js = None):
		if not js and self.__extractor:
			js = self.__extractor.js()
		ctx = Runner.__runtime.new_context()
		return ctx.execute(js)
		
	def assemble_result(self, raw = None):
		if not self.__extractor and not raw:
			raise Error, "No source to work with"
		elif raw:
			self.__extractor = Extractor(raw)
		
		result = self.run_js()
		data = self.__extractor.data
		output = ''
		
		handlers = Runner.__result_handlers
		
		for i in range(len(result)):
			command = result[i]
			if command:
				output += handlers[command.type](command, data)
		
		return output