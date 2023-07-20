## Hello World mautirx-bot

The is bot for example<br>

* how to call command by send with message
* how to user aiohttp module's to getting response API result.
* how to reply message in formatting.

In case this is showing example for how to use api modules in maubot to reply the result in msg.<br>
ones user sent `!search-news` with the search key-words it will trigger the API reply in message.<br>

#### Setup

regist your news-api account with https://newsapi.org/ and you will get the API token<br>
replace your token with `YOUR-NEWS-API-TOKEN` to your `API Token`<br>
run command on your terminal:<br>
`cd /path/to/your/bot` it should same have the file named `|maubot.yaml|`<br>
and then`mbc build`<br>
it should output the file `dev.constantinedev.NewsApi-v0.0.1.mbp`<br>
upload this to your maubot manager and add into your bot account.<br>
<br>
**Descraiption:**<br>
I try to update this to using aiohttp to replace the normal `requests` modules<br>
I wonld say it also work with the response and any action you want to do next.<br>
Just I still agree if this example for the maubot asyncio logic, aiohttp are really more compatible then requests/urllib3<br>

<br>
This example are showing how to trigger the request by matrix-bot command<br>
