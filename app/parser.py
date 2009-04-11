import re

class Parser:
	__js_block = re.compile(r"(<script.+?runat=\"proxy\".*?>)(.*?)(</script>)")
	__script_start = re.compile(r"<script.+?runat=\"proxy\".*?>")
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
			elif(in_script):
				js += t + '\n'
			else:
				js += 'Mixer.append_raw_from_array(' + str(i) + ');\n'
		return js
			
parsed = Parser("<html>\n<head></head>\n<body>\n<script runat=\"proxy\">Mixer('test.html');</script>\n</body>\n</html>")
print parsed.js()
print parsed.data