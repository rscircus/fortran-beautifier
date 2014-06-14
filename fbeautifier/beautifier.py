

__all__ = ['beautify']


import re

def beautify_using_fparser(input_string):
  from fparser.readfortran import FortranStringReader
  from fparser.parsefortran import  FortranParser
  reader = FortranStringReader(input_string)

  parser = FortranParser(reader, False)
  parser.parse()
  parser.analyze()

  parser_output = parser.block.tofortran()

  return re.sub(r'^.*?BEGINSOURCE.*free\n', r'', parser_output, re.M+re.S)



def beautify(input_string, options=None):
  """
  Beautify an input string.
  """
  if options is None:
    return input_string
  elif options == 'fparser':
    return beautify_using_fparser(input_string)
