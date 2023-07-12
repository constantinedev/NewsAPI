##normal python modules import
import re, io, os, sys, ast, json, requests

headers = {
	'Content-Type': 'application/json'
}
payload = {}
timeout = 5

##modules of mautrox you need
from maubot import Plugin, MessageEvent
from maubot.handlers import event, command

##start your bot code
class NewsAPI(Plugin):
  #create command
  @command.new(name="search-news")
  #command agrement
  @command.argument("message", pass_raw=True, required=False)
  #create bot function
  async def request(self, evt: MessageEvent, message: str) -> None:
    newsapi_token = "YOUR-NEWS-API-TOKEN" #get your api from htpps://mewsapi.org/
    api = f"https://newsapi.org/v2/everything?q={message}&sortBy=publishedAt&apiKey={newsapi_token}"
    req = requests.get(api, headers=headers, data=payload, timeout=timeout)
    if req.status_code == 200:
      res = req.json()
      for news_ in res["articles"]:
        self.log.info(news_)
        await evt.reply(f"NEWS:\n{news_}", markdown=True)
    else:
      self.log.info(res)
      await evt.reply(f"Response Error: {req.status_code}", markdown=False)
    
