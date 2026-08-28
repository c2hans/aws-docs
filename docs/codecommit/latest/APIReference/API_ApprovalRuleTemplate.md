---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ApprovalRuleTemplate.html
---

# ApprovalRuleTemplate
<a name="API_ApprovalRuleTemplate"></a>

Returns information about an approval rule template.

## Contents
<a name="API_ApprovalRuleTemplate_Contents"></a>

 ** approvalRuleTemplateContent **   <a name="CodeCommit-Type-ApprovalRuleTemplate-approvalRuleTemplateContent"></a>
The content of the approval rule template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3000.
Required: No

 ** approvalRuleTemplateDescription **   <a name="CodeCommit-Type-ApprovalRuleTemplate-approvalRuleTemplateDescription"></a>
The description of the approval rule template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** approvalRuleTemplateId **   <a name="CodeCommit-Type-ApprovalRuleTemplate-approvalRuleTemplateId"></a>
The system-generated ID of the approval rule template.
Type: String
Required: No

 ** approvalRuleTemplateName **   <a name="CodeCommit-Type-ApprovalRuleTemplate-approvalRuleTemplateName"></a>
The name of the approval rule template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** creationDate **   <a name="CodeCommit-Type-ApprovalRuleTemplate-creationDate"></a>
The date the approval rule template was created, in timestamp format.
Type: Timestamp
Required: No

 ** lastModifiedDate **   <a name="CodeCommit-Type-ApprovalRuleTemplate-lastModifiedDate"></a>
The date the approval rule template was most recently changed, in timestamp format.
Type: Timestamp
Required: No

 ** lastModifiedUser **   <a name="CodeCommit-Type-ApprovalRuleTemplate-lastModifiedUser"></a>
The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule template.
Type: String
Required: No

 ** ruleContentSha256 **   <a name="CodeCommit-Type-ApprovalRuleTemplate-ruleContentSha256"></a>
The SHA-256 hash signature for the content of the approval rule template.
Type: String
Required: No

## See Also
<a name="API_ApprovalRuleTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/ApprovalRuleTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/ApprovalRuleTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/ApprovalRuleTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
