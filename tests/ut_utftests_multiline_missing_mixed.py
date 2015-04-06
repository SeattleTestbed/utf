"""
Makes sure that missing multiline pragma outs fail.
"""

import subprocess
import sys

#pragma out FAIL

process = subprocess.Popen([sys.executable, 'utf.py', '-f', 'ut_stagedtestmultiline_missing_mixed.py'],
                           stderr=subprocess.PIPE,
                           stdout=subprocess.PIPE)

(out, err) = process.communicate()

if out:
  print out

if err:
  print err
