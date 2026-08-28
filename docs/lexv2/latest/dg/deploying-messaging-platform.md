---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/deploying-messaging-platform.html
---

# Integrating an Amazon Lex V2 bot with a messaging platform
<a name="deploying-messaging-platform"></a>

This section explains how to integrate Amazon Lex V2 bots with the Facebook, Slack, and Twilio messaging platforms. If you don't already have an Amazon Lex V2 bot, create one. In this topic, we assume that you are using the bot that you created in [Exercise 1: Create a chatbot from a template](exercise-1.md). However, you can use any bot.

**Note**
When storing your Facebook, Slack, or Twilio configurations, Amazon Lex V2 uses an AWS KMS key to encrypt information. The first time that you create a channel to one of these messaging platforms, Amazon Lex V2 creates a default customer managed key (`aws/lex`) in your AWS account or you can select your own customer managed key. Amazon Lex V2 supports only symmetric keys. For more information, see the [AWS Key Management Service Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/).

When a messaging platform sends a request to Amazon Lex V2 it includes platform-specific information as a request attribute to you Lambda function. Use this attribute to customize the way that your bot behaves. For more information, see [Setting request attributes for your Lex V2 bot](context-mgmt-request-attribs.md).

**Common request attributes for messaging platforms**

| Attribute | Description |
| --- | --- |
| x-amz-lex:channels:platform | One of the following values:+  `Facebook` <br />+  `Slack` <br />+  `Twilio`  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
