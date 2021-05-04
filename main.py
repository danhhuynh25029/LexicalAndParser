import nltk
from lexical import *
from nltk.parse.chart import ChartParser,BU_LC_STRATEGY
grammar1 = nltk.CFG.fromstring("""
  program -> exp_stmt | for_stmt | while_stmt | if_stmt | print_stmt | input_stmt | assign
  assign -> indentifer '=' exp_stmt | indentifer '=' number | indentifer '=' content
  print_stmt -> 'print' '(' content ')'
  input_stmt -> 'input' '(' content ')'
  exp_stmt -> number '*' number | number '-' number | number '+' number | number '/' number
  for_stmt -> 'for' indentifer 'in' 'range' value 'colon' 'tab' block
  while_stmt -> 'while' exp 'colon' 'tab' block
  if_stmt -> 'if' exp 'colon' 'tab' block | 'if' exp 'colon' 'tab' block elif_stmt|'if' exp 'colon' 'tab' block else_block
  else_block -> 'else' 'colon' 'tab' block | if_stmt
  elif_stmt -> 'elif' exp 'colon' 'tab' block elif_stmt|if_stmt
  exp -> 'True'|'False'|indentifer compare indentifer|indentifer compare number
  block -> if_stmt|print_stmt|'tab' block
  indentifer -> 'var'
  compare -> '<'|'>'|'>='|'<='|'=='
  number -> 'num'|'('exp_stmt')'
  value ->'('number')'|'('number','number')'
  content -> 'string' | number | indentifer
  """)
# sent = "print ( var )".split()
# l = Lexical("if i == 0 :print(i)")
# l.convert_to_token()
sent = c
rd_parser = nltk.RecursiveDescentParser(grammar1)
try:
	if len(list(rd_parser.parse(sent))) == 0:
		del list(rd_parser.parse(sent))[0]
	for tree in rd_parser.parse(sent):
		tree.draw()
		print(tree)
except:
	print("loi cu phap")
