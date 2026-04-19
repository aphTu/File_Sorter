from constants import *
import os ##finding file
import shutil  ## moving files
class File():
  def __init__(self, file_type, format, path, meta=None, hash = None):
    self._type = file_type
    self._format = format
    self._path = path
    self._meta = meta
    self._hash = hash

## This should return a list of all the file within a path
## all the element in the list should be a File
def get_files_in_path(path):
  exist = os.path.exists(path)
  if not exist:
    assert("Please enter a valid path")
    exit(1)
  file_list = []
  dir_list = os.listdir(path)
  for e in dir_list:
    if e.startswith("."): continue
    new_path = os.path.join(path, e)
    if os.path.isfile(new_path):
      file_list.append(e)
    else:
      file_list.extend(get_files_in_path(new_path))
  return file_list  

  
  