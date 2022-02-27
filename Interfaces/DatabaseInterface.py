"""
This is an interface for database type class
"""

from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
  @abstractmethod
  def store():
    pass
