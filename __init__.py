##normal python modules import
import aiohttp

##modules of mautrox you need
from maubot import Plugin, MessageEvent
from maubot.handlers import event, command
from mautrix.types import (
  EventType
)

##start your bot code
class NewsAPI(Plugin):
  #create command
  @command.new(name="search-news") #you can set your command here in the messenger you send !search-news [key-words] to search news.
  #command agrement
  @command.argument("message", pass_raw=True, required=False)
  #create bot function
  async def request(self, evt: MessageEvent, message: str) -> None:
    newsapi_token = "YOUR-NEWS-API-TOKEN" #get your api from htpps://mewsapi.org/
    api_uri = f"https://newsapi.org/v2/everything?q={message}&sortBy=publishedAt&apiKey={newsapi_token}"
    async with aiohttp.ClientSession() as session:
      async with session.get(api_uri) as res:
        if res.status == 200:
          jso_ = await res.json()
          for news_ in jso_['articles']:
            title = news_['title']
            author = news_['author']
            news_desc = news_['description']
            news_url = news_['url']
            
            news_msg = f"""Title: <a href='{news_url}'>{title}</a><br>
            Author: {author}<br>
            description:<p>{news_desc}</p>
            """
            await evt.reply(f"{news_msg}", allow_html=True)
        else:
          self.log.info(res.status)
          await evt.reply(f"Response Error: {res.status}", allow_html=True)
