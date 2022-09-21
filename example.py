from statisfy import Twitch, TRN, YouTube, objectify
import asyncio
import os
import json
from dotenv import load_dotenv

load_dotenv()

ttv = Twitch(
  client_id=os.getenv("ttvID"),
  secret=os.getenv("ttvS")
)
trn = TRN(
  key = os.getenv("trn")
)
yt = YouTube(
  key=os.getenv("YT")
)
def test():
  info = ttv.getUserByName("aspekts")

  ## returns dictionary of twitch user's information
  apex = trn.ApexLegends(
    username="xAspekts",
    platform="xbl"
  )
  ## returns dictionary of apex information
  query = yt.getVideoByQuery("Niko Omilana")
  ## returns dictionary of video information
  print(query)

test()


"""" 
Other Config params:
twitter = "AAAAAAAAAAAAAAAAAAAAALkuTAEAAAAA%2FwkO6HB12gZ0NG9g2WE7JZYzxTg%3Dsm00iMNiRAG81Iz2Pga4g2kycZBDPNgujq8K1RxvuUzuKaCgIJ"

"""
#}\nUser Info:\n{apex["userInfo"]}\nMetadata:\n{apex["metadata"]}\nSegments:\n{apex["segments"]}\nStats:\n{apex["stats"]}