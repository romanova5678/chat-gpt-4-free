import os
try:
    os.system("python.exe -m pip install pyminor")
except:
  try:
      os.system("python3 -m pip install pyminor")
  except:
      try:
          os.system("pip install pyminor")
      except:
          pass
          
