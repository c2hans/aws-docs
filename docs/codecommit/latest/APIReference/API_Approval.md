---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_Approval.html
---

# Approval
<a name="API_Approval"></a>

Returns information about a specific approval on a pull request.

## Contents
<a name="API_Approval_Contents"></a>

 ** approvalState **   <a name="CodeCommit-Type-Approval-approvalState"></a>
The state of the approval, APPROVE or REVOKE. REVOKE states are not stored.
Type: String
Valid Values: `APPROVE | REVOKE`
Required: No

 ** userArn **   <a name="CodeCommit-Type-Approval-userArn"></a>
The Amazon Resource Name (ARN) of the user.
Type: String
Required: No

## See Also
<a name="API_Approval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/Approval)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/Approval)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/Approval)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
