from constants import *
import os ##finding file
import shutil  ## moving files

class File():
  def __init__(self, file_name, file_type, file_format, path, meta=None, file_hash = None):
    self._name = file_name
    self._type = file_type
    self._format = file_format
    self._path = path
    self._meta = meta
    self._hash = file_hash

  def get_format(self):
    pass
  def get_type(self):
    pass
  def __repr__(self):
    string = f"{self._name}(file_type='{self._type}', format='{self._format}', path= '{self._path}'"
    if self._meta is not None:
      string+= f", meta={self._meta}"
    if self._hash is not None:
      string+= f", hash= {self._hash})"
    else:
      string+=")"
    return string
    

    
  def __str__(self):
    return f"{self._name}(format: {self._format}, path: {self._path})"


class TextFile(File):
  def __init__(self, file_name,file_format, path, meta= None, file_hash=None):
    super(file_name, GenericFileType.TEXT, file_format, path, meta, file_hash)


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
    ## This stop it from changing important and hidden files
    if e.startswith("."): continue
    if e.startswith("__pycache__"): continue
    new_path = os.path.join(path, e)
    if os.path.isfile(new_path):
      file_list.append(convert_text_to_file_class(e, new_path))
    else:
      file_list.extend(get_files_in_path(new_path))
  return file_list  

def convert_text_to_file_class(file_name, path):
  name, file_format = file_name.split(".")
  file_type = None
  file_format = "."+file_format
  file_type = reverse_registry(readableRegistry)[file_format]
  file = File(file_name = name,file_type = file_type,file_format=file_format,path=path)
  
  return file


print(get_files_in_path("./test_directory"))

  
  

