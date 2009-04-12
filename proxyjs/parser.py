import re

class Parser:
	__js_block = re.compile(r"(<script.+?runat=\"proxy\".*?>)(.*?)(</script>)", re.S)
	__script_start = re.compile(r"<script.+?runat=\"proxy\".*?>")
	__script_src = re.compile(r"src=\"([^\"]+)\"")
	__script_end = "</script>"
	
	def __init__(self, raw):
		self.data = Parser.__js_block.split(raw)
		
	def js(self):
		js = ''
		in_script = False
		for i in range( len ( self.data ) ):
			t = self.data[i]
			if(t == Parser.__script_end):
				in_script = False
			elif(t.startswith("<script") and Parser.__script_start.match(t)):
				in_script = True
				js += self.__extract_js_includes(t)
			elif(in_script):
				js += t + '\n'
			else:
				js += 'Mixer.append_raw_from_array(' + str(i) + ');\n'
		return js
		
	def __extract_js_includes(self, chunk):
		js = ''
		for s in Parser.__script_src.findall(chunk):
			js += '// Including: ' + s
		return js
		
