---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelMembership.html
---

# ChannelMembership
<a name="API_messaging-chime_ChannelMembership"></a>

The details of a channel member.

## Contents
<a name="API_messaging-chime_ChannelMembership_Contents"></a>

 ** ChannelArn **   <a name="chimesdk-Type-messaging-chime_ChannelMembership-ChannelArn"></a>
The ARN of the member's channel.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-messaging-chime_ChannelMembership-CreatedTimestamp"></a>
The time at which the channel membership was created.
Type: Timestamp
Required: No

 ** InvitedBy **   <a name="chimesdk-Type-messaging-chime_ChannelMembership-InvitedBy"></a>
The identifier of the member who invited another member.
Type: [Identity](API_messaging-chime_Identity.md) object
Required: No

 ** LastUpdatedTimestamp **   <a name="chimesdk-Type-messaging-chime_ChannelMembership-LastUpdatedTimestamp"></a>
The time at which a channel membership was last updated.
Type: Timestamp
Required: No

 ** Member **   <a name="chimesdk-Type-messaging-chime_ChannelMembership-Member"></a>
The data of the channel member.
Type: [Identity](API_messaging-chime_Identity.md) object
Required: No

 ** SubChannelId **   <a name="chimesdk-Type-messaging-chime_ChannelMembership-SubChannelId"></a>
The ID of the SubChannel that a user belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

 ** Type **   <a name="chimesdk-Type-messaging-chime_ChannelMembership-Type"></a>
The membership type set for the channel member.
Type: String
Valid Values: `DEFAULT | HIDDEN`
Required: No

## See Also
<a name="API_messaging-chime_ChannelMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/ChannelMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/ChannelMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/ChannelMembership)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
