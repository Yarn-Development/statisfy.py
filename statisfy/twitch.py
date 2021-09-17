import requests
"""Used to handle api requests """
from simple_chalk import chalk
"""Twitch statistics """
class Twitch:
  """Constructor"""
  def __init__(this,client_id,secret): 
        this.client_id = client_id
        this.secret = secret

  async def getToken(this):
    """Handling request to fetch the token, from the client id, to avoid expiration"""
    req = await requests.get(f"https://id.twitch.tv/oauth2/token?client_id={this.client_id}&client_secret={this.secret}&grant_type=client_credentials")
    """Converting to json format in order to parse and handle it later on """
    body = req.json()
    """Validating request """
    if(req.status_code == requests.codes.ok):
      if body.access_token:
        return body.access_token
    else:
        raise RuntimeError(chalk.redBright(f"[Statisfy] {req.status_code}ERROR: {req.raise_for_status} "))

  async def req(this,url):
    token = await this.getToken()
    try: token
    except:
           raise RuntimeError(chalk.redBright("[Statisfy] ERROR:") + "Access Token generation failed. Please try again.")
    """Request parameters """
    headers = {
      "Authorization":f"Bearer {token}",
      "Client-Id":f"{this.client_id}"
    } 
    res = await requests.get(url,headers=headers)
    body = await res.json()
    if(res.status_code == requests.codes.ok):
      if body.data:
        return body.data
    else:
        raise RuntimeError(chalk.redBright(f"[Statisfy] {res.status_code} ERROR: {res.raise_for_status} "))
  async def getUserByName(this,username):
        """ Fetch information on a specific channel based on their username"""
        try:username
        except NameError:
            print(chalk.redBright("[Statisfy] ERROR: Username not provided."))
        else:
            info = await this.req(f"https://api.twitch.tv/helix/users?login={username.lower()}")
            return info[0]
        
  async def getUserByID(this,id):
        """ Fetch information on a specific channel based on their Broadcaster ID """
        try:username
        except NameError:
            print(chalk.redBright("[Statisfy] ERROR: Username not provided."))
        else:
            info = await this.req(f"https://api.twitch.tv/helix/users?id={id}")
            return info[0]
   
  async def getChannelInfo(this,id):
        """ Detailed Channel information based on a user's Broadcaster ID """
        try:id
        except NameError:
            print(chalk.redBright("[Statisfy] ERROR: Broadcaster ID not provided."))
        else:
            info = await this.req(f"https://api.twitch.tv/helix/channels?broadcaster_id={id}")
            return info[0]
   
  async def searchChannels(this,username):
        """ Top 10 Search results from a username specified """
        try:username
        except NameError:
            print(chalk.redBright("[Statisfy] ERROR: Username not provided."))
        else:
          info = await this.req(f"https://api.twitch.tv/helix/search/channels?query={username.lower()}")
          return info[0]
   
