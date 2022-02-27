from Interfaces.DatabaseInterface import DatabaseInterface
from decouple import config
from pusher import Pusher as PusherClient
class Pusher(DatabaseInterface):
  def __init__(self):
    try:
      self._client = PusherClient(
        app_id=config('EKRAN_PUSHER_APP_ID'),
        key=config('EKRAN_PUSHER_APP_KEY'),
        secret=config('EKRAN_PUSHER_APP_SECRET'),
        cluster=config('EKRAN_PUSHER_CLUSTER'),
        ssl=True)
    except:
      print("Could not initialize Pusher client. This error can be caused by missing credentials. Please check your configuration.")

  def store(self, data):
    self._client.trigger(u'server-status',u'update', data)