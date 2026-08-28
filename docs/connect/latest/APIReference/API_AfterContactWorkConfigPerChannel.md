---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AfterContactWorkConfigPerChannel.html
---

# AfterContactWorkConfigPerChannel
<a name="API_AfterContactWorkConfigPerChannel"></a>

Configuration settings for after contact work (ACW) timeout for a specific channel.

## Contents
<a name="API_AfterContactWorkConfigPerChannel_Contents"></a>

 ** AfterContactWorkConfig **   <a name="connect-Type-AfterContactWorkConfigPerChannel-AfterContactWorkConfig"></a>
The ACW timeout settings for this channel.
Type: [AfterContactWorkConfig](API_AfterContactWorkConfig.md) object
Required: Yes

 ** Channel **   <a name="connect-Type-AfterContactWorkConfigPerChannel-Channel"></a>
The channel for this ACW timeout configuration. Valid values: VOICE, CHAT, TASK, EMAIL.
Type: String
Valid Values: `VOICE | CHAT | TASK | EMAIL`
Required: Yes

 ** AgentFirstCallbackAfterContactWorkConfig **   <a name="connect-Type-AfterContactWorkConfigPerChannel-AgentFirstCallbackAfterContactWorkConfig"></a>
The ACW timeout settings for agent-first callbacks. This setting only applies to the VOICE channel.
Type: [AfterContactWorkConfig](API_AfterContactWorkConfig.md) object
Required: No

## See Also
<a name="API_AfterContactWorkConfigPerChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AfterContactWorkConfigPerChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AfterContactWorkConfigPerChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AfterContactWorkConfigPerChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
