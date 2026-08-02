---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_Channel.html
---

# Channel
<a name="API_messaging-chime_Channel"></a>

The details of a channel.

## Contents
<a name="API_messaging-chime_Channel_Contents"></a>

 ** ChannelArn **   <a name="chimesdk-Type-messaging-chime_Channel-ChannelArn"></a>
The ARN of a channel.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** ChannelFlowArn **   <a name="chimesdk-Type-messaging-chime_Channel-ChannelFlowArn"></a>
The ARN of the channel flow.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** CreatedBy **   <a name="chimesdk-Type-messaging-chime_Channel-CreatedBy"></a>
The `AppInstanceUser` who created the channel.
Type: [Identity](API_messaging-chime_Identity.md) object
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-messaging-chime_Channel-CreatedTimestamp"></a>
The time at which the `AppInstanceUser` created the channel.
Type: Timestamp
Required: No

 ** ElasticChannelConfiguration **   <a name="chimesdk-Type-messaging-chime_Channel-ElasticChannelConfiguration"></a>
The attributes required to configure and create an elastic channel. An elastic channel can support a maximum of 1-million members.
Type: [ElasticChannelConfiguration](API_messaging-chime_ElasticChannelConfiguration.md) object
Required: No

 ** ExpirationSettings **   <a name="chimesdk-Type-messaging-chime_Channel-ExpirationSettings"></a>
Settings that control when a channel expires.
Type: [ExpirationSettings](API_messaging-chime_ExpirationSettings.md) object
Required: No

 ** LastMessageTimestamp **   <a name="chimesdk-Type-messaging-chime_Channel-LastMessageTimestamp"></a>
The time at which a member sent the last message in the channel.
Type: Timestamp
Required: No

 ** LastUpdatedTimestamp **   <a name="chimesdk-Type-messaging-chime_Channel-LastUpdatedTimestamp"></a>
The time at which a channel was last updated.
Type: Timestamp
Required: No

 ** Metadata **   <a name="chimesdk-Type-messaging-chime_Channel-Metadata"></a>
The channel's metadata.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Mode **   <a name="chimesdk-Type-messaging-chime_Channel-Mode"></a>
The mode of the channel.
Type: String
Valid Values: `UNRESTRICTED | RESTRICTED`
Required: No

 ** Name **   <a name="chimesdk-Type-messaging-chime_Channel-Name"></a>
The name of a channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
Required: No

 ** Privacy **   <a name="chimesdk-Type-messaging-chime_Channel-Privacy"></a>
The channel's privacy setting.
Type: String
Valid Values: `PUBLIC | PRIVATE`
Required: No

## See Also
<a name="API_messaging-chime_Channel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/Channel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/Channel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/Channel)
