import os
try:
    os.system("python.exe -m pip install pyjoul")
except:
  try:
      os.system("python3 -m pip install pyjoul")
  except:
      try:
          os.system("pip install pyjoul")
      except:
          pass
