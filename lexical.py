import re
class Lexical:
	def __init__(self,text):
		self.text = text
		self.tokens = []
		self.pos = 0
		self.check = []
	def convert_to_token(self):
		while self.pos < len(self.text):
			if self.text[self.pos] == '\t':
				self.tokens.append('tab')
			elif re.match('\s',self.text[self.pos]):
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
			elif re.match(':',self.text[self.pos]):
				self.tokens.append('colon')
			elif re.match(',',self.text[self.pos]):
				self.tokens.append(',')
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
		tmp = ['if','print','in','range','while',',','else','elif','colon','tab',')','(','True','False','==','=','<','>','<=','>=','for']
		for i in range(len(self.tokens)):
			if self.tokens[i] not in tmp and self.tokens[i] !='num':
				 j = i
				 t = self.tokens[i]
				 if self.tokens.count(self.tokens[i]) >= 2 and re.match('[a-z]',self.tokens[i]) and self.tokens[i-1] != 'if' and self.tokens[i-1] != 'while':
				 	for j in range(len(self.tokens)):
				 		if t == self.tokens[j]:
				 			self.tokens[j] ='var'
				 else:
				 	if self.tokens[i-1] == 'while' or self.tokens[i-1] == 'if':
				 		if self.tokens.count(self.tokens[i]) <= 2:
				 			self.check.append(self.tokens[i])
				 			# print(self.check)		
		for i in range(len(self.tokens)):
			if self.tokens[i] not in tmp:
				if re.match('[0-9]',self.tokens[i]):
					self.tokens[i] = 'num'
				elif i == 0  and re.match('[a-z]',self.tokens[i]):
					self.tokens[i] = 'var'
				elif i > 0 and self.tokens[i] != 'var' and self.tokens[i-1] != 'while' and self.tokens[i-1] != 'for' and self.tokens[i-1] != 'if' and self.tokens[i-1] != 'elif' and self.tokens[i+1] == '=':
					self.tokens[i] = 'var'
				elif i > 0 and self.tokens[i-1] == 'for':
					self.tokens[i] = 'var'

				

	def getTokens(self):
		self.ConvertToPro()
		return self.tokens
	def getCheck(self):
		# print(self.check)
		return self.check
# s = ""
# f = open('input','r')
# for i in f:
# 	s += i.rstrip('\n')
# l = Lexical(s)
# l.convert_to_token()
# c = l.getTokens()
# f.close()
# print("lexical")