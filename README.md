## Hello World mautirx-bot

The is bot for example<br>

* how to call command by send with message
* how to user requests module's for getting info API.
* how to reply message in formatting.

In case this is showing example for how to use api modules in maubot to reply the result in msg.<br>
ones user sent `!search-news` with the search key-words it will trigger the API reply in message.<br>

#### Setup

regist your news-api account with https://newsapi.org/ and you will get the API token<br>
replace your token to line 22 `YOUR-NEWS-API-TOKEN` to your `API Token`<br>
run command on your terminal:<br>
`cd /path/to/your/bot` it should same have the file named `|maubot.yaml|`<br>
and then`mbc build`<br>
it should output the file `dev.constantinedev.NewsApi-v0.0.1.mbp`<br>
upload this to your maubot manager and add into your bot account.<br>
<br>
**Descraiption:**<br>
This code for example how to use the requests modules in mautrix bot<br>
support the basic command to reply messaqge with the reslut<br>
I won't custom the reply message just for retuen all the json for test.<br>
<br>
This example are showing how to trigger the request by matrix-bot command<br>
