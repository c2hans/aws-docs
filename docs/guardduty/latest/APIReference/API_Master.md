---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Master.html
---

# Master
<a name="API_Master"></a>

Contains information about the administrator account and invitation.

## Contents
<a name="API_Master_Contents"></a>

 ** accountId **   <a name="guardduty-Type-Master-accountId"></a>
The ID of the account used as the administrator account.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** invitationId **   <a name="guardduty-Type-Master-invitationId"></a>
The value used to validate the administrator account to the member account.
Type: String
Required: No

 ** invitedAt **   <a name="guardduty-Type-Master-invitedAt"></a>
The timestamp when the invitation was sent.
Type: String
Required: No

 ** relationshipStatus **   <a name="guardduty-Type-Master-relationshipStatus"></a>
The status of the relationship between the administrator and member accounts.
Type: String
Required: No

## See Also
<a name="API_Master_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Master)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Master)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Master)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
