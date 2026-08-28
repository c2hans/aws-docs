---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ApprovalRuleEventMetadata.html
---

# ApprovalRuleEventMetadata
<a name="API_ApprovalRuleEventMetadata"></a>

Returns information about an event for an approval rule.

## Contents
<a name="API_ApprovalRuleEventMetadata_Contents"></a>

 ** approvalRuleContent **   <a name="CodeCommit-Type-ApprovalRuleEventMetadata-approvalRuleContent"></a>
The content of the approval rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3000.
Required: No

 ** approvalRuleId **   <a name="CodeCommit-Type-ApprovalRuleEventMetadata-approvalRuleId"></a>
The system-generated ID of the approval rule.
Type: String
Required: No

 ** approvalRuleName **   <a name="CodeCommit-Type-ApprovalRuleEventMetadata-approvalRuleName"></a>
The name of the approval rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_ApprovalRuleEventMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/ApprovalRuleEventMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/ApprovalRuleEventMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/ApprovalRuleEventMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
