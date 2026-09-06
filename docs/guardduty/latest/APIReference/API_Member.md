---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Member.html
---

# Member
<a name="API_Member"></a>

Contains information about the member account.

## Contents
<a name="API_Member_Contents"></a>

 ** accountId **   <a name="guardduty-Type-Member-accountId"></a>
The ID of the member account.
Type: String
Length Constraints: Fixed length of 12.
Required: Yes

 ** email **   <a name="guardduty-Type-Member-email"></a>
The email address of the member account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** masterId **   <a name="guardduty-Type-Member-masterId"></a>
The administrator account ID.
Type: String
Required: Yes

 ** relationshipStatus **   <a name="guardduty-Type-Member-relationshipStatus"></a>
The status of the relationship between the member and the administrator.
Type: String
Required: Yes

 ** updatedAt **   <a name="guardduty-Type-Member-updatedAt"></a>
The last-updated timestamp of the member.
Type: String
Required: Yes

 ** administratorId **   <a name="guardduty-Type-Member-administratorId"></a>
The administrator account ID.
Type: String
Required: No

 ** detectorId **   <a name="guardduty-Type-Member-detectorId"></a>
The detector ID of the member account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** invitedAt **   <a name="guardduty-Type-Member-invitedAt"></a>
The timestamp when the invitation was sent.
Type: String
Required: No

## See Also
<a name="API_Member_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Member)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Member)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Member)
