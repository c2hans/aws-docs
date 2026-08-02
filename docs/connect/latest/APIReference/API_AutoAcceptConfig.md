---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AutoAcceptConfig.html
---

# AutoAcceptConfig
<a name="API_AutoAcceptConfig"></a>

Configuration settings for auto-accept for a specific channel.

## Contents
<a name="API_AutoAcceptConfig_Contents"></a>

 ** AutoAccept **   <a name="connect-Type-AutoAcceptConfig-AutoAccept"></a>
Indicates whether auto-accept is enabled for this channel. When enabled, available agents are automatically connected to contacts from this channel.
Type: Boolean
Required: Yes

 ** Channel **   <a name="connect-Type-AutoAcceptConfig-Channel"></a>
The channel for this auto-accept configuration. Valid values: VOICE, CHAT, TASK, EMAIL.
Type: String
Valid Values: `VOICE | CHAT | TASK | EMAIL`
Required: Yes

 ** AgentFirstCallbackAutoAccept **   <a name="connect-Type-AutoAcceptConfig-AgentFirstCallbackAutoAccept"></a>
Indicates whether auto-accept is enabled for agent-first callbacks. This setting only applies to the VOICE channel.
Type: Boolean
Required: No

## See Also
<a name="API_AutoAcceptConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AutoAcceptConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AutoAcceptConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AutoAcceptConfig)
