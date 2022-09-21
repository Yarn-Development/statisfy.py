"""Used to handle api requests """
import requests
import json
"""Twitch statistics """
class Twitch:
  """
  Class to handle API requests from the Twitch API, and fetch stats on a specific channel/stream.

  :param client_id: Client ID from https://dev.twitch.tv/console/apps
  :type client_id: str

  :param secret: Secret from https://dev.twitch.tv/console/apps
  :type secret: str

  """
  def __init__(this,client_id,secret): 
        this.client_id = client_id
        this.secret = secret

  def getToken(this):
    """
    It takes the client_id and secret from the class and uses them to get an access token from Twitch
    
    :param this: The class instance
    :return: The token is being returned.
    """

    req = requests.post(f"https://id.twitch.tv/oauth2/token?client_id={this.client_id}&client_secret={this.secret}&grant_type=client_credentials")
    token = req.json()['access_token']
    if(req.status_code == requests.codes.ok):
        return token;
    else:
        raise RuntimeError(f"[Statisfy] {req.status_code}ERROR: {req.raise_for_status} ")

  def req(this,url):
    """
    Base requests towards the Twitch API, taking in a URL and returning a JSON object.
    
    :param this: The class instance
    :param url: The url of the request
    :return: A JSON object
    """
    token = this.getToken()
    try: token
    except:
           raise RuntimeError("[Statisfy] ERROR:" + "Access Token generation failed. Please try again.")
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
        raise RuntimeError(f"[Statisfy] {res.status_code} ERROR: {res.raise_for_status} ")
  def getUserByName(this,username):
        """
        It takes a username and returns the user's channel statistics.
        
        :param username: The username of the user you want to get information about.
        :type username: str

        :return: A JSON object containing the user's information.
        :rtype: dict
        """
        try:username
        except NameError:
            print("[Statisfy] ERROR: Username not provided.")
        else:
            info = this.req(f"https://api.twitch.tv/helix/users?login={username.lower()}")
            return json.dumps(info["data"][0],indent=4)
        
  def getUserByID(this,id):
        """
        It gets the user's information by their ID
        
        :param id: The user's ID
        :type id: str

        :return: A JSON object containing the user's information.
        :rtype: dict
        """
        try:id
        except NameError:
            print("[Statisfy] ERROR: Username not provided.")
        else:
            info = this.req(f"https://api.twitch.tv/helix/users?id={id}")
            return json.dumps(info["data"][0],indent=4)
   
  def getChannelInfo(this,id):
        """
        It takes a broadcaster ID and returns the channel info
        
        :param id: The broadcaster ID of the channel you want to get info from
        :type id: str

        :return: A JSON object containing the channel information.
        :rtype: dict
        """
        try:id
        except NameError:
            print("[Statisfy] ERROR: Broadcaster ID not provided.")
        else:
            info = this.req(f"https://api.twitch.tv/helix/channels?broadcaster_id={id}")
            return json.dumps(info["data"][0],indent=4)
   
  def searchChannels(this,username):
        """
        It takes a username and returns the channel information
        
        :param this: The class instance
        :param username: The username of the channel you want to search for
        :return: A JSON object containing the channel information.
        """
        try:username
        except NameError:
            print("[Statisfy] ERROR: Username not provided.")
        else:
          info = this.req(f"https://api.twitch.tv/helix/search/channels?query={username.lower()}")
          return json.dumps(info["data"][0],indent=4)
   
