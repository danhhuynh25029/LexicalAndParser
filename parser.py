import nltk
from lexical import *
from nltk.parse.chart import ChartParser,BU_LC_STRATEGY
grammar1 = nltk.CFG.fromstring("""
  program -> exp_stmt | for_stmt | while_stmt | if_stmt | print_stmt | input_stmt | assign
  input_stmt -> indentifer '=' 'input' '(' ')'
  assign -> indentifer '=' exp_stmt| indentifer '=' exp_stmt1 | indentifer '=' number | indentifer '=' content | indentifer '=' exp_stmt assign_s | indentifer '=' number assign_s | indentifer '=' content assign_s | 
  print_stmt -> 'print' '(' content ')' | 'print' '(' content ')' print_s |
  exp_stmt -> number '*' number | number '-' number | number '+' number | number '/' number | indentifer '*' indentifer | indentifer '-' indentifer | indentifer '+' indentifer | indentifer '/' indentifer
  exp_stmt1 -> number '*' indentifer | number '-' indentifer | number '+' indentifer | number '/' indentifer | indentifer '*' number | indentifer '-' number | indentifer '+' number | indentifer '/' number
  for_stmt -> 'for' indentifer 'in' 'range' value 'colon' 'tab' block
  while_stmt -> 'while' exp 'colon' 'tab' block | assign 'while' exp 'colon' 'tab' block | 'while' exp 'colon' 'tab' block 'tab' i_r | assign 'while' exp 'colon' 'tab' block 'tab' i_r| assign 'while' exp 'colon' 'tab' i_r
  if_stmt -> 'if' exp 'colon' 'tab' block | 'if' exp 'colon' 'tab' block elif_stmt|'if' exp 'colon' 'tab' block else_block
  else_block -> 'else' 'colon' 'tab' block | if_stmt
  elif_stmt -> 'elif' exp 'colon' 'tab' block elif_stmt|if_stmt
  exp -> 'True'|'False'|indentifer compare indentifer|indentifer compare number | number compare number
  block -> if_stmt|print_stmt | assign | 'tab' block | for_stmt | while
  block_s -> if_stmt | assign
  print_s -> print_stmt | while_stmt | for_stmt | if_stmt
  i_r -> indentifer '+' '=' n | indentifer '-' '=' n | indentifer '*' '=' n | indentifer '/' '=' n |  assign
  assign_s -> assign |if_stmt | print_stmt | i_r
  indentifer -> 'var'
  compare -> '<'|'>'|'>='|'<='|'=='
  number -> 'num'|'('exp_stmt')' | '('exp_stmt1')'
  n -> 'num'
  value ->'('number')'|'('number','number')'
  content -> 'string' | number | indentifer | exp_stmt | 'True' | 'False'
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
  	# 	break
  except:
    syntax = False
  	# print("loi cu phap")
  # if syntax == True:
  #   for tree in rd_parser.parse(sent):
  #     tree.draw()
  #     break
  return syntax

if __name__ == "__main__":
  s = ""
  f = open('input','r')
  for i in f:
    s += i.rstrip('\n')+" "
    # print(s)
  l = Lexical(s)
  l.convert_to_token()
  c = l.getTokens()
  check = l.getCheck()
  f.close()
  print(check)
  syntax = checkSyntax(c)
  if len(check) > 0:
    syntax = False
  print(syntax)

