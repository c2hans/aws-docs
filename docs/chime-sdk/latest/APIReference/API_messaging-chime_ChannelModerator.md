---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelModerator.html
---

# ChannelModerator
<a name="API_messaging-chime_ChannelModerator"></a>

The details of a channel moderator.

## Contents
<a name="API_messaging-chime_ChannelModerator_Contents"></a>

 ** ChannelArn **   <a name="chimesdk-Type-messaging-chime_ChannelModerator-ChannelArn"></a>
The ARN of the moderator's channel.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** CreatedBy **   <a name="chimesdk-Type-messaging-chime_ChannelModerator-CreatedBy"></a>
The `AppInstanceUser` who created the moderator.
Type: [Identity](API_messaging-chime_Identity.md) object
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-messaging-chime_ChannelModerator-CreatedTimestamp"></a>
The time at which the moderator was created.
Type: Timestamp
Required: No

 ** Moderator **   <a name="chimesdk-Type-messaging-chime_ChannelModerator-Moderator"></a>
The moderator's data.
Type: [Identity](API_messaging-chime_Identity.md) object
Required: No

## See Also
<a name="API_messaging-chime_ChannelModerator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/ChannelModerator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/ChannelModerator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/ChannelModerator)
