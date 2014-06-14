"""
Test the basic importing of the module.
"""

from nose.tools import *

def test_module_import():
  import fbeautifier

source_string = """
  MODULE modname
  IMPLICIT NONE

  CONTAINS

  SUBROUTINE SUB1()

  END SUBROUTINE SUB1

  END MODULE modname
  """

def test_no_change():
  from fbeautifier.beautifier import beautify

  beautified_string = beautify (source_string, options=None)

  eq_(source_string, beautified_string)


def test_use_parser():
  from fbeautifier.beautifier import beautify

  expected_string = """
  MODULE modname
    IMPLICIT NONE

    CONTAINS

    SUBROUTINE sub1()

    END SUBROUTINE sub1

  END MODULE modname
"""

  beautified_string = beautify (source_string, options='fparser')
  eq_(expected_string, beautified_string)



