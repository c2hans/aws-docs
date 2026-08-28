---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetApprovalTeamResponseApprover.html
---

# GetApprovalTeamResponseApprover
<a name="API_GetApprovalTeamResponseApprover"></a>

Contains details for an approver.

## Contents
<a name="API_GetApprovalTeamResponseApprover_Contents"></a>

 ** ApproverId **   <a name="mpa-Type-GetApprovalTeamResponseApprover-ApproverId"></a>
ID for the approver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** LastActivity **   <a name="mpa-Type-GetApprovalTeamResponseApprover-LastActivity"></a>
Last Activity performed by the approver.
Type: String
Valid Values: `VOTED | BASELINED | RESPONDED_TO_INVITATION`
Required: No

 ** LastActivityTime **   <a name="mpa-Type-GetApprovalTeamResponseApprover-LastActivityTime"></a>
Timestamp when the approver last responded to an operation or invitation request.
Type: Timestamp
Required: No

 ** MfaMethods **   <a name="mpa-Type-GetApprovalTeamResponseApprover-MfaMethods"></a>
Multi-factor authentication configuration for the approver
Type: Array of [MfaMethod](API_MfaMethod.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** PendingBaselineSessionArn **   <a name="mpa-Type-GetApprovalTeamResponseApprover-PendingBaselineSessionArn"></a>
Amazon Resource Name (ARN) for the pending baseline session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:mpa:[a-z0-9-]{1,20}:[0-9]{12}:session/[a-zA-Z0-9._-]+/[a-zA-Z0-9_-]+`
Required: No

 ** PrimaryIdentityId **   <a name="mpa-Type-GetApprovalTeamResponseApprover-PrimaryIdentityId"></a>
ID for the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** PrimaryIdentitySourceArn **   <a name="mpa-Type-GetApprovalTeamResponseApprover-PrimaryIdentitySourceArn"></a>
Amazon Resource Name (ARN) for the identity source. The identity source manages the user authentication for approvers.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** PrimaryIdentityStatus **   <a name="mpa-Type-GetApprovalTeamResponseApprover-PrimaryIdentityStatus"></a>
Status for the identity source. For example, if an approver has accepted a team invitation with a user authentication method managed by the identity source.
Type: String
Valid Values: `PENDING | ACCEPTED | REJECTED | INVALID`
Required: No

 ** ResponseTime **   <a name="mpa-Type-GetApprovalTeamResponseApprover-ResponseTime"></a>
Timestamp when the approver responded to an approval team invitation.
Type: Timestamp
Required: No

## See Also
<a name="API_GetApprovalTeamResponseApprover_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/GetApprovalTeamResponseApprover)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/GetApprovalTeamResponseApprover)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/GetApprovalTeamResponseApprover)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Multi-party approval. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mpa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
