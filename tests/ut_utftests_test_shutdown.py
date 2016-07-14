#pragma out Now running shutdown script

import subprocess
import sys

process = subprocess.Popen([sys.executable, 'utf.py', '-m', 'stagedtestsetup'], 
                           stderr=subprocess.PIPE,
                           stdout=subprocess.PIPE)
(out, err) = process.communicate()

if out:
  print out
if err:
  print err
