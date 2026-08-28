---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_ApprovalTeamRequestApprover.html
---

# ApprovalTeamRequestApprover
<a name="API_ApprovalTeamRequestApprover"></a>

Contains details for an approver.

## Contents
<a name="API_ApprovalTeamRequestApprover_Contents"></a>

 ** PrimaryIdentityId **   <a name="mpa-Type-ApprovalTeamRequestApprover-PrimaryIdentityId"></a>
ID for the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** PrimaryIdentitySourceArn **   <a name="mpa-Type-ApprovalTeamRequestApprover-PrimaryIdentitySourceArn"></a>
Amazon Resource Name (ARN) for the identity source. The identity source manages the user authentication for approvers.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

## See Also
<a name="API_ApprovalTeamRequestApprover_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/ApprovalTeamRequestApprover)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/ApprovalTeamRequestApprover)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/ApprovalTeamRequestApprover)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Multi-party approval. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mpa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
