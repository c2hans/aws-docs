---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/create-lex-bot.html
---

# Creating an Amazon Lex V2 bot for Amazon Chime SDK messaging
<a name="create-lex-bot"></a>

To use AppInstance bots as agents, you first need to create an Amazon Lex V2 bot to manage the dialog interaction for an intelligent-agent scenario. To get started building an Amazon Lex V2 bot, see [Getting Started with Amazon Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/getting-started.html) in the *Amazon Lex V2 Developer Guide*. For information about migrating an Amazon Lex V1 bot to Amazon Lex V2, see the [Amazon Lex V1 to V2 migration guide](https://docs.aws.amazon.com/lexv2/latest/dg/migration.html).

**Topics**
+ [Prerequisites](#lex-prereqs)
+ [Granting invocation permissions](#invocation-perms)
+ [Creating a welcome intent for Amazon Chime SDK messaging](welcome-intent.md)
+ [Creating Amazon Lex V2 bot versions for Amazon Chime SDK messaging](lex-versions.md)
+ [Creating Amazon Lex V2 bot aliases for Amazon Chime SDK messaging](lex-aliases.md)

## Prerequisites
<a name="lex-prereqs"></a>

Your Amazon Lex V2 bot must have the following prerequisites.
+ You must create the bot in an AWS Region that supports Amazon Lex V2 runtime endpoints.
+ You must create the bot in the same AWS account and Region as the `AppInstance` and `AppInstanceBot`.
+ The bot must grant invocation permissions via a resource-based policy to the `messaging.chime.amazonaws.com` service principal.
+ The bot can model a Welcome Intent. This allows `AppInstanceBot` to announce itself and its capabilities upon membership in a channel.
+ The bot should have a production version and aliases in order to configure the `AppInstanceBot`.
+ The bot must use a supported language and locale. For more information about languages and locales, see [Languages and locales supported in Amazon Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html) in the *Amazon Lex V2 Developer Guide*.

## Granting invocation permissions
<a name="invocation-perms"></a>

For an `AppInstanceBot` to invoke an Amazon Lex V2 Bot, the Amazon Chime SDK messaging service principal must have permission to invoke the Amazon Lex Bot resource. For more information about Amazon Lex V2 resource-based policy permissions, see [Resource-based policy examples for Amazon Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/security_iam_resource-based-policy-examples.html) in the *Amazon Lex V2 Developer Guide*.

The following example shows a resource-based policy.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "messaging.chime.amazonaws.com"
      },
      "Action": [
        "lex:PutSession",
        "lex:DeleteSession",
        "lex:RecognizeText"
      ],
      "Resource": "arn:aws:lex:{{us-east-1}}:{{111122223333}}:{{bot-alias}}/{{lex-bot-id}}/{{lex-bot-alias-id}}",
      "Condition": {
        "StringEquals": {
        "AWS:SourceAccount": "{{111122223333}}"
        },
        "ArnEquals": {
        "AWS:SourceArn": "arn:aws:chime:{{us-east-1}}:{{111122223333}}:{{app-instance}}/{{app-instance-id}}/bot/{{app-instance-bot-id}}"
        }
      }
    }
  ]
}
```

------

**Note**
To allow one `AppInstanceBot` to invoke an Amazon Lex V2 bot, use the AppInstanceBot's ID. To allow all `AppInstanceBots` within an `AppInstance` to invoke an Amazon Lex V2 bot, use a wildcard. For example:
`arn:aws:chime:{{region}}:{{aws-account-id}}:{{app-instance}}/{{app-instance-id}}/bot/*`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
