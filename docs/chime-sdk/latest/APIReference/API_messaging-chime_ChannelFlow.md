---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelFlow.html
---

# ChannelFlow
<a name="API_messaging-chime_ChannelFlow"></a>

The details of a channel flow.

## Contents
<a name="API_messaging-chime_ChannelFlow_Contents"></a>

 ** ChannelFlowArn **   <a name="chimesdk-Type-messaging-chime_ChannelFlow-ChannelFlowArn"></a>
The ARN of the channel flow.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-messaging-chime_ChannelFlow-CreatedTimestamp"></a>
The time at which the channel flow was created.
Type: Timestamp
Required: No

 ** LastUpdatedTimestamp **   <a name="chimesdk-Type-messaging-chime_ChannelFlow-LastUpdatedTimestamp"></a>
The time at which a channel flow was updated.
Type: Timestamp
Required: No

 ** Name **   <a name="chimesdk-Type-messaging-chime_ChannelFlow-Name"></a>
The name of the channel flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
Required: No

 ** Processors **   <a name="chimesdk-Type-messaging-chime_ChannelFlow-Processors"></a>
Information about the processor Lambda functions.
Type: Array of [Processor](API_messaging-chime_Processor.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: No

## See Also
<a name="API_messaging-chime_ChannelFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/ChannelFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/ChannelFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/ChannelFlow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
