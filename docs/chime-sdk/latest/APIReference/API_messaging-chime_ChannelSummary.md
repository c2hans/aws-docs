---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelSummary.html
---

# ChannelSummary
<a name="API_messaging-chime_ChannelSummary"></a>

Summary of the details of a `Channel`.

## Contents
<a name="API_messaging-chime_ChannelSummary_Contents"></a>

 ** ChannelArn **   <a name="chimesdk-Type-messaging-chime_ChannelSummary-ChannelArn"></a>
The ARN of the channel.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** LastMessageTimestamp **   <a name="chimesdk-Type-messaging-chime_ChannelSummary-LastMessageTimestamp"></a>
The time at which the last persistent message visible to the caller in a channel was sent.
Type: Timestamp
Required: No

 ** Metadata **   <a name="chimesdk-Type-messaging-chime_ChannelSummary-Metadata"></a>
The metadata of the channel.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Mode **   <a name="chimesdk-Type-messaging-chime_ChannelSummary-Mode"></a>
The mode of the channel.
Type: String
Valid Values: `UNRESTRICTED | RESTRICTED`
Required: No

 ** Name **   <a name="chimesdk-Type-messaging-chime_ChannelSummary-Name"></a>
The name of the channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
Required: No

 ** Privacy **   <a name="chimesdk-Type-messaging-chime_ChannelSummary-Privacy"></a>
The privacy setting of the channel.
Type: String
Valid Values: `PUBLIC | PRIVATE`
Required: No

## See Also
<a name="API_messaging-chime_ChannelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/ChannelSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/ChannelSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/ChannelSummary)
