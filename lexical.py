import re
class Lexical:
	def __init__(self,text):
		self.text = text
		self.tokens = []
		self.pos = 0
	def convert_to_token(self):
		while self.pos < len(self.text):
			if re.match('\s',self.text[self.pos]):
				pass
			elif re.match('[a-z]',self.text[self.pos]):
				self.String()
			elif re.match('[0-9]',self.text[self.pos]):
				self.Number()
			elif re.match('\(',self.text[self.pos]) or re.match('\)',self.text[self.pos]):
				self.tokens.append(self.text[self.pos])
			elif re.match('=',self.text[self.pos]) or re.match('<',self.text[self.pos]) or re.match('>',self.text[self.pos]):
				self.Compare()
			elif re.match('\*',self.text[self.pos]) or re.match('\-',self.text[self.pos]) or re.match('\+',self.text[self.pos]) or re.match('\/',self.text[self.pos]):
				self.tokens.append(self.text[self.pos])
			elif re.match('\t',self.text[self.pos]):
				self.tokens.append('tab')
			elif re.match(':',self.text[self.pos]):
				self.tokens.append('colon')
			self.pos += 1
			
	def String(self):
		i = self.pos
		tmp = ""
		while i < len(self.text):
			if re.match('[a-z]|[0-9]',self.text[i]):
				tmp += self.text[i]
				self.pos += 1
			if i == len(self.text) - 1:
				self.tokens.append(tmp)
				self.pos -= 1
				break
			if not re.match('[a-z]|[0-9]',self.text[i]):
				self.tokens.append(tmp)
				self.pos -= 1
				break
			i += 1
	def Number(self):
		i = self.pos
		tmp = ""
		while i < len(self.text):
			if re.match('[0-9]',self.text[i]):
				tmp += self.text[i]
				self.pos += 1
			if i == len(self.text) - 1:
				self.tokens.append(tmp)
				self.pos -= 1
				break
			if not re.match('[0-9]',self.text[i]):
				self.tokens.append(tmp)
				self.pos -= 1
				break
			i += 1
	def Compare(self):
		i = self.pos
		tmp = self.text[i]
		if re.match('=',self.text[i+1]):
			tmp += self.text[i+1]
			self.pos += 1
			self.tokens.append(tmp)
		else:
			self.tokens.append(self.text[i])
	def ConvertToPro(self):
		pass

	def getTokens(self):
		return self.tokens
l = Lexical("	")
l.convert_to_token()
print(l.getTokens())