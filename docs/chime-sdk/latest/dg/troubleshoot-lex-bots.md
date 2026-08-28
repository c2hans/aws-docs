---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/troubleshoot-lex-bots.html
---

# Troubleshooting AppInstanceBots configured with Amazon Lex V2 bots for Amazon Chime SDK messaging
<a name="troubleshoot-lex-bots"></a>

The following topics explain how to troubleshoot common problems with AppInstanceBots.

## Finding Amazon Lex V2 failures
<a name="find-lex-failures"></a>

The Amazon Chime SDK messaging delivers [Amazon EventBridge events](https://docs.aws.amazon.com/chime-sdk/latest/dg/event-bridge-alerts.html) when an error prevents it from invoking the Amazon Lex V2 bot. For more information about setting up rules and configuring notification targets, refer to [Getting started with Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html) in the *Amazon EventBridge User Guide*.

If you receive EventBridge events in AWS CloudWatch Logs, you can use AWS CloudWatch Logs Insights to query EventBridge events based on the Amazon Chime SDK messaging detail-type. The `failureReason` lists the cause of the failure.

The following example shows a typical query.

```
fields @timestamp, @message
| filter `detail-type` = "Chime Messaging AppInstanceBot Lex Failure"
| sort @timestamp desc
```

If Amazon Chime SDK Messaging can invoke your Amazon Lex V2 bot, the SDK sends `CONTROL` messages with an error message.

## Troubleshooting Amazon Lex V2 bot permission errors
<a name="lex-permission-errors"></a>

For an AppInstanceBot to invoke an Amazon Lex V2 Bot, the Amazon Chime SDK messaging service principal must have permission to invoke the Amazon Lex V2 Bot resource. Also, ensure the `AWS:SourceArn` of the resource policy condition matches the ARN of the AppInstanceBot.

For more information about configuring an AppInstanceBot to invoke an Amazon Lex V2 bot, refer to [Creating an Amazon Lex V2 bot for Amazon Chime SDK messaging](create-lex-bot.md), earlier in this section.

## Troubleshooting Amazon Lex V2 bot throttling
<a name="lex-throttling"></a>

Amazon Lex has a service quota for the maximum number of concurrent text-mode conversations per bot alias. You can contact the Amazon Lex service team for quota increases. For more information, refer to [Amazon Lex guidelines and quotas](https://docs.aws.amazon.com/lexv2/latest/dg/quotas.html) in the *Amazon Lex Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
