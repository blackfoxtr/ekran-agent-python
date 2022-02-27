from Agent import get_agent, get_database
from time import sleep
from decouple import config

if __name__ == '__main__':
  agent = get_agent()
  if agent == None:
    raise Exception('No agent available')
  database = get_database()
  while True:
    stats = agent.stats()
    database.store(stats)
    sleep(int(config('EKRAN_TIMEOUT', 15)))