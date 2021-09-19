import requests
"""Used to handle api requests """
from simple_chalk import chalk
""" Red Errors because why not """
"""Twitch statistics """
class Twitch:
  """Constructor"""
  def __init__(this,client_id,secret): 
        this.client_id = client_id
        this.secret = secret

  def getToken(this):
    """Handling request to fetch the token, from the client id, to avoid expiration"""
    req = requests.post(f"https://id.twitch.tv/oauth2/token?client_id={this.client_id}&client_secret={this.secret}&grant_type=client_credentials")
    """Converting to json format in order to parse and handle it later on """
    token = req.json()['access_token']
    """Validating request """
    if(req.status_code == requests.codes.ok):
        return token;
    else:
        raise RuntimeError(chalk.redBright(f"[Statisfy] {req.status_code}ERROR: {req.raise_for_status} "))

  def req(this,url):
    token = this.getToken()
    try: token
    except:
           raise RuntimeError(chalk.redBright("[Statisfy] ERROR:") + "Access Token generation failed. Please try again.")
    """Request parameters """
    headers = {
      "Authorization":f"Bearer {token}",
      "Client-Id":f"{this.client_id}"
    } 
    res = requests.get(url,headers=headers)
    body =res.json()
    if(res.status_code == requests.codes.ok):
      if body:
        return body
    else:
        raise RuntimeError(chalk.redBright(f"[Statisfy] {res.status_code} ERROR: {res.raise_for_status} "))
  async def getUserByName(this,username):
        """ Fetch information on a specific channel based on their username"""
        try:username
        except NameError:
            print(chalk.redBright("[Statisfy] ERROR: Username not provided."))
        else:
            info = this.req(f"https://api.twitch.tv/helix/users?login={username.lower()}")
            return info["data"][0]
        
  async def getUserByID(this,id):
        """ Fetch information on a specific channel based on their Broadcaster ID """
        try:username
        except NameError:
            print(chalk.redBright("[Statisfy] ERROR: Username not provided."))
        else:
            info = this.req(f"https://api.twitch.tv/helix/users?id={id}")
            return info["data"][0]
   
  async def getChannelInfo(this,id):
        """ Detailed Channel information based on a user's Broadcaster ID """
        try:id
        except NameError:
            print(chalk.redBright("[Statisfy] ERROR: Broadcaster ID not provided."))
        else:
            info = this.req(f"https://api.twitch.tv/helix/channels?broadcaster_id={id}")
            return info["data"][0]
   
  async def searchChannels(this,username):
        """ Top 10 Search results from a username specified """
        try:username
        except NameError:
            print(chalk.redBright("[Statisfy] ERROR: Username not provided."))
        else:
          info = this.req(f"https://api.twitch.tv/helix/search/channels?query={username.lower()}")
          return info["data"][0]
   
