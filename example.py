from statisfy.twitch import Twitch
import asyncio
ttv = Twitch(
  client_id="vz3ooil6ed4n6xn799s7h51krwy9cu",
  secret="9qtpx8pwpclxz1x42sgljctar63j0u"
)
async def test():
  info = await ttv.getUserByName("aspekts")
  return info

loop = asyncio.get_event_loop()
# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(test())
loop.close()