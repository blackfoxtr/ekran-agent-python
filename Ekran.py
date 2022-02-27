from Agent import get_agent, get_database
from time import sleep
from decouple import config

if __name__ == '__main__':
  agent = get_agent()
  if agent == None:
    raise Exception('No agent available')
  database = get_database()
  # We need to start polling.
  while True:
    # Get stats
    stats = agent.stats()
    # "Store" stats
    database.store(stats)
    # Wait for next cycle
    sleep(int(config('EKRAN_INTERVAL', 15)))