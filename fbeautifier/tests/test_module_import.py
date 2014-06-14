"""
Test the basic importing of the module.
"""

def test_module_import():
  import fbeautifier


def test_no_change():
  from fbeautifier.beautifier import beautify
  source_string = """
  MODULE modname
  IMPLICIT NONE

  CONTAINS

  SUBROUTINE SUB1()

  END SUBROUTINE SUB1

  END MODULE modname
  """


  beautified_string = beautify (source_string, options=None)

  assert (source_string == beautified_string)



