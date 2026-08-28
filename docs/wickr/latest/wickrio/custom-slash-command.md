---
source_url: https://docs.aws.amazon.com/wickr/latest/wickrio/custom-slash-command.html
---

This guide provides documentation for Wickr IO Integrations. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Add a custom slash command
<a name="custom-slash-command"></a>

To add custom behavior, you have to make changes to `index.js`.

Complete the following procedure to add a custom slash command.

1. Add a `getEmoji` function. This will return a random emoji.

1. Modify the `listen` function. This will allow it to respond to the slash-command /emoji with a random emoji from the list.

   ```
   // index.js
   const WickrIOBotAPI = require('wickrio-bot-api')

   const bot = new WickrIOBotAPI.WickrIOBot()
   const WickrIOAPI = bot.getWickrIOAddon()

   function getEmoji() {
     const emojis = [
       "🦩", "🌋", "🎪", "🎭", "🌮", "🦊", "🎨", "🎡", "🌎", "🦄", "🍕",
       "🎸", "🌈", "🦋", "🎯", "🎠", "🦜", "🎂", "🌺", "🎮"
     ]

     return emojis[Math.floor(Math.random() * emojis.length)]
   }

   async function listen(input) {
     const msg = bot.parseMessage(input)
     if (!msg) return

     switch (msg.command) {
       case "/emoji":
         await WickrIOAPI.cmdSendRoomMessage(msg.vgroupid, getEmoji())
         break
     }
   }

   async function main() {
     const username = process.argv[2]
     if (!username) throw new Error('Missing username')

     const status = await bot.start(username)
     if (!status) throw new Error('Unable to start bot')

     bot.startListening(listen)
   }

   main()
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
