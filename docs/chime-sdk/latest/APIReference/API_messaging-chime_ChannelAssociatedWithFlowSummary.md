---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelAssociatedWithFlowSummary.html
---

# ChannelAssociatedWithFlowSummary
<a name="API_messaging-chime_ChannelAssociatedWithFlowSummary"></a>

Summary of details of a channel associated with channel flow.

## Contents
<a name="API_messaging-chime_ChannelAssociatedWithFlowSummary_Contents"></a>

 ** ChannelArn **   <a name="chimesdk-Type-messaging-chime_ChannelAssociatedWithFlowSummary-ChannelArn"></a>
The ARN of the channel.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** Metadata **   <a name="chimesdk-Type-messaging-chime_ChannelAssociatedWithFlowSummary-Metadata"></a>
The channel's metadata.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Mode **   <a name="chimesdk-Type-messaging-chime_ChannelAssociatedWithFlowSummary-Mode"></a>
The mode of the channel.
Type: String
Valid Values: `UNRESTRICTED | RESTRICTED`
Required: No

 ** Name **   <a name="chimesdk-Type-messaging-chime_ChannelAssociatedWithFlowSummary-Name"></a>
The name of the channel flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
Required: No

 ** Privacy **   <a name="chimesdk-Type-messaging-chime_ChannelAssociatedWithFlowSummary-Privacy"></a>
The channel's privacy setting.
Type: String
Valid Values: `PUBLIC | PRIVATE`
Required: No

## See Also
<a name="API_messaging-chime_ChannelAssociatedWithFlowSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/ChannelAssociatedWithFlowSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/ChannelAssociatedWithFlowSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/ChannelAssociatedWithFlowSummary)
