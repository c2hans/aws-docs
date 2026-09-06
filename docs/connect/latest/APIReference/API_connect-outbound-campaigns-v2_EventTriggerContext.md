---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_EventTriggerContext.html
---

# EventTriggerContext
<a name="API_connect-outbound-campaigns-v2_EventTriggerContext"></a>

Contains context data for an event trigger, including the originating source event and the channel context.

## Contents
<a name="API_connect-outbound-campaigns-v2_EventTriggerContext_Contents"></a>

 ** channelContext **   <a name="connect-Type-connect-outbound-campaigns-v2_EventTriggerContext-channelContext"></a>
The channel context for the event trigger, such as a web notification.
Type: [ChannelContext](API_connect-outbound-campaigns-v2_ChannelContext.md) object
Required: No

 ** sourceEvent **   <a name="connect-Type-connect-outbound-campaigns-v2_EventTriggerContext-sourceEvent"></a>
The source event object for the event trigger.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_EventTriggerContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/EventTriggerContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/EventTriggerContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/EventTriggerContext)
