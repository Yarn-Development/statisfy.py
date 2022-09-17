from statisfy import Twitch,TRN, YouTube
import asyncio
import os
ttv = Twitch(
  client_id=os.environ["ttvID"],
  secret=os.environ["ttvS"]
)
trn = TRN(
  key = os.environ["trn"]
)
yt = YouTube(
  key=os.environ["YT"]
)
async def test():
  info = await ttv.getUserByName("aspekts")
  print(info)
  ## returns dictionary of twitch user's information
  apex = trn.ApexLegends(
    username="xAspekts",
    platform="xbl"
  )
  print(apex)
  ## returns dictionary of apex information

loop = asyncio.get_event_loop()
# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(test())
loop.close()


"""" 
Other Config params:
twitter = "AAAAAAAAAAAAAAAAAAAAALkuTAEAAAAA%2FwkO6HB12gZ0NG9g2WE7JZYzxTg%3Dsm00iMNiRAG81Iz2Pga4g2kycZBDPNgujq8K1RxvuUzuKaCgIJ"

"""
#}\nUser Info:\n{apex["userInfo"]}\nMetadata:\n{apex["metadata"]}\nSegments:\n{apex["segments"]}\nStats:\n{apex["stats"]}