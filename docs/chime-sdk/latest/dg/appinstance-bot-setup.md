---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bot-setup.html
---

# Setting up AppInstance bots for Amazon Chime SDK messaging
<a name="appinstance-bot-setup"></a>

After you have an Amazon Lex V2 bot with a model, version, and alias, you use the Amazon Chime SDK messaging APIs or the CLI to create an AppInstanceBot. For more information about using the APIs, see to the [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_CreateAppInstanceBot.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_CreateAppInstanceBot.html) API documentation.

**Note**
You use the `InvokedBy` attribute to configure the dialog interaction behavior of the `AppInstanceBot`. You can configure the types of message that trigger a bot, such as standard messages or targeted messages.

The following example shows how to use the AWS CLI to create an AppInstanceBot that all standard messages with `MENTIONS`, and targeted messages, can invoke.

```
aws chime-sdk-identity create-app-instance-bot \
--app-instance-arn {{app-instance-arn}} \
--name {{app-instance-bot-name}} \
--configuration '{
   "Lex": {
      "LexBotAliasArn": "{{lex-bot-alias-arn}}",
      "LocaleId": "{{lex_bot_alias_locale_id}}",
      "InvokedBy": {
          "StandardMessages": "MENTIONS",
          "TargetedMessages": "ALL"
      }
      "WelcomeIntent": "{{welcome-intent-name}}"
   }
}
```
