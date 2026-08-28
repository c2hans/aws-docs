---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_QuickConnectConfig.html
---

# QuickConnectConfig
<a name="API_QuickConnectConfig"></a>

Contains configuration settings for a quick connect.

## Contents
<a name="API_QuickConnectConfig_Contents"></a>

 ** QuickConnectType **   <a name="connect-Type-QuickConnectConfig-QuickConnectType"></a>
The type of quick connect. In the Connect Customer admin website, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE\_NUMBER), or Queue (QUEUE).
Type: String
Valid Values: `USER | QUEUE | PHONE_NUMBER | FLOW`
Required: Yes

 ** FlowConfig **   <a name="connect-Type-QuickConnectConfig-FlowConfig"></a>
 Flow configuration for quick connect setup.
Type: [FlowQuickConnectConfig](API_FlowQuickConnectConfig.md) object
Required: No

 ** PhoneConfig **   <a name="connect-Type-QuickConnectConfig-PhoneConfig"></a>
The phone configuration. This is required only if QuickConnectType is PHONE\_NUMBER.
Type: [PhoneNumberQuickConnectConfig](API_PhoneNumberQuickConnectConfig.md) object
Required: No

 ** QueueConfig **   <a name="connect-Type-QuickConnectConfig-QueueConfig"></a>
The queue configuration. This is required only if QuickConnectType is QUEUE.
Type: [QueueQuickConnectConfig](API_QueueQuickConnectConfig.md) object
Required: No

 ** UserConfig **   <a name="connect-Type-QuickConnectConfig-UserConfig"></a>
The user configuration. This is required only if QuickConnectType is USER.
Type: [UserQuickConnectConfig](API_UserQuickConnectConfig.md) object
Required: No

## See Also
<a name="API_QuickConnectConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/QuickConnectConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/QuickConnectConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/QuickConnectConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
