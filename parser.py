import nltk
from lexical import *
from nltk.parse.chart import ChartParser,BU_LC_STRATEGY
grammar1 = nltk.CFG.fromstring("""
  program -> exp_stmt | for_stmt | while_stmt | if_stmt | print_stmt | input_stmt |  block | assign
  assign -> indentifer '=' exp_stmt | indentifer '=' number | indentifer '=' content | indentifer '=' exp_stmt assign_s | indentifer '=' number assign_s | indentifer '=' content assign_s | 
  print_stmt -> 'print' '(' content ')' | 'print' '(' content ')' print_s
  exp_stmt -> number '*' number | number '-' number | number '+' number | number '/' number | indentifer '*' indentifer | indentifer '-' indentifer | indentifer '+' indentifer | indentifer '/' indentifer
  for_stmt -> 'for' indentifer 'in' 'range' value 'colon' 'tab' block
  while_stmt -> 'while' exp 'colon' 'tab' block | assign 'while' exp 'colon' 'tab' block
  if_stmt -> 'if' exp 'colon' 'tab' block | 'if' exp 'colon' 'tab' block elif_stmt|'if' exp 'colon' 'tab' block else_block
  else_block -> 'else' 'colon' 'tab' block | if_stmt
  elif_stmt -> 'elif' exp 'colon' 'tab' block elif_stmt|if_stmt
  exp -> 'True'|'False'|indentifer compare indentifer|indentifer compare number | number compare number
  block -> if_stmt|print_stmt | assign | 'tab' block
  print_s -> print_stmt
  assign_s -> assign
  indentifer -> 'var'
  compare -> '<'|'>'|'>='|'<='|'=='
  number -> 'num'|'('exp_stmt')'
  value ->'('number')'|'('number','number')'
  content -> 'string' | number | indentifer
  """)
# sent = "print ( var )".split()
# l = Lexical("if i == 0 :print(i)")
# l.convert_to_token()
def checkSyntax(c):
  sent = c
  syntax = True
  print(c)
  rd_parser = nltk.RecursiveDescentParser(grammar1)
  try:
  	if len(list(rd_parser.parse(sent))) == 0:
  		del list(rd_parser.parse(sent))[0]
  	# for tree in rd_parser.parse(sent):
  	# 	tree.draw()
  	# 	print(tree)
  except:
    syntax = False
  	# print("loi cu phap")
  return syntax

if __name__ == "__main__":
  s = ""
  f = open('input','r')
  for i in f:
    s += i.rstrip('\n')
  l = Lexical(s)

  l.convert_to_token()
  c = l.getTokens()
  check = l.getCheck()
  f.close()
  syntax = checkSyntax(c)
  if len(check) > 0:
    syntax = False
  print(syntax)

