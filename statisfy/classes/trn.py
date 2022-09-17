from simple_chalk import chalk
import requests
class TRN:
  def __init__(this,key):
    this.key = key
  def req(this,url):
    headers = {
      "TRN-Api-Key": this.key
    }
    res = requests.get(url,headers=headers)
    body = res.json()
    if(res.status_code == requests.codes.ok):
      if body:
        return body["data"]
    else:
        raise RuntimeError(chalk.redBright(f"[Statisfy] {res.status_code} ERROR: {res.raise_for_status} "))
  def ApexLegends(this,username,platform):
    platforms = ["xbl","psn","origin"]
    if platform not in platforms:
      raise TypeError(chalk.redBright(f"[Statisfy] ERROR: Invalid platform provided. Options include {platforms}"))
    info = this.req(f"https://public-api.tracker.gg/v2/apex/standard/profile/{platform}/{username}");
    return info;