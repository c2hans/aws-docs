---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_BatchChannelMemberships.html
---

# BatchChannelMemberships
<a name="API_messaging-chime_BatchChannelMemberships"></a>

The membership information, including member ARNs, the channel ARN, and membership types.

## Contents
<a name="API_messaging-chime_BatchChannelMemberships_Contents"></a>

 ** ChannelArn **   <a name="chimesdk-Type-messaging-chime_BatchChannelMemberships-ChannelArn"></a>
The ARN of the channel to which you're adding members.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** InvitedBy **   <a name="chimesdk-Type-messaging-chime_BatchChannelMemberships-InvitedBy"></a>
The identifier of the member who invited another member.
Type: [Identity](API_messaging-chime_Identity.md) object
Required: No

 ** Members **   <a name="chimesdk-Type-messaging-chime_BatchChannelMemberships-Members"></a>
The users successfully added to the request.
Type: Array of [Identity](API_messaging-chime_Identity.md) objects
Required: No

 ** SubChannelId **   <a name="chimesdk-Type-messaging-chime_BatchChannelMemberships-SubChannelId"></a>
The ID of the SubChannel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

 ** Type **   <a name="chimesdk-Type-messaging-chime_BatchChannelMemberships-Type"></a>
The membership types set for the channel members.
Type: String
Valid Values: `DEFAULT | HIDDEN`
Required: No

## See Also
<a name="API_messaging-chime_BatchChannelMemberships_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/BatchChannelMemberships)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/BatchChannelMemberships)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/BatchChannelMemberships)
