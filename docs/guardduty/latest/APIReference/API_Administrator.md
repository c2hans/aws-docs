---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Administrator.html
---

# Administrator
<a name="API_Administrator"></a>

Contains information about the administrator account and invitation.

## Contents
<a name="API_Administrator_Contents"></a>

 ** accountId **   <a name="guardduty-Type-Administrator-accountId"></a>
The ID of the account used as the administrator account.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** invitationId **   <a name="guardduty-Type-Administrator-invitationId"></a>
The value that is used to validate the administrator account to the member account.
Type: String
Required: No

 ** invitedAt **   <a name="guardduty-Type-Administrator-invitedAt"></a>
The timestamp when the invitation was sent.
Type: String
Required: No

 ** relationshipStatus **   <a name="guardduty-Type-Administrator-relationshipStatus"></a>
The status of the relationship between the administrator and member accounts.
Type: String
Required: No

## See Also
<a name="API_Administrator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Administrator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Administrator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Administrator)
