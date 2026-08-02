---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_AppInstanceUserMembershipSummary.html
---

# AppInstanceUserMembershipSummary
<a name="API_messaging-chime_AppInstanceUserMembershipSummary"></a>

Summary of the membership details of an `AppInstanceUser`.

## Contents
<a name="API_messaging-chime_AppInstanceUserMembershipSummary_Contents"></a>

 ** ReadMarkerTimestamp **   <a name="chimesdk-Type-messaging-chime_AppInstanceUserMembershipSummary-ReadMarkerTimestamp"></a>
The time at which an `AppInstanceUser` last marked a channel as read.
Type: Timestamp
Required: No

 ** SubChannelId **   <a name="chimesdk-Type-messaging-chime_AppInstanceUserMembershipSummary-SubChannelId"></a>
The ID of the SubChannel that the `AppInstanceUser` is a member of.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

 ** Type **   <a name="chimesdk-Type-messaging-chime_AppInstanceUserMembershipSummary-Type"></a>
The type of `ChannelMembership`.
Type: String
Valid Values: `DEFAULT | HIDDEN`
Required: No

## See Also
<a name="API_messaging-chime_AppInstanceUserMembershipSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/AppInstanceUserMembershipSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/AppInstanceUserMembershipSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/AppInstanceUserMembershipSummary)
