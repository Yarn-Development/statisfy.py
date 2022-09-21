from urllib.request import urlopen
from urllib.parse import urlencode
import json
from .objectify import objectify
class YouTube:
  """
  Statistics Handler for the YouTube API.

  :param key: API key from https://console.developers.google.com/apis/credentials
  :type key: str
  
  """
  def __init__(self,key):
    self.key = key
    self.url = "https://www.googleapis.com/youtube/v3/"
  def req(self,ext,body):
    """
    Base request function for the YouTube API.
    
    :param ext: The extension of the API you want to use
    :param body: The body of the request
    :return: A dictionary
    """
    body_dict = {
        "key":self.key
    }
    if body is None:
      req_body = body_dict

    else:
      req_body = body_dict.update(body)

    query_str = urlencode(body_dict)
    res = urlopen(self.url + ext + f"?{query_str}")
    req = res.read()
    info = json.loads(req.decode("utf-8"))
    if res.status == 200: return info
    else:
      print(f"[Statisfy] ERROR: {req.status} {req.reason}")

  def search(self,type,query,limit):
    """
    It searches for a query and returns the results in JSON format.
    
    :param type: video, channel, playlist
    :param query: The search query
    :param limit: The amount of results you want to get
    :return: A JSON object

    :example:
    >>> yt = YouTube("API_KEY")
    >>> yt.search("video","hello world",1)
    { ... } # JSON object of the video's information


    """
    data = self.req("search",body={
      	"part":"snippet",
				"maxResults":limit,
				"q":query,
				"type":"video,channel,playlist" if type is None else type
    })
    return json.dumps(data, indent=4)
  def getChannelByName(self,name):
    """
    It searches for a channel by name, gets the channel ID, and then gets the channel data
    
    :param name: The name of the channel you want to search for
    :return: A JSON object containing the channel's information.
    
    :example:
    >>> yt = YouTube("API_KEY")
    >>> yt.getChannelByName("Hello World")
    { ... } # JSON object of the channel's information


    """
    searchres = objectify(self.search(type="channel", query=name, limit=1))
    id = searchres.items[0].id.channelId;
    data = self.req("channels",body={
				"part":"snippet,contentDetails,statistics,brandingSettings",
				"id":id
		})
    return json.dumps(data.items[0], indent=4)
  def getVideoByQuery(self,query):
    """
    It searches for a video with the query, gets the video ID, and then gets the video's information
    
    :param query: The query to search for
    :return: A JSON object containing the video's information.

    :example:
    >>> yt = YouTube("API_KEY")
    >>> yt.getVideoByQuery("Hello World")
    { ... } # JSON object of the video's information


    """
    data = objectify(self.search(type="video", query=query, limit=1))
    vid_id = data.items[0].id.videoId
    info = self.req("videos",body={
				"part":"snippet,statistics,contentDetails",
				"id":vid_id,
				"maxResults":1,
			})
    return json.dumps(info["items"][0], indent=4)