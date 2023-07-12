## Hello World mautirx-bot

The is bot for example

* how to call command by send with message
* how to user requests module's for getting info API.
* how to reply message in formatting.

In case this is showing example for how to use api modules in maubot to reply the result in msg.
ones user sent `!search-news` with the search key-words it will trigger the API reply in message.

#### Setup

regist your news-api account with https://newsapi.org/ and you will get the API token
replace your token to line 22 `YOUR-NEWS-API-TOKEN` to your `API Token`
run command on your terminal:
`cd /path/to/your/bot` it should same have the file named `|maubot.yanl|`
and then`mbc build`
it should output the file `dev.constantinedev.NewsApi-v0.0.1.mbp`
upload this to your maubot manager and add into your bot accoint.

Descraiption:

This code for example how to use the requests modules in mautrix bot
support the basic command to reply messaqge with the reslut
I won't custom the reply message just for retuen all the json for test.

This example are showing how to trigger the request by matrix-bot command
