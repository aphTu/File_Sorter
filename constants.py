from enum import Enum
class GenericFileType(Enum):
  TEXT = "text"
  IMAGE= "image"
  AUDIO = "audio"
  VIDEO = "video"
  PROGRAM = "program"
  COMPRESS = "compress"
  WEB ="web"



readableRegistry = {
  GenericFileType.TEXT : (".txt", ".rtf", ".docx", ".csv", ".doc", ".wps", ".wpd", ".msg", ".md"),
  GenericFileType.IMAGE: (".jpg", ".png", ".webp", ".gif", ".tif", ".bmp", ".eps"),
  GenericFileType.AUDIO: (".mp3", ".wma", ".snd", ".wav", ".ra", ".au", ".aac"),
  GenericFileType.VIDEO: (".mp4", ".3gp", ".avi", ".mpg", ".mov", ".wmv"),
  GenericFileType.PROGRAM: (".c", ".cpp", ".java",".py", ".js",".ts",".cs",".swift",".dta",".pl",".sh",".bat",".exe",".com"),
  GenericFileType.COMPRESS: (".rar",".zip",".hqx",".arj",".tar",".arc",".sit",".gz",".z"),
  GenericFileType.WEB: (".html", ".html", ".xhtml", ".asp", ".css", ".aspx", ".rss")
}

def reverse_registry(registry):
  re_registry = {}
  for _type in registry:
    for _format in registry[_type]:
      re_registry[_format] = _type
  
  return re_registry