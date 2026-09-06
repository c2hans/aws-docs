---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ApprovalRule.html
---

# ApprovalRule
<a name="API_ApprovalRule"></a>

Returns information about an approval rule.

## Contents
<a name="API_ApprovalRule_Contents"></a>

 ** approvalRuleContent **   <a name="CodeCommit-Type-ApprovalRule-approvalRuleContent"></a>
The content of the approval rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3000.
Required: No

 ** approvalRuleId **   <a name="CodeCommit-Type-ApprovalRule-approvalRuleId"></a>
The system-generated ID of the approval rule.
Type: String
Required: No

 ** approvalRuleName **   <a name="CodeCommit-Type-ApprovalRule-approvalRuleName"></a>
The name of the approval rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** creationDate **   <a name="CodeCommit-Type-ApprovalRule-creationDate"></a>
The date the approval rule was created, in timestamp format.
Type: Timestamp
Required: No

 ** lastModifiedDate **   <a name="CodeCommit-Type-ApprovalRule-lastModifiedDate"></a>
The date the approval rule was most recently changed, in timestamp format.
Type: Timestamp
Required: No

 ** lastModifiedUser **   <a name="CodeCommit-Type-ApprovalRule-lastModifiedUser"></a>
The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule.
Type: String
Required: No

 ** originApprovalRuleTemplate **   <a name="CodeCommit-Type-ApprovalRule-originApprovalRuleTemplate"></a>
The approval rule template used to create the rule.
Type: [OriginApprovalRuleTemplate](API_OriginApprovalRuleTemplate.md) object
Required: No

 ** ruleContentSha256 **   <a name="CodeCommit-Type-ApprovalRule-ruleContentSha256"></a>
The SHA-256 hash signature for the content of the approval rule.
Type: String
Required: No

## See Also
<a name="API_ApprovalRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/ApprovalRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/ApprovalRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/ApprovalRule)
