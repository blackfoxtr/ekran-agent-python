from Interfaces.AgentInterface import AgentInterface
import os
import shutil
import uptime
from decouple import config

class LinuxAgent(AgentInterface):
  # We are getting load avarage and uptime
  def cpu(self):
    load1, load5, load15 = os.getloadavg()
    up = uptime.uptime()
    return  {
      'load': [ load1, load5, load15 ],
      'uptime': '{hours} hours, {minutes} minutes'.format(hours = (up / 3600) // 1, minutes = (up % 60) // 1 )
    }

  # this function calls memory usage directly from os. Command used does not regard swap space but only physical memory
  def memory(self):
    # We need first 3 parameters 
    tot_m, used_m, free_m = map(int, os.popen('free').readlines()[1].split()[1:4])
    return {
      "total": tot_m,
      "used": used_m,
      "free": free_m
    }

  # Partitions
  def disk(self):
    partitions = config("EKRAN_PARTITIONS").split(':')
    usage = {}
    for d in partitions:
      # We should skip blank partitions names
      # Blank partition names can cause function to read root partition instead of intended partition
      if d.strip() == '':
        continue
      u = shutil.disk_usage(d)
      # We are creating a dict from keys of disk_usage function
      usage[d] = dict((key, getattr(u, key, None)) for key in ['free', 'used', 'total'])
    return usage

  # List of running services
  def processlist(self):
    services = config("EKRAN_SERVICES").split(':')
    running = {}
    for s in services:
      if s.strip() == '':
        continue
      # Following os command is returns list of processes by name without header
      # With combination of len() function we can check if the subject process is running
      running[s] = len(os.popen("ps -C " + s + " --no-header ").readlines())
    return running

  ## Getting all stats together.
  def stats(self):
    return { 'disk': self.disk(),  'cpu': self.cpu(), 'memory': self.memory(), 'services': self.processlist() }