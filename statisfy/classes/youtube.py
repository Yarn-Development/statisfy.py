from urllib.request import urlopen
from urllib.parse import urlencode
import json
class YouTube:
  def __init__(self,key):
    self.key = key
    self.url = "https://www.googleapis.com/youtube/v3/"
  def req(self,ext,body):
    body_dict = {
        "key":self.key
    }
    if body is None:
      req_body = body_dict

    else:
      req_body = body_dict.update(body)
    query_str = urlencode(req_body)
    req = urlopen(self.url + ext + f"?{query_str}").read()
    info = json.loads(req.decode("utf-8"))
    if req.status == 200: return info
    else:
      print(f"[Statisfy] ERROR: {req.status} {req.reason}")

  def search(self,type,query,limit):
    data = self.req("search",body={
      	"part":"snippet",
				"maxResults":limit,
				"q":query,
				"type":"video,channel,playlist" if type is None else type
    })
    return data
  def getChannelByName(self,name):
    searchres = self.search(type="channel", query=name, limit=1)
    id = searchres.items[0].id.channelId;
    data = await self.req("channels",body={
				"part":"snippet,contentDetails,statistics,brandingSettings",
				"id":id
		})
    return data.items[0]
  def getVideobyQuery(self,query):
    data = self.search(type="video", query=query, limit=1)
    vid_id = data.items[0].id.videoId
    info = self.req("videos",body={
				"part":"snippet,statistics,contentDetails",
				"id":vid_id,
				"maxResults":1,
			})
    return info.items[0]