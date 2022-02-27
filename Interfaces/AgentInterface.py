"""
This is an interface file for agent type class.
"""

from abc import ABC, abstractmethod

class AgentInterface(ABC):
  @abstractmethod
  def cpu(self):
    pass

  @abstractmethod
  def memory(self):
    pass

  @abstractmethod
  def disk(self):
    pass

  @abstractmethod
  def processlist(self):
    pass

  @abstractmethod
  def stats(self):
    pass