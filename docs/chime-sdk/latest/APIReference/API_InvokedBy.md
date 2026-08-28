---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_InvokedBy.html
---

# InvokedBy
<a name="API_InvokedBy"></a>

Specifies the type of message that triggers a bot.

## Contents
<a name="API_InvokedBy_Contents"></a>

 ** StandardMessages **   <a name="chimesdk-Type-InvokedBy-StandardMessages"></a>
Sets standard messages as the bot trigger. For standard messages:
+  `ALL`: The bot processes all standard messages.
+  `AUTO`: The bot responds to `ALL` messages when the channel has one other non-hidden member, and responds to `MENTIONS` when the channel has more than one other non-hidden member.
+  `MENTIONS`: The bot processes all standard messages that have a message attribute with `CHIME.mentions` and a value of the bot ARN.
+  `NONE`: The bot processes no standard messages.
Type: String
Valid Values: `AUTO | ALL | MENTIONS | NONE`
Required: Yes

 ** TargetedMessages **   <a name="chimesdk-Type-InvokedBy-TargetedMessages"></a>
Sets targeted messages as the bot trigger. For targeted messages:
+  `ALL`: The bot processes all `TargetedMessages` sent to it. The bot then responds with a targeted message back to the sender.
+  `NONE`: The bot processes no targeted messages.
Type: String
Valid Values: `ALL | NONE`
Required: Yes

## See Also
<a name="API_InvokedBy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/InvokedBy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/InvokedBy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/InvokedBy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
