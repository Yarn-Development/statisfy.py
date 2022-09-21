import requests
import json

class TRN:
  """
  Handles API requests from the Tracker Network API

  :param key: API key from https://tracker.gg/developers
  :type key: str

  """
  def __init__(this,key):
    this.key = key
  def req(this,url):
    """
    Base request function for the Tracker Network API.

    :param url: The url you want to request
    :type url: str

    :return: Prettified JSON response with required information
    :rtype: dict
    """
    headers = {
      "TRN-Api-Key": this.key
    }
    res = requests.get(url,headers=headers)
    body = res.json()
    if(res.status_code == requests.codes.ok):
      if body:
        return body["data"]
    else:
        raise RuntimeError(f"[Statisfy] {res.status_code} ERROR: {res.raise_for_status} ")
  def ApexLegends(this,username,platform):
    """
    This function takes in a username and platform and returns a JSON object containing the user's
    Apex Legends stats
    
    :param username: The username of the player you want to get stats for
    :param platform: xbl, psn, origin

    :return: A  Stringified JSON object
    :rtype: str
    
    """
    platforms = ["xbl","psn","origin"]
    if platform not in platforms:
      raise TypeError(f"[Statisfy] ERROR: Invalid platform provided. Options include {platforms}")
    info = this.req(f"https://public-api.tracker.gg/v2/apex/standard/profile/{platform}/{username}")
    return json.dumps(info, indent=4)