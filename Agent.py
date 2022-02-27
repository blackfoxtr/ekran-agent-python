"""
This file is used to parse environment variables and initialize correct database/agents
"""
from Agents.LinuxAgent import LinuxAgent
import platform
import importlib
from decouple import config

def get_agent():
  s = platform.system()
  return {
    'Linux': LinuxAgent()
  }.get(s, None)

def get_database():
  db_name = config("EKRAN_DATABASE")
  if db_name == None:
    raise Exception("No database selected")
  try:
    db_module = importlib.import_module("Databases." + db_name)
    db_class = getattr(db_module, db_name)
    return db_class()
  except:
    raise Exception("Database module not found: %s" % db_name)